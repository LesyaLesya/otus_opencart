"""Модуль с фикстурами."""


import allure
import mysql.connector
import pytest
import requests
import time
from types import SimpleNamespace
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChOp
from selenium.webdriver.firefox.options import Options as FFOp
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from helpers import allure_helper


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
# https://github.com/pytest-dev/pytest/issues/230#issuecomment-402580536
def pytest_runtest_makereport(item):
    """Хук для установки статуса теста."""
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != 'passed':
        item.status = 'failed'
    else:
        item.status = 'passed'


def url_data(url_link, timeout=15):
    """Ожидание доступности видео."""
    while timeout:
        response = requests.get(url_link)
        if not response.ok:
            time.sleep(1)
            timeout -= 1
        else:
            if 'video' in url_link:
                return response.content
            else:
                return response.text
    return None


def pytest_addoption(parser):
    """Получение аргументов из командной строки."""
    parser.addoption(
        '--url', action='store', required=True, help='Укажите url приложения')
    parser.addoption(
        '--browser-name', action='store', required=True, choices=['chrome', 'firefox'],
        help='Укажите браузер: chrome, firefox')
    parser.addoption(
        '--browser-version', action='store', help='Укажите версию браузера - для запуска через selenoid')
    parser.addoption(
        '--local', action='store_true',
        help='Укажите флаг для локального запуска драйвера, без флага - для удаленного запуска')
    parser.addoption(
        '--executor', action='store',
        help='если local False - укажите хост selenoid, если True - не надо передавать параметр')


@pytest.fixture
def url(request):
    """Фикстура, возвращающая url, переданный в командной строке."""
    get_url = request.config.getoption('--url')
    return f'http://{get_url}'


@pytest.fixture
def browser(request, db_connection):
    """Фикстура для запуска драйвера в зависимости от параметров."""
    browser_name = request.config.getoption('--browser-name')
    browser_version = request.config.getoption('--browser-version')
    executor = request.config.getoption('--executor')
    local = request.config.getoption('--local')
    test_name = request.node.name

    capabilities = {
        'browserName': browser_name,
        'browserVersion': browser_version,
        'screenResolution': '1440x900',
        'name': test_name,
        'selenoid:options': {
            'enableVNC': True,
            'enableVideo': True}}

    if local:
        if browser_name == 'chrome':
            options = ChOp()
            options.headless = True
            driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
        elif browser_name == 'firefox':
            options = FFOp()
            options.headless = True
            driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())
        else:
            raise pytest.UsageError('Для локального запуска --browser_name - chrome или firefox')
        allure_helper.attach_capabilities(driver)
        allure_helper.add_allure_env(browser_name, browser_version, local)
        request.addfinalizer(driver.quit)
        driver.maximize_window()
        return driver
    else:
        driver = webdriver.Remote(
            command_executor=f'http://{executor}:4444/wd/hub', desired_capabilities=capabilities)
        allure_helper.attach_capabilities(driver)
        allure_helper.add_allure_env(browser_name, browser_version, local)

        def finalizer():
            video = f'http://{executor}:8080/video/{driver.session_id}.mp4'
            driver.quit()
            # В случае ошибки прикрепляем к отчету видео
            if request.node.status != 'passed':
                allure.attach(
                    name='video_for_' + driver.session_id,
                    body=url_data(video),
                    attachment_type=allure.attachment_type.MP4)
            # Удаляем видео из selenoid
            if url_data(video):
                requests.delete(video)

        request.addfinalizer(finalizer)
        driver.maximize_window()
        return driver


@pytest.fixture(scope='session')
def db_connection(request):
    db_host = request.config.getoption('--url')
    config = SimpleNamespace(
        DB_NAME='bitnami_opencart',
        HOST=db_host,
        PORT='3306',
        USER='bn_opencart',
        PASSWORD=''
    )
    connection = mysql.connector.connect(
        user=config.USER,
        password=config.PASSWORD,
        host=config.HOST,
        port=config.PORT,
        database=config.DB_NAME
    )
    request.addfinalizer(connection.close)
    return connection

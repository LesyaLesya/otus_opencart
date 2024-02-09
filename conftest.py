"""Модуль с фикстурами."""


import allure
import mysql.connector
import pytest
import requests
import time


from faker import Faker
from types import SimpleNamespace
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChOp
from selenium.webdriver.firefox.options import Options as FFOp
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from helpers import allure_helper
from helpers import db_queries


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
    parser.addoption(
        '--window_size', default='1920,1080', help='Укажите разрешение в формате "1920,1080"'
    )


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
    window_size = request.config.getoption('--window_size')
    window_size_for_selenoid = window_size.replace(',', 'x')
    window_width, window_height = window_size.split(',')
    test_name = request.node.name

    capabilities = {
        'browserName': browser_name,
        'browserVersion': browser_version,
        'screenResolution': window_size_for_selenoid,
        'name': test_name,
        'selenoid:options': {
            'enableVNC': True,
            'enableVideo': True},
        'acceptInsecureCerts': True}

    if local:
        if browser_name == 'chrome':
            options = ChOp()
            options.add_argument('--headless')
            options.add_argument('--incognito')
            options.add_argument('--ignore-certificate-errors')
            options.add_argument(f'--window-size={window_size}')
            options.add_argument('--disable-cache')
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36”)')
            driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
        elif browser_name == 'firefox':
            options = FFOp()
            profile = webdriver.FirefoxProfile()
            profile.accept_untrusted_certs = True
            profile.set_preference('general.useragent.override',
                                   'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) '
                                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36')
            options.add_argument('--headless')
            options.add_argument('--private')
            options.add_argument(f'--width={window_width}')
            options.add_argument(f'--height={window_height}')
            driver = webdriver.Firefox(options=options, firefox_profile=profile,
                                       executable_path=GeckoDriverManager().install())
        else:
            raise pytest.UsageError('Для локального запуска --browser_name - chrome или firefox')
        allure_helper.attach_capabilities(driver)
        allure_helper.add_allure_env(browser_name, browser_version, local)
        request.addfinalizer(driver.quit)
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
    cursor = connection.cursor()
    yield cursor
    connection.commit()
    cursor.close()
    connection.close()


@pytest.fixture
def do_fake():
    fake = Faker(['en_US'])
    return fake


@pytest.fixture
def delete_user(db_connection):
    """Фикстура, удаляющая пользователя."""
    def __del_user_from_bd(user_id):
        return db_queries.delete_user(db_connection, user_id)
    return __del_user_from_bd


@pytest.fixture
def create_user(db_connection, do_fake):
    """Фикстура, создающая пользователя."""
    @allure.step(
        'Создать пользователя: firstname={firstname}, lastname={lastname}, email={email}, telephone={telephone}')
    def __create_user(email=None, firstname=None, lastname=None, telephone=None):
        if email is None:
            email = do_fake.ascii_free_email()
        else:
            email = email

        if firstname is None:
            firstname = do_fake.first_name()
        else:
            firstname = firstname

        if lastname is None:
            lastname = do_fake.last_name()
        else:
            lastname = lastname

        if telephone is None:
            telephone = do_fake.phone_number()
        else:
            telephone = telephone

        db_queries.create_test_user(db_connection, email, firstname, lastname, telephone)
        user_id = db_queries.get_user_id(db_connection, email, firstname, lastname, telephone)
        return email, firstname, lastname, telephone, user_id
    return __create_user


@pytest.fixture
def fixture_create_delete_user(create_user, delete_user):
    """Фикстура создания и удаления пользователя."""
    email, firstname, lastname, telephone, user_id = create_user()
    yield email, firstname, lastname, telephone, user_id
    delete_user(user_id)

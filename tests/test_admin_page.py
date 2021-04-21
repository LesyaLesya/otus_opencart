"""Модуль с тестами для Административной страницы."""


import pytest
import allure
from pages.admin_page import AdminPage
from pages.locators import AdminPageLocators


@allure.feature("Административная страница")
@allure.story("Проверка присутствия элементов на Административной странице")
@allure.title("Поиск элемента {locator}")
@allure.link("#", name="User story")
@pytest.mark.parametrize("locator",
                         [AdminPageLocators.PANEL_HEADING,
                          AdminPageLocators.USERNAME_INPUT,
                          AdminPageLocators.PASSWORD_INPUT,
                          AdminPageLocators.LOGIN_BUTTON,
                          AdminPageLocators.HELP_BLOCK],
                         ids=["PANEL_HEADING", "USERNAME_INPUT",
                              "PASSWORD_INPUT", "LOGIN_BUTTON",
                              "HELP_BLOCK"])
def test_presence_of_elements_on_admin_login_page(browser, url, locator):
    """Тестовая функция для проверки видимости элементов на странице Каталога.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    :param locator: путь до элемента
    """
    url = f'{url}admin/'
    page = AdminPage(browser, url)
    page.open_url()
    page.is_element_visible(*locator)


@allure.feature("Административная страница")
@allure.story("Авторизация в админке")
@allure.title("Валидные креденшелы")
@allure.link("#", name="User story")
def test_login_valid(browser, url):
    """Тестовая функция для проверки логина в админку с валидными креденшелами.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    """
    url = f'{url}admin/'
    page = AdminPage(browser, url)
    page.open_url()
    page.set_username("user")
    page.set_password("bitnami")
    page.login_button_click()
    page.is_title_correct("Dashboard")


@allure.feature("Административная страница")
@allure.story("Авторизация в админке")
@allure.title("Невалидные креденшелы")
@allure.link("#", name="User story")
@pytest.mark.parametrize("login, passw", [("test", "test"),
                                          ("123", "")])
def test_login_failed(browser, url, login, passw):
    """Тестовая функция для проверки логина в админку с невалидными креденшелами.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    :param login: передаваемый логин
    :param passw: передаваемый пароль
    """
    url = f'{url}admin/'
    page = AdminPage(browser, url)
    page.open_url()
    page.set_username(login)
    page.set_password(passw)
    page.login_button_click()
    page.should_be_fail_login_alert()


@allure.feature("Административная страница")
@allure.title("Выход из админки")
@allure.link("#", name="User story")
@allure.description(" Проверка разлогина из админки")
def test_logout(browser, url):
    """Тестовая функция для проверки разлогина из админки.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    """
    url = f'{url}admin/'
    page = AdminPage(browser, url)
    page.open_url()
    page.set_username("user")
    page.set_password("bitnami")
    page.login_button_click()
    page.logout()
    page.should_be_successful_logout_text()


@allure.feature("Административная страница")
@allure.story("Таблица с товарами")
@allure.title("Отображение таблицы с товарами в админке")
@allure.link("#", name="User story")
def test_get_products_table(browser, url):
    """Тестовая функция для проверки отображения таблицы с товарами в админке.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    """
    url = f'{url}admin/'
    page = AdminPage(browser, url)
    page.open_url()
    page.set_username("user")
    page.set_password("bitnami")
    page.login_button_click()
    page.get_product_table()
    page.should_be_products_table()

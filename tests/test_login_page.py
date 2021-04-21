"""Модуль с тестами для страницы Логина."""


import pytest
import allure
from pages.locators import LoginPageLocators
from pages.login_page import LoginPage
from pages.account_page import AccountPage


@allure.feature("Страница логина")
@allure.story("Проверка присутствия элементов на странице Логина")
@allure.title("Поиск элемента {locator}")
@allure.link("#", name="User story")
@pytest.mark.parametrize("locator",
                         [LoginPageLocators.NEW_CUSTOMER_FORM,
                          LoginPageLocators.OLD_CUSTOMER_FORM,
                          LoginPageLocators.RIGHT_LIST_MENU,
                          LoginPageLocators.BUTTON_FOR_NEW_CUSTOMER,
                          LoginPageLocators.BUTTON_FOR_OLD_CUSTOMER],
                         ids=["NEW_CUSTOMER_FORM", "OLD_CUSTOMER_FORM",
                              "RIGHT_LIST_MENU", "BUTTON_FOR_NEW_CUSTOMER",
                              "BUTTON_FOR_OLD_CUSTOMER"])
def test_presence_of_elements_on_login_page(browser, url, locator):
    """Тестовая функция для проверки видимости элементов на странице Логина.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    :param locator: путь до элемента
    """
    url = f'{url}index.php?route=account/login'
    page = LoginPage(browser, url)
    page.open_url()
    page.is_element_visible(*locator)


@allure.feature("Страница логина")
@allure.story("Проверка авторизации в ЛК")
@allure.title("Успешная авторизация в ЛК")
@allure.link("#", name="User story")
def test_success_login(browser, url):
    """Тестовая функция для проверки успешного входа пользователья в ЛК.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
    url = f'{url}index.php?route=account/login'
    page = LoginPage(browser, url)
    page.open_url()
    page.login_user(clr=True)
    account_page = AccountPage(browser, browser.current_url)
    account_page.is_title_correct("My Account")


@allure.feature("Страница логина")
@allure.story("Проверка авторизации в ЛК")
@allure.title("Неуспешная авторизация в ЛК - невалидный email")
@pytest.mark.parametrize("email", ["123", ""])
def test_fail_login_invalid_email(browser, url, email):
    """Тестовая функция для проверки неуспешного входа пользователья в ЛК -
    некорректный email.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
    url = f'{url}index.php?route=account/login'
    page = LoginPage(browser, url)
    page.open_url()
    page.login_user(email=email, create=False)
    page.check_fail_login()


@allure.feature("Страница логина")
@allure.story("Проверка авторизации в ЛК")
@allure.title("Неуспешная авторизация в ЛК - невалидный пароль")
@pytest.mark.parametrize("passw", ["oops", ""])
def test_fail_login_invalid_password(browser, url, passw):
    """Тестовая функция для проверки неуспешного входа пользователья в ЛК -
    некорректный пароль.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
    url = f'{url}index.php?route=account/login'
    page = LoginPage(browser, url)
    page.open_url()
    page.login_user(password=passw, clr=True)
    page.check_fail_login()

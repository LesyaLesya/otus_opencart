"""Модуль с тестами для страницы Логина."""


import allure
import pytest

from helpers.urls import URLS
from pages.account_page import AccountPage
from pages.login_page import LoginPage


@allure.feature('Страница логина')
@pytest.mark.login_page
class TestLoginPage:
    """Тесты страницы логина."""

    @allure.story('Элементы страницы')
    @allure.title('Проверка видимости элементов на странице')
    @allure.link('#', name='User story')
    def test_visibility_of_elements_on_login_page(self, browser, url):
        """Тестовая функция для проверки видимости элементов на странице Логина.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = LoginPage(browser, url)
        page.open_url(path=URLS.LOGIN_PAGE)
        page.check_elements_visibility()

    @allure.story('Проверка авторизации в ЛК')
    @allure.title('Успешная авторизация')
    @allure.link('#', name='User story')
    def test_success_login(self, browser, url, db_connection):
        """Тестовая функция для проверки успешного входа пользователья в ЛК.

            :param browser: фикстура для запуска драйвера
            :param url: фикстура с урлом тестируемого ресурса
            :param db_connection: фикстура коннекта к БД
            """
        page = LoginPage(browser, url, db_connection)
        page.open_url(path=URLS.LOGIN_PAGE)
        page.login_user(clr=True)
        account_page = AccountPage(browser, browser.current_url)
        account_page.is_title_correct('My Account')

    @allure.story('Проверка авторизации в ЛК')
    @allure.title('Неуспешная авторизация - невалидный email')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('email', ['123', ''])
    def test_fail_login_invalid_email(self, browser, url, email):
        """Тестовая функция для проверки неуспешного входа пользователья в ЛК -
        некорректный email.

            :param browser: фикстура для запуска драйвера
            :param url: фикстура с урлом тестируемого ресурса
            :param email: email
            """
        page = LoginPage(browser, url)
        page.open_url(path=URLS.LOGIN_PAGE)
        page.login_user(email=email, create=False)
        page.alert.check_danger_alert()

    @allure.story('Проверка авторизации в ЛК')
    @allure.title('Неуспешная авторизация - невалидный пароль')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('passw', ['oops', ''])
    def test_fail_login_invalid_password(self, browser, url, passw, db_connection):
        """Тестовая функция для проверки неуспешного входа пользователья в ЛК -
        некорректный пароль.

            :param browser: фикстура для запуска драйвера
            :param url: фикстура с урлом тестируемого ресурса
            :param db_connection: фикстура коннекта к БД
            :param passw: пароль
            """
        page = LoginPage(browser, url, db_connection)
        page.open_url(path=URLS.LOGIN_PAGE)
        page.login_user(password=passw, clr=True)
        page.alert.check_danger_alert()

"""Модуль с тестами для страницы Регистрации."""


import allure
import pytest

from helpers.db_helper import check_user_in_db, check_user_not_in_db
from helpers.urls import URLS
from pages.account_page import AccountPage
from pages.register_page import RegisterPage


@allure.feature('Страница регистрации')
@pytest.mark.register_page
class TestRegisterPage:
    """Тесты страницы регистрации."""

    @allure.story('Элементы страницы')
    @allure.title('Проверка видимости элементов на странице')
    @allure.link('#', name='User story')
    def test_visibility_of_elements_on_register_page(self, browser, url):
        """Тестовая функция для проверки видимости элементов на странице Регистрации.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = RegisterPage(browser, url)
        page.open_url(path=URLS.REGISTER_PAGE)
        page.check_elements_visibility()

    @allure.story('Проверка регистрации нового пользователя')
    @allure.title('Успешная регистрация')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('firstname, lastname, email, tel, password, confirm, radio_idx',
                             [('Test1', 'Test2', 'test@test12.com', '89991112233', 'test', 'test', 0),
                              ('Пользователь', 'Фамилия', 'a1@test.ru', '11111111', '12345', '12345', 1)])
    def test_success_register_new_user(
            self, browser, url, db_connection, firstname, lastname, email, tel, password, confirm, radio_idx):
        """Тестовая функция для проверки успешной регистрации нового пользователя.

            :param browser: фикстура для запуска драйвера
            :param url: фикстура с урлом тестируемого ресурса
            :param db_connection: фикстура коннекта к БД
            :param firstname: имя юзера
            :param lastname: фамилия юзера
            :param email: email юзера
            :param tel: телефон юзера
            :param password: пароль
            :param confirm: повторно пароль
            :param radio_idx: согласие на рассылку
            """
        page = RegisterPage(browser, url)
        page.open_url(path=URLS.REGISTER_PAGE)
        page.register_user(
            firstname, lastname, email, tel, password, confirm, radio_idx)
        account_page = AccountPage(browser, browser.current_url)
        account_page.is_title_correct('Your Account Has Been Created!')
        check_user_in_db(db_connection, firstname, lastname, email, tel, radio_idx)

    @allure.story('Проверка регистрации нового пользователя')
    @allure.title('Пустые поля')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('firstname, lastname, email, tel, password, confirm, radio_idx',
                             [(None, 'Test2', 'test@test12.com', '89991112233', 'test', 'test', 0),
                              ('Test1', None, 'test@test12.com', '89991112233', 'test', 'test', 0),
                              ('Test1', 'Test2', None, '89991112233', 'test', 'test', 0),
                              ('Test1', 'Test2', 'test@test12.com', None, 'test', 'test', 0),
                              ('Test1', 'Test2', 'test@test12.com', '89991112233', None, 'test', 0),
                              ('Test1', 'Test2', 'test@test12.com', '89991112233', 'test', None, 0)])
    def test_register_new_user_empty_fields(
            self, browser, url, db_connection, firstname, lastname, email, tel, password, confirm, radio_idx):
        """Тестовая функция для проверки регистрации нового пользователя - пустые поля.

            :param browser: фикстура для запуска драйвера
            :param url: фикстура с урлом тестируемого ресурса
            :param db_connection: фикстура коннекта к БД
            :param firstname: имя юзера
            :param lastname: фамилия юзера
            :param email: email юзера
            :param tel: телефон юзера
            :param password: пароль
            :param confirm: повторно пароль
            :param radio_idx: согласие на рассылку
            """
        page = RegisterPage(browser, url)
        page.open_url(path=URLS.REGISTER_PAGE)
        page.register_user(
            firstname, lastname, email, tel, password, confirm, radio_idx)
        page_after_register = RegisterPage(browser, browser.current_url)
        page_after_register.is_title_correct('Register Account')
        if not email:
            check_user_not_in_db(db_connection, firstname=firstname, lastname=lastname, tel=tel)
            page_after_register.check_fail_register_without_email()
        else:
            check_user_not_in_db(db_connection, email)
            if not firstname:
                page_after_register.check_fail_register_without_firstname()
            if not lastname:
                page_after_register.check_fail_register_without_lastname()
            if not tel:
                page_after_register.check_fail_register_without_telephone()
            if not password:
                page_after_register.check_fail_register_without_password()
            if not confirm:
                page_after_register.check_fail_register_without_confirm()

    @allure.story('Проверка регистрации нового пользователя')
    @allure.title('Не принятие пользовательского соглашения')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('firstname, lastname, email, tel, password, confirm, radio_idx, privacy',
                             [('Test1', 'Test2', 'test@test12.com', '89991112233', 'test', 'test', 0, False)])
    def test_register_new_user_without_accept_privacy_policy(
            self, browser, url, db_connection, firstname, lastname, email, tel, password, confirm, radio_idx, privacy):
        """Тестовая функция для проверки регистрации нового пользователя - пустые поля.

            :param browser: фикстура для запуска драйвера
            :param url: фикстура с урлом тестируемого ресурса
            :param db_connection: фикстура коннекта к БД
            :param firstname: имя юзера
            :param lastname: фамилия юзера
            :param email: email юзера
            :param tel: телефон юзера
            :param password: пароль
            :param confirm: повторно пароль
            :param radio_idx: согласие на рассылку
            :param privacy: чек-бокс privacy policy
            """
        page = RegisterPage(browser, url)
        page.open_url(path=URLS.REGISTER_PAGE)
        page.register_user(
            firstname, lastname, email, tel, password, confirm, radio_idx, privacy)
        page_after_register = RegisterPage(browser, browser.current_url)
        page_after_register.is_title_correct('Register Account')
        check_user_not_in_db(db_connection, email)
        page_after_register.check_fail_register_without_accept_privacy_policy()

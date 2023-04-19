"""Модуль с тестами для страницы Аккуанта."""

import allure
import pytest

from helpers.db_helper import check_user_in_db, check_user_not_in_db
from helpers.locators import LoginPageLocators
from helpers.urls import URLS
from pages.account_page import (
    AccountPage, EditAccountPage, LoginPage, LogoutPage, RegisterPage)


@allure.feature('Страница логаута из аккаунта')
@pytest.mark.account_page
@pytest.mark.account_logout_page
class TestAccountLogoutPage:
    """Тесты страницы Логаута из аккаунта."""

    @allure.story('Логаут')
    @allure.title('Логаут из правого блока')
    @allure.link('#', name='User story')
    def test_logout_from_right_block(self, browser, url, fixture_create_delete_user):
        """Тестовая функция для проверки логаута из правого блока.

            :param browser: фикстура для запуска драйвера
            :param url: фикстура с урлом тестируемого ресурса
            :param fixture_create_delete_user: фикстура создания и удаления тестового пользователя
            """
        email, firstname, lastname, telephone = fixture_create_delete_user
        page = LoginPage(browser, url)
        page.open_url(path=URLS.LOGIN_PAGE)
        page.login_user(email)
        account_page = AccountPage(browser, browser.current_url)
        account_page.logout_from_right_block()
        logout_page = LogoutPage(browser, browser.current_url)
        logout_page.is_title_correct('Account Logout')
        logout_page.check_text_after_logout()
        logout_page.check_right_block_after_logout()
        logout_page.click_my_account()
        login_page = LoginPage(browser, browser.current_url)
        login_page.is_element_visible(*LoginPageLocators.NEW_CUSTOMER_FORM)
        login_page.is_element_visible(*LoginPageLocators.OLD_CUSTOMER_FORM)


@allure.feature('Страница логина')
@pytest.mark.account_page
@pytest.mark.account_login_page
class TestAccountLoginPage:
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
    def test_success_login(self, browser, url, fixture_create_delete_user):
        """Тестовая функция для проверки успешного входа пользователья в ЛК.

            :param browser: фикстура для запуска драйвера
            :param url: фикстура с урлом тестируемого ресурса
            :param fixture_create_delete_user: фикстура создания и удаления тестового пользователя
            """
        email, firstname, lastname, telephone = fixture_create_delete_user
        page = LoginPage(browser, url)
        page.open_url(path=URLS.LOGIN_PAGE)
        page.login_user(email)
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
        page.login_user(email)
        page.alert.check_danger_alert()

    @allure.story('Проверка авторизации в ЛК')
    @allure.title('Неуспешная авторизация - невалидный пароль')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('passw', ['oops', ''])
    def test_fail_login_invalid_password(self, browser, do_fake, url, passw, fixture_create_delete_user):
        """Тестовая функция для проверки неуспешного входа пользователья в ЛК -
        некорректный пароль.

            :param browser: фикстура для запуска драйвера
            :param url: фикстура с урлом тестируемого ресурса
            :param passw: пароль
            :param fixture_create_delete_user: фикстура создания и удаления тестового пользователя
            """
        email, firstname, lastname, telephone = fixture_create_delete_user
        page = LoginPage(browser, url)
        page.open_url(path=URLS.LOGIN_PAGE)
        page.login_user(email, passw)
        page.alert.check_danger_alert()


@allure.feature('Страница регистрации')
@pytest.mark.account_page
@pytest.mark.account_register_page
class TestAccountRegisterPage:
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
            self, browser, url, db_connection, delete_user, firstname,
            lastname, email, tel, password, confirm, radio_idx):
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
        check_user_in_db(db_connection, delete_user, firstname, lastname, email, tel, radio_idx)

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
        page_after_register.alert.check_error_text('Warning: You must agree to the Privacy Policy!')


@allure.feature('Страница редактирования аккаунта')
@pytest.mark.account_page
@pytest.mark.account_edit_page
class TestAccountEditPage:
    """Тесты страницы редактирования аккаунта."""

    @allure.story('Редактирование данных аккаунта')
    @allure.title('Проверка изменения имени пользователя')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('new_firstname', ['lala', '123'])
    def test_change_firstname_user(
            self, browser, url, fixture_create_delete_user, new_firstname, db_connection, delete_user):
        """Тестовая функция для проверки изменения имени пользователя на странице редактирования аккаунт.

        :param browser: фикстура для запуска драйвера
        :param db_connection: фикстура коннекта к БД
        :param url: фикстура с урлом тестируемого ресурса
        :param fixture_create_delete_user: фикстура создания и удаления тестового пользователя
        :param new_firstname: имя пользователя
        """
        email, firstname, lastname, telephone = fixture_create_delete_user
        page = LoginPage(browser, url)
        page.open_url(path=URLS.LOGIN_PAGE)
        page.login_user(email)
        account_page = AccountPage(browser, browser.current_url)
        account_page.click_edit_account()
        edit_page = EditAccountPage(browser, browser.current_url)
        edit_page.is_title_correct('My Account Information')
        edit_page.change_firstname(new_firstname)
        edit_page.save_changes()
        account_page_after_save = AccountPage(browser, browser.current_url)
        account_page_after_save.alert.check_success_alert()
        account_page_after_save.click_edit_account()
        edit_page_new = EditAccountPage(browser, browser.current_url)
        edit_page_new.check_firstname(new_firstname)
        edit_page_new.check_lastname(lastname)
        edit_page_new.check_email(email)
        edit_page_new.check_phone(telephone)
        check_user_in_db(db_connection, delete_user, new_firstname, lastname, email, telephone)

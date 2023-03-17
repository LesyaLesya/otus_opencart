"""Модуль с тестами для страницы Аккуанта."""


import allure
import pytest

from helpers.locators import LoginPageLocators
from helpers.urls import URLS
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


@allure.feature('Страница аккаунта')
@pytest.mark.account_page
class TestAccountPage:
    """Тесты страницы аккаунта."""

    @allure.story('Логаут')
    @allure.title('Логаут из правого блока после регистрации')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('firstname, lastname, email, tel, password, confirm, radio_idx',
                             [('Test1', 'Test2', 'test@test12.com', '89991112233', 'test', 'test', 0)])
    def test_logout_from_right_block_after_register_new_user(
            self, browser, url, db_connection, firstname, lastname, email, tel, password, confirm, radio_idx):
        """Тестовая функция для проверки логаута из правого блока после регистрации нового пользователя.

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
        account_page.logout_from_right_block()
        account_page_after_logout = AccountPage(browser, browser.current_url)
        account_page_after_logout.is_title_correct('Account Logout')
        account_page_after_logout.check_text_after_logout()
        account_page_after_logout.check_right_block_after_logout()
        account_page_after_logout.click_my_account_after_logout(db_connection, email, firstname)
        login_page = LoginPage(browser, browser.current_url)
        login_page.is_element_visible(*LoginPageLocators.NEW_CUSTOMER_FORM)
        login_page.is_element_visible(*LoginPageLocators.OLD_CUSTOMER_FORM)

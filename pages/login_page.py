"""Модуль c методами для страницы Логина."""


import allure
from pages.base_page import BasePage
from helpers.locators import LoginPageLocators
from helpers import db_queries


class LoginPage(BasePage):
    """Класс с методами для страницы Логина."""

    @allure.step('Проверить видимость элементов на странице')
    def check_elements_visibility(self):
        """Проверка видимости элементов."""
        lst = [LoginPageLocators.NEW_CUSTOMER_FORM,
               LoginPageLocators.OLD_CUSTOMER_FORM,
               LoginPageLocators.RIGHT_LIST_MENU,
               LoginPageLocators.BUTTON_FOR_NEW_CUSTOMER,
               LoginPageLocators.BUTTON_FOR_OLD_CUSTOMER]
        for i in lst:
            self.is_element_visible(*i)

    @allure.step('Залогиниться с email {email}, паролем {password}')
    def login_user(self, email="otus_test@test.ru", password="test", create=True, clr=False):
        """Процесс логина пользователя в аккаунт.

        :param email: email
        :param password: пароль
        :param create: нужно ли создавать нового пользователя
        :param clr: нужно ли удалять созданного пользователя
        """
        if create:
            db_queries.delete_user(self.db_connection, email)
            email = db_queries.create_test_user(self.db_connection, email)
        self.input_text(*LoginPageLocators.EMAIL_INPUT, email)
        self.input_text(*LoginPageLocators.PASSWORD_INPUT, password)
        self.click_on_element(*LoginPageLocators.LOGIN_BUTTON)
        if clr is True:
            db_queries.delete_user(self.db_connection, email)

    @allure.step('Проверить, что выведен алерт с ошибкой авторизации')
    def check_fail_login(self):
        """Проверка отображения алерта с ошибкой авторизации."""
        self.is_element_visible(*LoginPageLocators.FAIL_LOGIN_ALERT)

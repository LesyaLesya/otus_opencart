"""Модуль c методами для страницы Логина."""


import allure
from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from helpers import test_data


class LoginPage(BasePage):
    """Класс с методами для страницы Логина."""

    def login_user(self, email="otus_test@test.ru", password="test", create=True, clr=False):
        """Процесс логина пользователя в аккаунт."""

        if create:
            test_data.delete_user(self.browser.db, email)
            email = test_data.create_test_user(self.browser.db, email)
        with allure.step(f"Ввести логин {email}"):
            self.input_text(*LoginPageLocators.EMAIL_INPUT, email)
        with allure.step(f"Ввести пароль {password}"):
            self.input_text(*LoginPageLocators.PASSWORD_INPUT, password)
        with allure.step("Кликнуть на кнопку логина"):
            self.click_on_element(*LoginPageLocators.LOGIN_BUTTON)
        if clr is True:
            test_data.delete_user(self.browser.db, email)
        return self

    @allure.step("Проверить, что выведен алерт с ошибкой авторизации")
    def check_fail_login(self):
        """Проверка отображения алерта с ошибкой авторизации."""

        self.is_element_visible(*LoginPageLocators.FAIL_LOGIN_ALERT)
        return self

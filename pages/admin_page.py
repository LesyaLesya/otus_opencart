"""Модуль c методами для Административной страницы."""


import allure

from helpers.locators import AdminPageLocators
from pages.base_page import BasePage


class AdminPage(BasePage):
    """Класс с методами для Административной страницы."""

    @allure.step('Проверить видимость элементов на странице')
    def check_elements_visibility(self):
        """Проверка видимости элементов."""
        lst = [AdminPageLocators.PANEL_HEADING,
               AdminPageLocators.USERNAME_INPUT,
               AdminPageLocators.PASSWORD_INPUT,
               AdminPageLocators.LOGIN_BUTTON,
               AdminPageLocators.HELP_BLOCK]
        for i in lst:
            self.is_element_visible(*i)

    @allure.step('Залогиниться в админку с логином {name} и паролем {passw}')
    def login(self, name, passw):
        """Логин в админку.

        :param name: имя пользователя
        :param passw: пароль пользователя
        """
        self.input_text(*AdminPageLocators.USERNAME_INPUT, name)
        self.input_text(*AdminPageLocators.PASSWORD_INPUT, passw)
        self.click_on_element(*AdminPageLocators.LOGIN_BUTTON)

    @allure.step('Нажать на кнопку разлогина')
    def logout(self):
        """Нахождение кнопки разлогина и нажатие на нее."""
        self.click_on_element(*AdminPageLocators.LOGOUT_BUTTON)

    @allure.step('Проверить, что осуществлен выход из админки')
    def check_successful_logout_text(self):
        """Проверка видимости элемента после разлогина."""
        self.is_element_visible(*AdminPageLocators.NEED_LOGIN_TEXT)

    @allure.step('Перейти к таблице с товарами')
    def get_product_table(self):
        """Переход к таблице с товарами."""
        with allure.step('Кликнуть по Catalog в левом меню'):
            self.click_on_element(*AdminPageLocators.LEFT_MENU_CATALOGUE)
        with allure.step('Кликнуть по Products в левом меню'):
            self.click_on_element(*AdminPageLocators.LEFT_MENU_PRODUCTS)

    @allure.step('Проверить, что таблица отображается')
    def check_products_table(self):
        """Проверка видимости таблицы."""
        self.is_element_visible(*AdminPageLocators.PRODUCTS_TABLE)

    @allure.step('Проверить, что выведен алерт с ошибкой авторизации')
    def check_fail_login_alert(self):
        """Проверка видимости алерта."""
        self.is_element_visible(*AdminPageLocators.FAIL_LOGIN_ALERT)

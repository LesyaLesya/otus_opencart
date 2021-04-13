"""Модуль c методами для Административной страницы."""


import allure
from otus_opencart.pages.base_page import BasePage
from otus_opencart.pages.locators import AdminPageLocators


class AdminPage(BasePage):
    """Класс с методами для Административной страницы."""

    @allure.step("Ввести логин {name}")
    def set_username(self, name):
        """Добавление имени в инпут.

        :param name: имя пользователя
        """

        self.input_text(*AdminPageLocators.USERNAME_INPUT, name)
        return self

    @allure.step("Ввести пароль {passw}")
    def set_password(self, passw):
        """Добавление пароля в инпут.

        :param passw: пароль пользователя
        """

        self.input_text(*AdminPageLocators.PASSWORD_INPUT, passw)
        return self

    @allure.step("Залогиниться")
    def login_button_click(self):
        """Клик на кнопку логина."""

        self.click_on_element(*AdminPageLocators.LOGIN_BUTTON)
        return self

    @allure.step("Нажать на кнопку разлогина")
    def logout(self):
        """Нахождение кнопки разлогина и нажатие на нее."""

        self.click_on_element(*AdminPageLocators.LOGOUT_BUTTON)
        return self

    @allure.step("Проверить, что осуществлен выход из админки")
    def should_be_successful_logout_text(self):
        """Проверка видимости элемента после разлогина."""

        self.is_element_visible(*AdminPageLocators.NEED_LOGIN_TEXT)
        return self

    @allure.step("Перейти к таблице с товарами")
    def get_product_table(self):
        """Переход к таблице с товарами."""

        with allure.step("Кликнуть по Catalog в левом меню"):
            self.click_on_element(*AdminPageLocators.LEFT_MENU_CATALOGUE)
        with allure.step("Кликнуть по Categories в левом меню"):
            self.click_on_element(*AdminPageLocators.LEFT_MENU_CATEGORIES)
        return self

    @allure.step("Проверить, что таблица отображается")
    def should_be_table(self):
        """Проверка видимости таблицы."""

        self.is_element_visible(*AdminPageLocators.CATEGORIES_TABLE)
        return self

"""Модуль c методами для Шапки сайта."""


import allure
from pages.base_page import BasePage
from pages.locators import HeaderPageLocators
from pages.styles import Colors, Cursor


class HeaderPage(BasePage):
    """Класс с методами для Шапки сайта."""

    @allure.step("Ввести в поле поиска значение {txt}")
    def set_search_text(self, txt):
        """Ввод текста в поле поиска.

        :param txt: искомое значение
        """

        self.input_text(*HeaderPageLocators.SEARCH_INPUT, txt)
        return self

    @allure.step("Нажать на кнопку поиска")
    def start_search(self):
        """Нажатие на кнопку запуска поиска."""

        self.click_on_element(*HeaderPageLocators.SEARCH_BUTTON)
        return self

    def go_to_login_page(self):
        """Проверка перехода на страницу Логина."""

        with allure.step("Кликнуть на кнопку MY_ACCOUNT"):
            self.click_on_element(*HeaderPageLocators.MY_ACCOUNT_LINK)
        with allure.step("Кликнуть на кнопку Login"):
            self.click_on_element(*HeaderPageLocators.LOGIN_LINK)
        return self

    def check_logo_css(self):
        """Проверка стилей логотипа без наведения."""

        lst = []
        with allure.step("Получить стили элемента"):
            for prop in ["font-size", "font-weight", "cursor", "color"]:
                lst.append(self.get_css_property(*HeaderPageLocators.LOGO, prop))
        with allure.step("Проверить, что шрифт 33px"):
            assert lst[0] == "33px", f"Размер текста - {lst[0]}"
        with allure.step("Проверить, что жирность 500"):
            assert lst[1] == "500", f"Жирность шрифта - {lst[1]}"
        with allure.step("Проверить, что курсор Pointer"):
            assert lst[2] == Cursor.POINTER, f"Курсор - {lst[2]}"
        with allure.step(f"Проверить, что цвет {Colors.LIGHT_BLUE}"):
            assert lst[3] == Colors.LIGHT_BLUE, f"Цвет текста - {lst[3]}"

    def check_logo_css_hover(self):
        """Проверка стилей логотипа при наведении."""

        self.mouse_move_to_element(*HeaderPageLocators.LOGO)
        lst = []
        with allure.step("Получить стили элемента"):
            for prop in ["font-size", "font-weight", "cursor", "color"]:
                lst.append(self.get_css_property(*HeaderPageLocators.LOGO, prop))
        with allure.step("Проверить, что шрифт 33px"):
            assert lst[0] == "33px", f"Размер текста - {lst[0]}"
        with allure.step("Проверить, что жирность 500"):
            assert lst[1] == "500", f"Жирность шрифта - {lst[1]}"
        with allure.step("Проверить, что курсор Pointer"):
            assert lst[2] == Cursor.POINTER, f"Курсор - {lst[2]}"
        with allure.step(f"Проверить, что цвет {Colors.DARK_BLUE}"):
            assert lst[3] == Colors.DARK_BLUE, f"Цвет текста - {lst[3]}"

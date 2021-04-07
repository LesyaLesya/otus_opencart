"""Модуль c методами для Шапки сайта."""


import allure
from otus_opencart.pages.base_page import BasePage
from otus_opencart.pages.locators import HeaderPageLocators


class HeaderPage(BasePage):
    """Класс с методами для Шапки сайта."""

    @allure.step("Ввести в поле поиска значение {txt}")
    def set_search_text(self, txt):
        """Ввод текста в поле поиска.

        :param txt: искомое значение
        """

        self.input_text(*HeaderPageLocators.SEARCH_INPUT, txt)

    @allure.step("Нажать на кнопку поиска")
    def start_search(self):
        """Нажатие на кнопку запуска поиска."""

        self.click_on_element(*HeaderPageLocators.SEARCH_BUTTON)

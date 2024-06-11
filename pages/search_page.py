"""Модуль c методами для страницы поиска."""


import allure

from utils.allure_helper import attach
from utils.locators import SearchPageLocators
from base.base_page import BasePage
from config.links import Links


class SearchPage(BasePage):
    """Класс с методами для страницы Поиска."""

    PAGE_URL = Links.SEARCH_PAGE

    EMPTY_SEARCH = 'There is no product that matches the search criteria.'

    @allure.step('Проверить видимость элементов на странице')
    def check_elements_visibility(self):
        """Проверка видимости элементов."""
        lst = [SearchPageLocators.SEARCH_INPUT,
               SearchPageLocators.SEARCH_BUTTON,
               SearchPageLocators.SELECT_CATEGORY,
               SearchPageLocators.CHECKBOX_CATEGORY,
               SearchPageLocators.CHECKBOX_DESCRIPTION]
        for i in lst:
            self.is_element_visible(*i)

    @allure.step('Ввести в поиск значение {value}')
    def search_input(self, value):
        """Ввод текста в поле поиска.

        :param value: искомое значение
        """
        self.input_text(*SearchPageLocators.SEARCH_INPUT, value)

    @allure.step('Нажать на кнопку поиска')
    def search_start(self):
        """Нажатие на кнопку поиска."""
        self.click_on_element(*SearchPageLocators.SEARCH_BUTTON)

    @allure.step('Проверить искомое значение {value} в названиях товаров')
    def check_item_from_search_result(self, value):
        """Получение всех товаров из результата поиска и проверка,
        что искомое значение содержится в названии товара.

        :param value: искомое значение
        """
        elements = self._element(*SearchPageLocators.PRODUCT_NAME, all=True)
        names = [i.text for i in elements]
        for i in names:
            with allure.step(f'Проверить, что значение {value} есть в результатах поиска {i.lower()}'):
                attach(self.browser)
                assert value in i.lower(), f'Название товара {i.lower()}'

    @allure.step('Проверить, что поиск выдал 0 результатов.')
    def check_empty_search_result(self):
        """Проверка пустого результата поиска."""
        result = self.get_text_of_element(*SearchPageLocators.EMPTY_RESULT)
        with allure.step(f'Проверить, что текст - {self.EMPTY_SEARCH}'):
            attach(self.browser)
            assert result == self.EMPTY_SEARCH, 'Найдены товары'

    @allure.step('В выпадающем списке выбрать значение {value}')
    def select_category(self, value):
        """Выбрать категорию для поиска.

        :param value: значения в выпадающем списке
        """
        element = self.select_products(*SearchPageLocators.SELECT_CATEGORY)
        element.select_by_visible_text(value)

"""Модуль c методами для страницы поиска."""


import allure
from otus_opencart.pages.base_page import BasePage
from otus_opencart.pages.locators import SearchPageLocators


class SearchPage(BasePage):
    """Класс с методами для страницы Поиска."""

    @allure.step("Ввести в поле поиска значение {txt}")
    def set_search_text(self, txt):
        """Ввод текста в поле поиска.

        :param txt: искомое значение
        """

        self.input_text(*SearchPageLocators.SEARCH_INPUT, txt)

    @allure.step("Нажать на кнопку поиска")
    def start_search(self):
        """Нажатие на кнопку запуска поиска."""

        self.click_on_element(*SearchPageLocators.SEARCH_BUTTON)

    @allure.step("Проверить искомое значение {value} в названиях товаров")
    def get_item_from_search_result(self, value):
        """Получение всех товаров из результата поиска и проверка,
        что искомое значение содержится в названии товара."""

        elements = self._element(*SearchPageLocators.PRODUCT_NAME, all=True)
        names = [i.text for i in elements]
        for i in names:
            assert value in i.lower(), f"Название товара {i.lower()}"

    @allure.step("Проверить, что поиск выдал 0 результатов.")
    def get_empty_search_result(self):
        """Получение пустого результата поиска."""

        result = self.get_text_of_element(*SearchPageLocators.EMPTY_RESULT)
        assert result == "There is no product that matches the search criteria.", \
            "Найдены товары"



"""Модуль c методами для страницы Сравнение товара."""

import allure
from pages.base_page import BasePage
from pages.locators import ComparePageLocators


class ComparisonPage(BasePage):
    """Класс с методами для страницы сравнения товаров."""

    @allure.step("Проверить, что товар в сравнении")
    def check_item_in_comparison(self, name):
        """Проверка видимости товара в сравнении."""

        name_in_comparison = self.get_text_of_element(*ComparePageLocators.ITEM_NAMES)
        assert name == name_in_comparison, \
            f"Название {name}, название в вишлисте {name_in_comparison}"

"""Модуль c методами для страницы Сравнение товара."""

import allure

from helpers import allure_helper
from helpers.locators import ComparePageLocators
from pages.base_page import BasePage


class ComparisonPage(BasePage):
    """Класс с методами для страницы сравнения товаров."""

    @allure.step('Проверить, что товар в сравнении')
    def check_item_in_comparison(self, name):
        """Проверка видимости товара в сравнении.

        :param name: название товара
        """
        elements = self._element(*ComparePageLocators.ITEM_NAMES, all=True)
        product_names = [i.text for i in elements]
        with allure.step(f'Проверить что все товар {name} есть в спсике {product_names}'):
            allure_helper.attach(self.browser)
            assert name in product_names, \
                f'Название {name}, названия в сравнении {product_names}'

    @allure.step('Удалить все товары из сравнения')
    def del_from_compare(self):
        """Удаление всех товаров из сравнения."""
        elements = self._element(*ComparePageLocators.REMOVE_BUTTON, all=True)
        for i in range(len(elements)):
            self.click_on_element(*ComparePageLocators.REMOVE_BUTTON, i)

    @allure.step('Проверить текст на пустой странице Сравнения')
    def check_empty_compare(self):
        """Проверка текста при отсутсвии товаров в сравнении."""
        txt = self.get_text_of_element(*ComparePageLocators.TEXT_FOR_EMTY_COMPARE)
        with allure.step('Проверить, что текст - You have not chosen any products to compare.'):
            allure_helper.attach(self.browser)
            assert txt == 'You have not chosen any products to compare.', f'Текст - {txt}'

    @allure.step('Добавить товар в корзину из сравнения')
    def add_to_cart_from_compare(self, idx):
        """Добавление товара в корзину из сравнения."""
        self.click_on_element(*ComparePageLocators.ADD_TO_CART_BUTTON, idx)

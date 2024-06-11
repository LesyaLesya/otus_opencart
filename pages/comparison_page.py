"""Модуль c методами для страницы Сравнение товара."""

import allure

from utils.allure_helper import attach
from utils.locators import ComparePageLocators
from base.base_page import BasePage


class ComparisonPage(BasePage):
    """Класс с методами для страницы сравнения товаров."""

    EMPTY_COMPARE = 'You have not chosen any products to compare.'

    @allure.step('Проверить, что товар в сравнении')
    def check_item_in_comparison(self, name):
        """Проверка видимости товара в сравнении.

        :param name: название товара
        """
        elements = self._element(*ComparePageLocators.ITEM_NAMES, all=True)
        product_names = [i.text for i in elements]
        with allure.step(f'Проверить что все товар {name} есть в спсике {product_names}'):
            attach(self.browser)
            assert name in product_names, \
                f'Название {name}, названия в сравнении {product_names}'

    @allure.step('Удалить товары из сравнения')
    def delete_from_compare(self, all=True, idx=0):
        """Удаление товаров из сравнения."""
        if all:
            elements = self._element(*ComparePageLocators.REMOVE_BUTTON, all=True)
            while len(elements) != 0:
                self.click_on_element(*ComparePageLocators.REMOVE_BUTTON, idx)
                elements.pop(0)
        else:
            self.click_on_element(*ComparePageLocators.REMOVE_BUTTON, idx)

    @allure.step('Проверить текст на пустой странице Сравнения')
    def check_empty_compare(self):
        """Проверка текста при отсутсвии товаров в сравнении."""
        txt = self.get_text_of_element(*ComparePageLocators.TEXT_FOR_EMTY_COMPARE)
        with allure.step(f'Проверить, что текст - {self.EMPTY_COMPARE}'):
            attach(self.browser)
            assert txt == self.EMPTY_COMPARE, f'Текст - {txt}'

    @allure.step('Добавить товар в корзину из сравнения')
    def add_to_cart_from_compare(self, idx):
        """Добавление товара в корзину из сравнения."""
        self.scroll_down_page()
        self.click_on_element(*ComparePageLocators.ADD_TO_CART_BUTTON, idx)

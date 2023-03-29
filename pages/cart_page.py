"""Модуль c методами для страницы Корзины."""

import allure

from helpers import allure_helper
from helpers.locators import CartPageLocators
from pages.base_page import BasePage


class CartPage(BasePage):
    """Класс с методами для страницы корзины."""

    @allure.step('Проверить, что товар в корзине')
    def check_item_in_cart(self, name):
        """Проверка видимости товара в корзине.

        :param name: название товара
        """
        elements = self._element(*CartPageLocators.ITEM_NAMES, all=True)
        product_names = [i.text for i in elements]
        with allure.step(f'Проверить что все товары {product_names} содержат название {name}'):
            allure_helper.attach(self.browser)
            assert name in product_names, f'Название {name}, названия товаров в корзине {product_names}'

    @allure.step('Проверить, сколько товаров в корзине')
    def check_quantity_of_items_in_cart(self, value):
        """Проверка видимости товара в корзине.

        :param value: количество товаров в корзине
        """
        elements = self._element(*CartPageLocators.ITEM_NAMES, all=True)
        quantity = len(elements)
        with allure.step(f'Проверить, что в корзине {value} товаров'):
            assert quantity == value, f'Товаров в корзине {quantity}, ожидаем {value}'

    @allure.step('Удалить товар из корзины')
    def remove_product_from_cart(self):
        """Проверка удаления товаров из корзины."""
        self.click_on_element(*CartPageLocators.REMOVE_BUTTONS)

    @allure.step('Проверить, что корзина пуста')
    def check_empty_cart(self):
        """Проверка удаления товаров из корзины."""
        text = self.get_text_of_element(*CartPageLocators.TEXT_EMPTY_CART)
        with allure.step(
                'Проверить что текст - Your shopping cart is empty!'):
            allure_helper.attach(self.browser)
            assert text == 'Your shopping cart is empty!', f'Текст - {text}'

    @allure.step('Обновить цену, указав количество {value}')
    def update_price(self, value):
        """Ввод значения в инпут и клик по кнопке обновления цены.

        :param value: количество товара
        """
        self.input_text(*CartPageLocators.QUANTITY_INPUT, value)
        self.click_on_element(*CartPageLocators.QUANTITY_REFRESH_BUTTON)

    @allure.step('Проверить, что цена обновилась')
    def check_updating_price(self, value):
        """Проверка обновленной цены.

        :param value: количество товара
        """
        with allure.step('Получить цену за единицу товара'):
            unit_price = self.get_text_of_element(*CartPageLocators.UNIT_PRICE)
        unit_price_in_float = float(unit_price.replace(',', '').replace('$', ''))
        with allure.step('Получить общую цену за товар'):
            total_price = self.get_text_of_element(*CartPageLocators.TOTAL_PRICE)
        total_price_in_float = float(total_price.replace(',', '').replace('$', ''))
        with allure.step(f'Проверить, что общая цена {total_price_in_float} == {unit_price_in_float} * {value}'):
            allure_helper.attach(self.browser)
            assert total_price_in_float == unit_price_in_float * value, \
                f'Общая цена - {total_price_in_float}, цена за единицу {unit_price_in_float}'

    @allure.step('Нажать на кнопку возврата к покупкам')
    def click_continue_shopping(self):
        """Проверка нажатия на кнопку возврата к покупкам."""
        self.click_on_element(*CartPageLocators.CONTINUE_SHOPPING_BUTTON)

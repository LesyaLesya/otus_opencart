"""Модуль c методами для страницы Корзины."""

import allure
from pages.base_page import BasePage
from pages.locators import CartPageLocators


class CartPage(BasePage):
    """Класс с методами для страницы корзины."""

    @allure.step("Проверить, что товар в корзине")
    def check_item_in_cart(self, name):
        """Проверка видимости товара в корзине."""

        elements = self._element(*CartPageLocators.ITEM_NAMES, all=True)
        product_names = [i.text for i in elements]
        assert name in product_names, f"Название {name}, названия в корзине {product_names}"

    @allure.step("Удалить товар из корзины")
    def remove_product_from_cart(self):
        """Проверка удаления товаров из корзины."""

        self.click_on_element(*CartPageLocators.REMOVE_BUTTONS)
        return self

    @allure.step("Проверить, что корзина пуста")
    def check_empty_cart(self):
        """Проверка удаления товаров из корзины."""

        text = self.get_text_of_element(*CartPageLocators.TEXT_EMPTY_CART)
        assert text == 'Your shopping cart is empty!', f'Текст - {text}'

    @allure.step("Ввести в инпут значение {value}")
    def _set_quantity(self, value):
        """Ввод значения в инпут. Возвращает введенное значение."""

        self.input_text(*CartPageLocators.QUANTITY_INPUT, value)
        return value

    @allure.step("Нажать на кнопку обновления цены")
    def _refresh_price(self):
        """Возвращает клик по кнопке."""

        self.click_on_element(*CartPageLocators.QUANTITY_REFRESH_BUTTON)
        return self

    @allure.step("Нажать на кнопку обновления цены")
    def updating_price(self, val):
        """Возвращает клик по кнопке."""
        value = self._set_quantity(val)
        self._refresh_price()
        unit_price = self.get_text_of_element(*CartPageLocators.UNIT_PRICE)
        unit_price_in_float = float(unit_price.replace(',', '').replace('$', ''))
        total_price = self.get_text_of_element(*CartPageLocators.TOTAL_PRICE)
        total_price_in_float = float(total_price.replace(',', '').replace('$', ''))
        assert total_price_in_float == unit_price_in_float * value, \
            f'Общая цена - {total_price_in_float}, цена за единицу {unit_price_in_float}'

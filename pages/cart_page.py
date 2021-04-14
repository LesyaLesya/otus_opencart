"""Модуль c методами для страницы Корзины."""

import allure
from otus_opencart.pages.base_page import BasePage
from otus_opencart.pages.locators import CartPageLocators


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

        return self.click_on_element(*CartPageLocators.REMOVE_BUTTONS)

    @allure.step("Проверить, что корзина пуста")
    def check_empty_cart(self):
        """Проверка удаления товаров из корзины."""

        text = self.get_text_of_element(*CartPageLocators.TEXT_EMPTY_CART)
        assert text == 'Your shopping cart is empty!', f'Текст - {text}'

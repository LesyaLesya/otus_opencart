"""Модуль c методами для страницы Корзины."""

import allure
from otus_opencart.pages.base_page import BasePage
from otus_opencart.pages.locators import CartPageLocators


class CartPage(BasePage):
    """Класс с методами для страницы корзины."""

    @allure.step("Проверить, что товар в сравнении")
    def check_item_in_cart(self, name):
        """Проверка видимости товара в корзине."""

        name_in_cart = self.get_text_of_element(*CartPageLocators.ITEM_NAMES)
        assert name == name_in_cart, \
            f"Название {name}, название в корзине {name_in_cart}"

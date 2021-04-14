"""Модуль c методами для страницы Аккаунта пользователя."""

import allure
from otus_opencart.pages.base_page import BasePage
from otus_opencart.pages.locators import AccountPageLocators


class AccountPage(BasePage):
    """Класс с методами для страницы Аккаунта пользователя."""

    @allure.step("Открыть виш-лист")
    def open_wishlist(self):
        """Открытие вишлиста."""

        self.click_on_element(*AccountPageLocators.WISH_LIST_LINK)
        return self

    @allure.step("Проверить, что товар в виш-листе")
    def check_item_in_wish_list(self, name):
        """Проверка видимости товара в вишлисте."""

        elements = self._element(*AccountPageLocators.ITEM_NAMES, all=True)
        product_names = [i.text for i in elements]
        assert name in product_names, f"Название {name}, названия в вишлисте {product_names}"

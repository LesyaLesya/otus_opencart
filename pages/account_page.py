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

        name_in_wishlist = self.get_text_of_element(*AccountPageLocators.ITEM_NAME_IN_WISH_LIST)
        assert name == name_in_wishlist, \
            f"Название {name}, название в вишлисте {name_in_wishlist}"

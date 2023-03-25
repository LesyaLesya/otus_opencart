"""Модуль c методами для страницы Аккаунта пользователя."""

import allure

from helpers import allure_helper
from helpers.db_helper import del_user_from_bd
from helpers.locators import AccountPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    """Класс с методами для страницы Аккаунта пользователя."""

    @allure.step('Открыть виш-лист')
    def open_wishlist(self):
        """Открытие вишлиста."""
        self.click_on_element(*AccountPageLocators.WISH_LIST_LINK)

    @allure.step('Проверить, что товар в виш-листе')
    def check_item_in_wish_list(self, name):
        """Проверка видимости товара в вишлисте.

        :param name: название товара
        """
        elements = self._element(*AccountPageLocators.ITEM_NAMES, all=True)
        product_names = [i.text for i in elements]
        with allure.step(f'Проверить что все товары {product_names} содержат название {name}'):
            allure_helper.attach(self.browser)
            assert name in product_names, f'Название {name}, названия продуктов в вишлисте {product_names}'

    @allure.step('Сделать логаут из правого блока')
    def logout_from_right_block(self,):
        """Логаут из правого блока."""
        self.click_on_element(*AccountPageLocators.LOGOUT_RIGHT_BLOCK)

    @allure.step('Проверить текст после логаута')
    def check_text_after_logout(self):
        """Проверка текста после логаута."""
        self.is_element_visible(*AccountPageLocators.TEXT_AFTER_LOGOUT)
        text = self.get_text_of_element(*AccountPageLocators.TEXT_AFTER_LOGOUT)
        with allure.step(
                'Проверить что текст после логаута  - You have been logged off your account. It is now safe to leave the computer.'):
            allure_helper.attach(self.browser)
            assert text == 'You have been logged off your account. It is now safe to leave the computer.', \
                f'Текст после логаута {text}'

    @allure.step('Проверить пункты в правом блоке после логаута')
    def check_right_block_after_logout(self):
        """Проверка пунктов в правом блоке после логаута."""
        self.is_element_visible(*AccountPageLocators.REGISTER_RIGHT_BLOCK)
        self.is_element_visible(*AccountPageLocators.LOGIN_RIGHT_BLOCK)

    @allure.step('Зайти в аккаунт после логаута')
    def click_my_account_after_logout(self, db_connection, email, fistname, del_user=True):
        """Заход в аккаунт после логаута."""
        self.click_on_element(*AccountPageLocators.MY_ACCOUNT_RIGHT_BLOCK)
        if del_user:
            del_user_from_bd(db_connection, email, fistname)

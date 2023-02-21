"""Модуль c методами для страницы Аккаунта пользователя."""

import allure
from pages.base_page import BasePage
from pages.locators import AccountPageLocators
from helpers import test_data


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

    def check_user_in_db(self, firstname, lastname, email, tel, radio_idx):
        self.__get_user_from_db(firstname, lastname, email, tel, radio_idx)
        self.__del_user_from_bd(email, firstname)

    @allure.step("Проверить, что пользователь появилось в БД")
    def __get_user_from_db(self, firstname, lastname, email, tel, radio_idx):
        """ Проверка пользователя в БД. """

        result = test_data.get_new_user(self.browser.db, firstname, email)
        firstname_db = result[0][4]
        lastname_db = result[0][5]
        email_db = result[0][6]
        tel_db = result[0][7]
        newsletter_db = result[0][13]
        active_db = result[0][17]
        with allure.step(f"Проверяем, что запись об юзере создана в БД "):
            assert firstname_db == firstname, f'Имя пользователя в базе {firstname_db}, ОР {firstname}'
            assert lastname_db == lastname, f'Фамилия пользователя в базе {lastname_db}, ОР {lastname}'
            assert email_db == email, f'Email пользователя в базе {email_db}, ОР {email}'
            assert tel_db == tel, f'Телефон пользователя в базе {tel_db}, ОР {tel}'
            assert active_db == 1, f'Активность пользователя в базе {active_db}, ОР 1'
            if radio_idx == 0:
                assert newsletter_db == 1, f'Рассылка пользователя в базе {newsletter_db}, ОР 1'
            else:
                assert newsletter_db == 0, f'Рассылка пользователя в базе {newsletter_db}, ОР 0'

    @allure.step("Удалить пользователя из БД")
    def __del_user_from_bd(self, email, fistname):
        """ Возвращает удаление юзера из БД. """

        return test_data.delete_user(self.browser.db, email, fistname)

"""Модуль c методами для страницы Аккаунта пользователя."""

import allure

from helpers import allure_helper
from helpers.locators import (
     AccountPageLocators, EditAccountPageLocators, LoginPageLocators,
     LogoutPageLocators, RegisterPageLocators, WishlistPageLocators)
from pages.base_page import BasePage


class AccountPage(BasePage):
    """Класс с методами для страницы Аккаунта пользователя."""

    @allure.step('Открыть виш-лист')
    def open_wishlist(self):
        """Открытие вишлиста."""
        self.click_on_element(*AccountPageLocators.WISH_LIST_LINK)

    @allure.step('Сделать логаут из правого блока')
    def logout_from_right_block(self, ):
        """Логаут из правого блока."""
        self.click_on_element(*AccountPageLocators.LOGOUT_RIGHT_BLOCK)

    @allure.step('Зайти в аккаунт')
    def click_my_account(self):
        """Заход в аккаунт."""
        self.click_on_element(*AccountPageLocators.MY_ACCOUNT_RIGHT_BLOCK)

    @allure.step('Перейти на страницу редактирования аккаунта')
    def click_edit_account(self):
        """Заход на страницу редактирования аккаунта."""
        self.click_on_element(*AccountPageLocators.EDIT_ACCOUNT_RIGHT_BLOCK)


class WishlistPage(AccountPage):
    """Класс с методами для страницы Вишлиста Аккаунта пользователя."""

    @allure.step('Проверить количество товаров в вишлисте')
    def check_len_items_in_wish_list(self, n):
        """Проверка количества товаров в вилисте."""
        elements = self._element(*WishlistPageLocators.ITEM_NAMES, all=True)
        with allure.step(f'Проверить, что в вишлисте {n} товаров'):
            allure_helper.attach(self.browser)
            assert len(elements) == n, f'Количество товаров - {len(elements)}'

    @allure.step('Проверить, что товар в виш-листе')
    def check_item_in_wish_list(self, name):
        """Проверка видимости товара в вишлисте.

        :param name: название товара
        """
        elements = self._element(*WishlistPageLocators.ITEM_NAMES, all=True)
        product_names = [i.text for i in elements]
        with allure.step(f'Проверить что все товары {product_names} содержат название {name}'):
            allure_helper.attach(self.browser)
            assert name in product_names, f'Название {name}, названия продуктов в вишлисте {product_names}'

    @allure.step('Проверить, что вишлист пустой')
    def check_empty_wish_list(self):
        """Проверка, что вишлист пустой."""
        self.is_element_visible(*WishlistPageLocators.EMPTY_WISHLIST_TEXT)
        text = self.get_text_of_element(*WishlistPageLocators.EMPTY_WISHLIST_TEXT)
        with allure.step(
                'Проверить что текст - Your wish list is empty.'):
            allure_helper.attach(self.browser)
            assert text == 'Your wish list is empty.', \
                f'Текств в пустом вишлисте - {text}'

    @allure.step('Удалить товары из вишлиста')
    def del_items_from_wish_list(self, all=False, idx=0):
        """Проверка удаления из вишлиста."""
        if all:
            elements = self._element(*WishlistPageLocators.REMOVE_BUTTON, all=True)
            for i in range(len(elements)):
                self.click_on_element(*WishlistPageLocators.REMOVE_BUTTON, i)
        else:
            self.click_on_element(*WishlistPageLocators.REMOVE_BUTTON, idx)


class LogoutPage(AccountPage):
    """Класс с методами для страницы логаута из Аккаунта пользователя."""

    @allure.step('Проверить текст после логаута')
    def check_text_after_logout(self):
        """Проверка текста после логаута."""
        self.is_element_visible(*LogoutPageLocators.TEXT_AFTER_LOGOUT)
        text = self.get_text_of_element(*LogoutPageLocators.TEXT_AFTER_LOGOUT)
        with allure.step(
                'Проверить что текст после логаута  - '
                'You have been logged off your account. It is now safe to leave the computer.'):
            allure_helper.attach(self.browser)
            assert text == 'You have been logged off your account. It is now safe to leave the computer.', \
                f'Текст после логаута {text}'

    @allure.step('Проверить пункты в правом блоке после логаута')
    def check_right_block_after_logout(self):
        """Проверка пунктов в правом блоке после логаута."""
        self.is_element_visible(*LogoutPageLocators.REGISTER_RIGHT_BLOCK)
        self.is_element_visible(*LogoutPageLocators.LOGIN_RIGHT_BLOCK)


class LoginPage(AccountPage):
    """Класс с методами для страницы Логина."""

    @allure.step('Проверить видимость элементов на странице')
    def check_elements_visibility(self):
        """Проверка видимости элементов."""
        lst = [LoginPageLocators.NEW_CUSTOMER_FORM,
               LoginPageLocators.OLD_CUSTOMER_FORM,
               LoginPageLocators.RIGHT_LIST_MENU,
               LoginPageLocators.BUTTON_FOR_NEW_CUSTOMER,
               LoginPageLocators.BUTTON_FOR_OLD_CUSTOMER]
        for i in lst:
            self.is_element_visible(*i)

    @allure.step('Залогиниться с email {email}, паролем {password}')
    def login_user(self, email, password='test'):
        """Процесс логина пользователя в аккаунт.

        :param email: email
        :param password: пароль
        """
        self.input_text(*LoginPageLocators.EMAIL_INPUT, email)
        self.input_text(*LoginPageLocators.PASSWORD_INPUT, password)
        self.click_on_element(*LoginPageLocators.LOGIN_BUTTON)


class RegisterPage(AccountPage):
    """Класс с методами для страницы Регистрации."""

    @allure.step('Проверить видимость элементов на странице')
    def check_elements_visibility(self):
        """Проверка видимости элементов."""
        lst = [RegisterPageLocators.HEADER,
               RegisterPageLocators.TEXT_FOR_LOGIN,
               RegisterPageLocators.FIRST_NAME_FIELD,
               RegisterPageLocators.LAST_NAME_FIELD,
               RegisterPageLocators.EMAIL_FIELD,
               RegisterPageLocators.TEL_FIELD,
               RegisterPageLocators.PASSW_FIELD,
               RegisterPageLocators.CONFIRM_FIELD,
               RegisterPageLocators.PRIVACY_POLICY,
               RegisterPageLocators.CONTINUE_BUTTON,
               RegisterPageLocators.RIGHT_MENU]
        for i in lst:
            self.is_element_visible(*i)

    @allure.step(
        'Зарегистрировать пользователя с данными: email {email}, имя {firstname}, '
        'фамилия {lastname}, телефон {tel}, пароль {password}, повтор пароля {confirm}, '
        'согласие на рассылку {radio_idx}')
    def register_user(
            self, firstname, lastname, email, tel, password, confirm, radio_idx, checkbox=True):
        """Процесс регистрации пользователя.

        :param firstname: имя
        :param lastname: фамилия
        :param email: email
        :param password: пароль
        :param confirm: подтверждение пароля
        :param radio_idx: согласие на рассылку
        :param checkbox: принятие пользовательского соглашения
        """
        if firstname:
            self.input_text(*RegisterPageLocators.FIRST_NAME_FIELD, firstname)
        if lastname:
            self.input_text(*RegisterPageLocators.LAST_NAME_FIELD, lastname)
        if email:
            self.input_text(*RegisterPageLocators.EMAIL_FIELD, email)
        if tel:
            self.input_text(*RegisterPageLocators.TEL_FIELD, tel)
        if password:
            self.input_text(*RegisterPageLocators.PASSW_FIELD, password)
        if confirm:
            self.input_text(*RegisterPageLocators.CONFIRM_FIELD, confirm)
        if radio_idx == 0 or radio_idx == 1:
            self.click_on_element(*RegisterPageLocators.SUBSCRIBE_RADIO, radio_idx)
        if checkbox:
            self.click_on_element(*RegisterPageLocators.AGREE_CHECKBOX)
        self.click_on_element(*RegisterPageLocators.CONTINUE_BUTTON)

    @allure.step('Проверить, что выведена ошибка  - имя обязательно')
    def check_fail_register_without_firstname(self):
        """ Проверка отображения ошибки регистрации без firstname. """
        self.is_element_visible(*RegisterPageLocators.FIRST_NAME_ERROR)
        error_text = self.get_text_of_element(*RegisterPageLocators.FIRST_NAME_ERROR)
        with allure.step('Проверить, что текст ошибки при пустом имени - First Name must be between 1 and 32 characters!'):
            allure_helper.attach(self.browser)
            assert error_text == 'First Name must be between 1 and 32 characters!', \
                f'Текст ошибки {error_text}'

    @allure.step('Проверить, что выведена ошибка  - фамилия обязательна')
    def check_fail_register_without_lastname(self):
        """ Проверка отображения ошибки регистрации без lastname. """
        self.is_element_visible(*RegisterPageLocators.LAST_NAME_ERROR)
        error_text = self.get_text_of_element(*RegisterPageLocators.LAST_NAME_ERROR)
        with allure.step(
                'Проверить, что текст ошибки при пустом имени - Last Name must be between 1 and 32 characters!'):
            allure_helper.attach(self.browser)
            assert error_text == 'Last Name must be between 1 and 32 characters!', \
                f'Текст ошибки {error_text}'

    @allure.step('Проверить, что выведена ошибка  - email обязателен')
    def check_fail_register_without_email(self):
        """ Проверка отображения ошибки регистрации без email. """
        self.is_element_visible(*RegisterPageLocators.EMAIL_ERROR)
        error_text = self.get_text_of_element(*RegisterPageLocators.EMAIL_ERROR)
        with allure.step(
                'Проверить, что текст ошибки при пустом имени - E-Mail Address does not appear to be valid!'):
            allure_helper.attach(self.browser)
            assert error_text == 'E-Mail Address does not appear to be valid!', \
                f'Текст ошибки {error_text}'

    @allure.step('Проверить, что выведена ошибка  - телефон обязателен')
    def check_fail_register_without_telephone(self):
        """ Проверка отображения ошибки регистрации без телефона. """
        self.is_element_visible(*RegisterPageLocators.TEL_ERROR)
        error_text = self.get_text_of_element(*RegisterPageLocators.TEL_ERROR)
        with allure.step(
                'Проверить, что текст ошибки при пустом имени - Telephone must be between 3 and 32 characters!'):
            allure_helper.attach(self.browser)
            assert error_text == 'Telephone must be between 3 and 32 characters!', \
                f'Текст ошибки {error_text}'

    @allure.step('Проверить, что выведена ошибка  - пароль обязателен')
    def check_fail_register_without_password(self):
        """ Проверка отображения ошибки регистрации без пароля. """
        self.is_element_visible(*RegisterPageLocators.PASSWORD_ERROR)
        error_text = self.get_text_of_element(*RegisterPageLocators.PASSWORD_ERROR)
        with allure.step(
                'Проверить, что текст ошибки при пустом имени - Password must be between 4 and 20 characters!'):
            allure_helper.attach(self.browser)
            assert error_text == 'Password must be between 4 and 20 characters!', \
                f'Текст ошибки {error_text}'

    @allure.step('Проверить, что выведена ошибка  - подтверждение пароля обязательно')
    def check_fail_register_without_confirm(self):
        """ Проверка отображения ошибки регистрации без подтверждения пароля. """
        self.is_element_visible(*RegisterPageLocators.CONFIRM_ERROR)
        error_text = self.get_text_of_element(*RegisterPageLocators.CONFIRM_ERROR)
        with allure.step(
                'Проверить, что текст ошибки при пустом имени - Password confirmation does not match password!'):
            allure_helper.attach(self.browser)
            assert error_text == 'Password confirmation does not match password!', \
                f'Текст ошибки {error_text}'


class EditAccountPage(AccountPage):
    """Класс с методами для страницы редактирования аккаунта."""

    @allure.step('Изменить имя на {firstname}')
    def change_firstname(self, firstname):
        """Изменение имени пользователя.

        :param firstname: имя пользователя
        """
        self.input_text(*EditAccountPageLocators.FIRSTNAME_FIELD, firstname)

    @allure.step('Сохранить изменения данных аккаунта')
    def save_changes(self):
        """Сохранение данных аккаунта."""
        self.click_on_element(*EditAccountPageLocators.SUBMIT_BUTTON)

    def check_firstname(self, firstname):
        """Получение имени пользователя из инупта."""
        firstname_in_input = self.getting_attr('value', *EditAccountPageLocators.FIRSTNAME_FIELD)
        with allure.step(f'Проверить, что имя в инпуте {firstname_in_input} == {firstname}'):
            allure_helper.attach(self.browser)
            assert firstname_in_input == firstname, f'Имя в инпуте {firstname_in_input}, ОР {firstname}'

    def check_lastname(self, lastname):
        """Получение фамилии пользователя из инупта."""
        lastname_in_input = self.getting_attr('value', *EditAccountPageLocators.LASTNAME_FIELD)
        with allure.step(f'Проверить, что фамилия в инпуте {lastname_in_input} == {lastname}'):
            allure_helper.attach(self.browser)
            assert lastname_in_input == lastname, f'Фамилия в инпуте {lastname_in_input}, ОР {lastname}'

    def check_email(self, email):
        """Получение email пользователя из инупта."""
        email_in_input = self.getting_attr('value', *EditAccountPageLocators.EMAIL_INPUT)
        with allure.step(f'Проверить, что email в инпуте {email_in_input} == {email}'):
            allure_helper.attach(self.browser)
            assert email_in_input == email, f'email в инпуте {email_in_input}, ОР {email}'

    def check_phone(self, phone):
        """Получение телефона пользователя из инупта."""
        phone_in_input = self.getting_attr('value', *EditAccountPageLocators.TELEPHONE_INPUT)
        with allure.step(f'Проверить, что телефон в инпуте {phone_in_input} == {phone}'):
            allure_helper.attach(self.browser)
            assert phone_in_input == phone, f'Телефон в инпуте {phone_in_input}, ОР {phone}'

    @allure.step('Нажать на кнопку назад')
    def press_back(self):
        """Сохранение данных аккаунта."""
        self.click_on_element(*EditAccountPageLocators.BACK_BUTTON)

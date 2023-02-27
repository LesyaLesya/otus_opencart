"""Модуль c методами для страницы Регистрации."""


import allure
from pages.base_page import BasePage
from pages.locators import RegisterPageLocators
from helpers import test_data


class RegisterPage(BasePage):
    """Класс с методами для страницы Регистрации."""

    def register_user(
            self, fistname, lastname, email, tel, password, confirm, radio_idx, checkbox=True):
        """Процесс регистрации пользователя."""

        if fistname:
            with allure.step(f"Ввести имя {fistname}"):
                self.input_text(*RegisterPageLocators.FIRST_NAME_FIELD, fistname)
        if lastname:
            with allure.step(f"Ввести фамилию {lastname}"):
                self.input_text(*RegisterPageLocators.LAST_NAME_FIELD, lastname)
        if email:
            with allure.step(f"Ввести email {email}"):
                self.input_text(*RegisterPageLocators.EMAIL_FIELD, email)
        if tel:
            with allure.step(f"Ввести телефон {tel}"):
                self.input_text(*RegisterPageLocators.TEL_FIELD, tel)
        if password:
            with allure.step(f"Ввести пароль {password}"):
                self.input_text(*RegisterPageLocators.PASSW_FIELD, password)
        if confirm:
            with allure.step(f"Ввести подтверждение пароля {confirm}"):
                self.input_text(*RegisterPageLocators.CONFIRM_FIELD, confirm)
        if radio_idx == 0 or radio_idx == 1:
            with allure.step(f"Ввести подписку на рассылку {radio_idx}"):
                self.click_on_element(*RegisterPageLocators.SUBSCRIBE_RADIO, radio_idx)
        if checkbox:
            with allure.step(f"Согласие с политикой {checkbox}"):
                self.click_on_element(*RegisterPageLocators.AGREE_CHECKBOX)
        return self.click_on_element(*RegisterPageLocators.CONTINUE_BUTTON)

    @allure.step("Проверить, что выведена ошибка  - имя обязательно")
    def check_fail_register_without_firstname(self):
        """ Проверка отображения ошибки регистрации без firstname. """

        assert self.is_element_visible(*RegisterPageLocators.FIRST_NAME_ERROR)
        error_text = self.get_text_of_element(*RegisterPageLocators.FIRST_NAME_ERROR)
        assert error_text == 'First Name must be between 1 and 32 characters!', \
            f'Текст ошибки {error_text}'

    @allure.step("Проверить, что пользователь не появился в БД")
    def check_user_not_in_db(self, email=None, firstname=None, lastname=None, tel=None):
        """ Проверка пользователя в БД. """

        result = test_data.get_new_user(self.browser.db, email, firstname, lastname, tel)
        assert len(result) == 0, f'Найдено записей {len(result)}'

    @allure.step("Проверить, что выведена ошибка  - фамилия обязательна")
    def check_fail_register_without_lastname(self):
        """ Проверка отображения ошибки регистрации без lastname. """

        assert self.is_element_visible(*RegisterPageLocators.LAST_NAME_ERROR)
        error_text = self.get_text_of_element(*RegisterPageLocators.LAST_NAME_ERROR)
        assert error_text == 'Last Name must be between 1 and 32 characters!', \
            f'Текст ошибки {error_text}'

    @allure.step("Проверить, что выведена ошибка  - email обязателен")
    def check_fail_register_without_email(self):
        """ Проверка отображения ошибки регистрации без email. """

        assert self.is_element_visible(*RegisterPageLocators.EMAIL_ERROR)
        error_text = self.get_text_of_element(*RegisterPageLocators.EMAIL_ERROR)
        assert error_text == 'E-Mail Address does not appear to be valid!', \
            f'Текст ошибки {error_text}'

    @allure.step("Проверить, что выведена ошибка  - телефон обязателен")
    def check_fail_register_without_telephone(self):
        """ Проверка отображения ошибки регистрации без телефона. """

        assert self.is_element_visible(*RegisterPageLocators.TEL_ERROR)
        error_text = self.get_text_of_element(*RegisterPageLocators.TEL_ERROR)
        assert error_text == 'Telephone must be between 3 and 32 characters!', \
            f'Текст ошибки {error_text}'

    @allure.step("Проверить, что выведена ошибка  - пароль обязателен")
    def check_fail_register_without_password(self):
        """ Проверка отображения ошибки регистрации без пароля. """

        assert self.is_element_visible(*RegisterPageLocators.PASSWORD_ERROR)
        error_text = self.get_text_of_element(*RegisterPageLocators.PASSWORD_ERROR)
        assert error_text == 'Password must be between 4 and 20 characters!', \
            f'Текст ошибки {error_text}'

    @allure.step("Проверить, что выведена ошибка  - подтверждение пароля обязательно")
    def check_fail_register_without_confirm(self):
        """ Проверка отображения ошибки регистрации без подтверждения пароля. """

        assert self.is_element_visible(*RegisterPageLocators.CONFIRM_ERROR)
        error_text = self.get_text_of_element(*RegisterPageLocators.CONFIRM_ERROR)
        assert error_text == 'Password confirmation does not match password!', \
            f'Текст ошибки {error_text}'

    @allure.step("Проверить, что выведена ошибка  - принятие пользовательского соглашения обязательно")
    def check_fail_register_without_accept_privacy_policy(self):
        """ Проверка отображения ошибки регистрации без принятия пользовательского соглашения. """

        assert self.is_element_visible(*RegisterPageLocators.PRIVACY_POLICY_ALERT)
        error_text = self.get_text_of_element(*RegisterPageLocators.PRIVACY_POLICY_ALERT)
        assert error_text == 'Warning: You must agree to the Privacy Policy!', \
            f'Текст ошибки {error_text}'

"""Модуль c методами для страницы Регистрации."""


import allure
from pages.base_page import BasePage
from pages.locators import RegisterPageLocators


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

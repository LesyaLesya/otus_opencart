"""Модуль с тестами для страницы Регистрации."""


import pytest
import allure
from pages.locators import RegisterPageLocators
from pages.register_page import RegisterPage
from pages.account_page import AccountPage


@allure.feature("Страница регистрации")
@allure.story("Проверка присутствия элементов на странице Регистрации")
@allure.title("Поиск элемента {locator}")
@allure.link("#", name="User story")
@pytest.mark.parametrize("locator",
                         [RegisterPageLocators.HEADER,
                          RegisterPageLocators.TEXT_FOR_LOGIN,
                          RegisterPageLocators.FIRST_NAME_FIELD,
                          RegisterPageLocators.LAST_NAME_FIELD,
                          RegisterPageLocators.EMAIL_FIELD,
                          RegisterPageLocators.TEL_FIELD,
                          RegisterPageLocators.PASSW_FIELD,
                          RegisterPageLocators.CONFIRM_FIELD,
                          RegisterPageLocators.SUBSCRIBE_RADIO,
                          RegisterPageLocators.PRIVACY_POLICY,
                          RegisterPageLocators.CONTINUE_BUTTON,
                          RegisterPageLocators.RIGHT_MENU],
                         ids=["HEADER", "TEXT_FOR_LOGIN",
                              "FIRST_NAME_FIELD", "LAST_NAME_FIELD",
                              "EMAIL_FIELD", "TEL_FIELD", "PASSW_FIELD",
                              "CONFIRM_FIELD", "SUBSCRIBE_RADIO", "PRIVACY_POLICY",
                              "CONTINUE_BUTTON", "RIGHT_MENU"])
def test_presence_of_elements_on_register_page(browser, url, locator):
    """Тестовая функция для проверки видимости элементов на странице Регистрации.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    :param locator: путь до элемента
    """
    url = f'{url}index.php?route=account/register'
    page = RegisterPage(browser, url)
    page.open_url()
    page.is_element_visible(*locator)


@allure.feature("Страница регистрации")
@allure.story("Проверка регистрации нового пользователя")
@allure.title("Успешная регистрация")
@allure.link("#", name="User story")
@pytest.mark.parametrize('firstname, lastname, email, tel, password, confirm, radio_idx',
                         [('Test1', 'Test2', 'test@test12.com', '89991112233', 'test', 'test', 0),
                          ('Пользователь', 'Фамилия', 'a1@test.ru', '11111111', '12345', '12345', 1)])
def test_success_register_new_user(
        browser, url, firstname, lastname, email, tel, password, confirm, radio_idx):
    """Тестовая функция для проверки успешной регистрации нового пользователя.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        :param firstname: имя юзера
        :param lastname: фамилия юзера
        :param email: email юзера
        :param tel: телефон юзера
        :param password: пароль
        :param confirm: повторно пароль
        :param radio_idx: согласие на рассылку
        """
    url = f'{url}index.php?route=account/register'
    page = RegisterPage(browser, url)
    page.open_url()
    page.register_user(
        firstname, lastname, email, tel, password, confirm, radio_idx)
    account_page = AccountPage(browser, browser.current_url)
    account_page.is_title_correct("Your Account Has Been Created!")
    account_page.check_user_in_db(firstname, lastname, email, tel, radio_idx)

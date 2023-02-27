"""Модуль с тестами для страницы Регистрации."""


import pytest
import allure
from pages.locators import LoginPageLocators, RegisterPageLocators
from pages.login_page import LoginPage
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


@allure.feature("Страница регистрации")
@allure.story("Проверка регистрации нового пользователя")
@allure.title("Пустые поля")
@allure.link("#", name="User story")
@pytest.mark.parametrize('firstname, lastname, email, tel, password, confirm, radio_idx',
                         [(None, 'Test2', 'test@test12.com', '89991112233', 'test', 'test', 0),
                          ('Test1', None, 'test@test12.com', '89991112233', 'test', 'test', 0),
                          ('Test1', 'Test2', None, '89991112233', 'test', 'test', 0),
                          ('Test1', 'Test2', 'test@test12.com', None, 'test', 'test', 0),
                          ('Test1', 'Test2', 'test@test12.com', '89991112233', None, 'test', 0),
                          ('Test1', 'Test2', 'test@test12.com', '89991112233', 'test', None, 0)])
def test_register_new_user_empty_fields(
        browser, url, firstname, lastname, email, tel, password, confirm, radio_idx):
    """Тестовая функция для проверки регистрации нового пользователя - пустые поля.

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
    page_after_register = RegisterPage(browser, browser.current_url)
    page_after_register.is_title_correct("Register Account")
    if not email:
        page_after_register.check_fail_register_without_email()
        page_after_register.check_user_not_in_db(firstname=firstname, lastname=lastname, tel=tel)
    else:
        page_after_register.check_user_not_in_db(email)
        if not firstname:
            page_after_register.check_fail_register_without_firstname()
        if not lastname:
            page_after_register.check_fail_register_without_lastname()
        if not tel:
            page_after_register.check_fail_register_without_telephone()
        if not password:
            page_after_register.check_fail_register_without_password()
        if not confirm:
            page_after_register.check_fail_register_without_confirm()


@allure.feature("Страница регистрации")
@allure.story("Проверка регистрации нового пользователя")
@allure.title("Не принятие пользовательского соглашения")
@allure.link("#", name="User story")
@pytest.mark.parametrize('firstname, lastname, email, tel, password, confirm, radio_idx, privacy',
                         [('Test1', 'Test2', 'test@test12.com', '89991112233', 'test', 'test', 0, False)])
def test_register_new_user_without_accept_privacy_policy(
        browser, url, firstname, lastname, email, tel, password, confirm, radio_idx, privacy):
    """Тестовая функция для проверки регистрации нового пользователя - пустые поля.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        :param firstname: имя юзера
        :param lastname: фамилия юзера
        :param email: email юзера
        :param tel: телефон юзера
        :param password: пароль
        :param confirm: повторно пароль
        :param radio_idx: согласие на рассылку
        :param privacy: чек-бокс privacy policy
        """
    url = f'{url}index.php?route=account/register'
    page = RegisterPage(browser, url)
    page.open_url()
    page.register_user(
        firstname, lastname, email, tel, password, confirm, radio_idx, privacy)
    page_after_register = RegisterPage(browser, browser.current_url)
    page_after_register.is_title_correct("Register Account")
    page_after_register.check_user_not_in_db(email)
    page_after_register.check_fail_register_without_accept_privacy_policy()


@allure.feature("Страница регистрации")
@allure.story("Проверка регистрации нового пользователя")
@allure.title("Логаут из правого блока после регистрации")
@allure.link("#", name="User story")
@pytest.mark.parametrize('firstname, lastname, email, tel, password, confirm, radio_idx',
                         [('Test1', 'Test2', 'test@test12.com', '89991112233', 'test', 'test', 0)])
def test_logout_from_right_block_after_register_new_user(
        browser, url, firstname, lastname, email, tel, password, confirm, radio_idx):
    """Тестовая функция для проверки логаута из правого блока после регистрации нового пользователя.

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
    account_page.logout_from_right_block()
    account_page_after_logout = AccountPage(browser, browser.current_url)
    account_page_after_logout.is_title_correct('Account Logout')
    account_page_after_logout.check_text_after_logout()
    account_page_after_logout.check_right_block_after_logout()
    account_page_after_logout.click_my_account_after_logout(email, firstname)
    login_page = LoginPage(browser, browser.current_url)
    login_page.is_element_visible(*LoginPageLocators.NEW_CUSTOMER_FORM)
    login_page.is_element_visible(*LoginPageLocators.OLD_CUSTOMER_FORM)

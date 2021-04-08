"""Модуль с тестами для страницы Логина."""


import pytest
import allure
from otus_opencart.pages.locators import LoginPageLocators
from otus_opencart.pages.base_page import BasePage


@allure.feature("Страница логина")
@allure.story("Проверка присутствия элементов на странице Логина")
@allure.title("Поиск элемента {locator}")
@allure.link("#", name="User story")
@pytest.mark.parametrize("locator",
                         [LoginPageLocators.NEW_CUSTOMER_FORM,
                          LoginPageLocators.OLD_CUSTOMER_FORM,
                          LoginPageLocators.RIGHT_LIST_MENU,
                          LoginPageLocators.BUTTON_FOR_NEW_CUSTOMER,
                          LoginPageLocators.BUTTON_FOR_OLD_CUSTOMER],
                         ids=["NEW_CUSTOMER_FORM", "OLD_CUSTOMER_FORM",
                              "RIGHT_LIST_MENU", "BUTTON_FOR_NEW_CUSTOMER",
                              "BUTTON_FOR_OLD_CUSTOMER"])
def test_presence_of_elements_on_login_page(browser, url, locator):
    """Тестовая функция для проверки видимости элементов на странице Логина.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    :param locator: путь до элемента
    """
    url = f'{url}index.php?route=account/login'
    page = BasePage(browser, url)
    page.open_url()
    page.is_element_visible(*locator)

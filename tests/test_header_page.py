"""Модуль с тестами для Шапки сайта."""

import pytest
import allure
from pages.header_page import HeaderPage
from pages.search_page import SearchPage
from pages.login_page import LoginPage
from pages.locators import HeaderPageLocators


@allure.feature("Шапка сайта")
@allure.story("Проверка присутствия элементов в Шапке сайта")
@allure.title("Поиск элемента {locator}")
@allure.link("#", name="User story")
@pytest.mark.parametrize("locator",
                         [HeaderPageLocators.LOGO,
                          HeaderPageLocators.MENU,
                          HeaderPageLocators.CART_BUTTON,
                          HeaderPageLocators.TOP_LINKS,
                          HeaderPageLocators.SEARCH_FIELD],
                         ids=["LOGO", "MENU", "CART_BUTTON", "TOP_LINKS",
                              "SEARCH_FIELD"])
def test_presence_of_elements_on_header_page(browser, url, locator):
    """Тестовая функция для проверки видимости элементов в шапке сайта.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    :param locator: путь до элемента
    """
    page = HeaderPage(browser, url)
    page.open_url()
    page.is_element_visible(*locator)


@allure.feature("Шапка сайта")
@allure.story("Переход на другие страницы")
@allure.title("Переход на страницу Логина")
@allure.link("#", name="User story")
def test_go_to_login_page(browser, url):
    """Тестовая функция для проверки перехода на другие
    страницы из шапки сайта.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    """
    page = HeaderPage(browser, url)
    page.open_url()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.is_title_correct("Account Login")


@allure.feature("Шапка сайта")
@allure.story("Поиск по сайту")
@allure.title("Проверка открытия страницы с результатом поиска")
@allure.link("#", name="User story")
@pytest.mark.parametrize("value", ["phone", "laptop", "HP"], ids=["phone", "laptop", "HP"])
def test_search_result_title(browser, url, value):
    """Тестовая функция для проверки тайтла страницы с результатами поиска.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    :param value: значение, вводимое в строку поиска
    """
    page = HeaderPage(browser, url)
    page.open_url()
    page.set_search_text(value)
    page.start_search()
    search_page = SearchPage(browser, browser.current_url)
    search_page.is_title_correct(f"Search - {value}")


@allure.feature("Шапка сайта")
@allure.story("Проверка стилей")
@allure.title("Проверка стилей логотипа")
@allure.link("#", name="User story")
def test_logo_styles(browser, url):
    """Тестовая функция для стилей логотипа.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    """
    page = HeaderPage(browser, url)
    page.open_url()
    page.check_logo_css()
    page.check_logo_css_hover()

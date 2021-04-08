"""Модуль с тестами для Шапки сайта."""


import pytest
import allure
from otus_opencart.pages.header_page import HeaderPage
from otus_opencart.pages.locators import HeaderPageLocators


@allure.feature("Шапка сайта")
@allure.story("Проверка присутствия элементов в Шапке сайта")
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
def test_search_result_title(browser, url):
    """Тестовая функция для проверки перехода на другие
    страницы из шапки сайта.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    """
    page = HeaderPage(browser, url)
    page.open_url()
    page.go_to_login_page()


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
    page.is_title_correct(f"Search - {value}")


"""Модуль с тестами для страницы Поиска."""

import pytest
import allure
from otus_opencart.pages.search_page import SearchPage
from otus_opencart.pages.locators import SearchPageLocators


@allure.feature("Страница Поиска")
@allure.story("Проверка присутствия элементов на странице Поиска")
@allure.title("Поиск элемента {locator}")
@allure.link("#", name="User story")
@pytest.mark.parametrize("locator",
                         [SearchPageLocators.SEARCH_INPUT,
                          SearchPageLocators.SEARCH_BUTTON,
                          SearchPageLocators.SELECT_CATEGORY,
                          SearchPageLocators.CHECKBOX_CATEGORY,
                          SearchPageLocators.CHECKBOX_DESCRIPTION],
                         ids=["SEARCH_INPUT", "SEARCH_BUTTON", "SELECT_CATEGORY",
                              "CHECKBOX_CATEGORY", "CHECKBOX_DESCRIPTION"])
def test_presence_of_elements_on_search_page(browser, url, locator):
    """Тестовая функция для проверки видимости элементов на странице Поиска.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    :param locator: путь до элемента
    """
    url = f'{url}index.php?route=product/search'
    page = SearchPage(browser, url)
    page.open_url()
    page.is_element_visible(*locator)

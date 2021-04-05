"""Модуль с тестами для Шапки сайта."""


import pytest
import allure
from otus_opencart.pages.header_page import HeaderPage


@allure.feature("Шапка сайта")
@allure.story("Поиск по сайту")
@allure.title("Проверка открытия страницы с результатом поиска")
@allure.link("#", name="User story")
@allure.description("Проверка тайтла страницы с результатами поиска")
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

#тесты с позитивным результатом
#негативным результатом

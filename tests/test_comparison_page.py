"""Модуль с тестами для страницы Сравнения товаров."""


import pytest
import allure
from pages.catalogue_page import CataloguePage
from pages.comparison_page import ComparisonPage


@allure.feature("Страница Сравнения")
@allure.story("Удаление товара из Сравнения")
@allure.title("Удаление товара из Сравнения")
@allure.link("#", name="User story")
@pytest.mark.parametrize("idx", [2])
def test_remove_from_compare(browser, url, idx):
    """Тестовая функция для проверки удаления товара из сравнения.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    :param idx: порядковый индекс элемента
    """
    catalogue_url = f'{url}index.php?route=product/category&path=18'
    catalogue_page = CataloguePage(browser, catalogue_url)
    catalogue_page.open_url()
    catalogue_page.add_to_compare(idx)
    catalogue_page.go_to_compare_page()
    compare_page = ComparisonPage(browser, browser.current_url)
    compare_page.del_from_compare()
    compare_page.should_be_empty_compare()

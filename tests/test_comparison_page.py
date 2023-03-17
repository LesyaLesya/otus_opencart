"""Модуль с тестами для страницы Сравнения товаров."""


import allure
import pytest

from helpers.urls import URLS
from pages.catalogue_page import CataloguePage
from pages.comparison_page import ComparisonPage


@allure.feature('Страница Сравнения')
@pytest.mark.comparison_page
class TestComparisonPage:
    """Тесты страницы Сравнения."""

    @allure.story('Товары в сравнении')
    @allure.title('Удаление товара из Сравнения')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('idx', [2])
    def test_remove_from_compare(self, browser, url, idx):
        """Тестовая функция для проверки удаления товара из сравнения.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        :param idx: порядковый индекс элемента
        """
        catalogue_page = CataloguePage(browser, url)
        catalogue_page.open_url(path=URLS.CATALOGUE_PAGE)
        catalogue_page.add_to_compare(idx)
        catalogue_page.go_to_compare_page()
        compare_page = ComparisonPage(browser, browser.current_url)
        compare_page.del_from_compare()
        compare_page.check_success_alert()
        compare_page.check_empty_compare()

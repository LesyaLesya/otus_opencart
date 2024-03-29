"""Модуль с тестами для страницы Сравнения товаров."""


import allure
import pytest

from helpers.urls import URLS
from pages.cart_page import CartPage
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
        compare_page.alert.check_success_alert()
        compare_page.check_empty_compare()

    @allure.story('Товары в сравнении')
    @allure.title('Добавление в корзину товара из Сравнения')
    @allure.link('#', name='User story')
    def test_add_to_cart_from_compare(self, browser, url):
        """Тестовая функция для проверки добавления в корзину товара из сравнения.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        catalogue_page = CataloguePage(browser, url)
        catalogue_page.open_url(path=URLS.CATALOGUE_PAGE)
        catalogue_page.add_to_compare(1)
        item_name = catalogue_page.add_to_compare(2)
        catalogue_page.go_to_compare_page()
        compare_page = ComparisonPage(browser, browser.current_url)
        compare_page.add_to_cart_from_compare(1)
        compare_page.alert.check_success_alert()
        compare_page.alert.click_link_from_alert()
        cart_page = CartPage(browser, browser.current_url)
        cart_page.check_item_in_cart(item_name, 1)

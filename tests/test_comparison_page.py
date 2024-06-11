"""Модуль с тестами для страницы Сравнения товаров."""


import allure
import pytest

from base.base_test import BaseTest


@allure.feature('Страница Сравнения')
@pytest.mark.comparison_page
class TestComparisonPage(BaseTest):
    """Тесты страницы Сравнения."""

    @allure.story('Товары в сравнении')
    @allure.title('Удаление товара из Сравнения')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('idx', [2])
    def test_remove_from_compare(self, idx):
        """Тестовая функция для проверки удаления товара из сравнения.

        :param idx: порядковый индекс элемента
        """
        self.catalogue_page.open_url()
        self.catalogue_page.add_to_compare(idx)
        self.catalogue_page.go_to_compare_page()
        self.comparison_page.delete_from_compare()
        self.alert.check_success_alert()
        self.comparison_page.check_empty_compare()

    @allure.story('Товары в сравнении')
    @allure.title('Добавление в корзину товара из Сравнения')
    @allure.link('#', name='User story')
    def test_add_to_cart_from_compare(self):
        """Тестовая функция для проверки добавления в корзину товара из сравнения.

        """
        self.catalogue_page.open_url()
        self.catalogue_page.add_to_compare(1)
        item_name = self.catalogue_page.add_to_compare(2)
        self.catalogue_page.go_to_compare_page()
        self.comparison_page.add_to_cart_from_compare(1)
        self.alert.check_success_alert()
        self.alert.click_link_from_alert()
        self.cart_page.check_item_in_cart(item_name, 1)

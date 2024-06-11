"""Модуль с тестами для страницы Корзины."""

import allure
import pytest

from base.base_test import BaseTest


@allure.feature('Страница Корзины')
@pytest.mark.cart_page
class TestCartPage(BaseTest):
    """Тесты Страницы Корзины."""

    @allure.story('Удаление товара из корзины')
    @allure.title('Удаление всех товаров из корзины')
    @allure.link('#', name='User story')
    def test_remove_all_products_from_cart(self):
        """Тестовая функция для проверки удаления всех товаров
        из корзины.

        """
        self.product_page.open_url()
        self.product_page.add_to_cart()
        self.alert.click_link_from_alert()
        self.cart_page.remove_product_from_cart(all=True)
        self.cart_page.check_empty_cart()

    @allure.story('Удаление товара из корзины')
    @allure.title('Удаление части товаров из корзины')
    @allure.link('#', name='User story')
    def test_remove_part_products_from_cart(self):
        """Тестовая функция для проверки удаления части товаров
        из корзины.

        """
        self.catalogue_page.open_url()
        name = self.catalogue_page.add_to_cart(1)
        self.catalogue_page.add_to_cart(2)
        self.header.go_to_cart_page()
        self.cart_page.check_cart_page()
        self.cart_page.remove_product_from_cart(idx=1)
        self.cart_page.check_item_in_cart(name, 1)

    @allure.story('Изменение количества товара в корзине')
    @allure.title('Обновление цены за товар при изменении количества')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('value', [2, 3])
    def test_update_quantity_in_cart(self, value):
        """Тестовая функция для проверки обновления цены при
        изменении количества товара.

        """
        self.product_page.open_url()
        self.product_page.add_to_cart()
        self.alert.click_link_from_alert()
        self.cart_page.update_price(value)
        self.cart_page.check_updating_price(value)

    @allure.story('Возврат к покупкам из корзины')
    @allure.title('Нажатие на кнопку Continue Shopping')
    @allure.link('#', name='User story')
    def test_continue_shopping(self):
        """Тестовая функция для проверки возврата к покупкам при нажатии на кнопку Continue Shopping.

        """
        self.product_page.open_url()
        self.product_page.add_to_cart()
        self.alert.click_link_from_alert()
        self.cart_page.click_continue_shopping()
        self.main_page.is_title_correct(self.main_page.TITLE)

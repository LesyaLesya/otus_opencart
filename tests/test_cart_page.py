"""Модуль с тестами для страницы Корзины."""

import allure
import pytest

from helpers.urls import URLS
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


@allure.feature('Страница Корзины')
@pytest.mark.cart_page
class TestCartPage:
    """Тесты Страницы Корзины."""

    @allure.story('Удаление товара из корзины')
    @allure.title('Удаление всех товаров из корзины')
    @allure.link('#', name='User story')
    def test_remove_all_products_from_cart(self, browser, url):
        """Тестовая функция для проверки удаления всех товаров
        из корзины.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        product_page = ProductPage(browser, url)
        product_page.open_url(path=URLS.PRODUCT_PAGE)
        product_page.add_to_cart()
        product_page.alert.click_link_from_alert()
        cart_page = CartPage(browser, browser.current_url)
        cart_page.remove_product_from_cart()
        cart_page.check_empty_cart()

    @allure.story('Изменение количества товара в корзине')
    @allure.title('Обновление цены за товар при изменении количества')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('value', [2, 3])
    def test_update_quantity_in_cart(self, browser, url, value):
        """Тестовая функция для проверки обновления цены при
        изменении количества товара.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        product_page = ProductPage(browser, url)
        product_page.open_url(path=URLS.PRODUCT_PAGE)
        product_page.add_to_cart()
        product_page.alert.click_link_from_alert()
        cart_page = CartPage(browser, browser.current_url)
        cart_page.update_price(value)
        cart_page.check_updating_price(value)

    @allure.story('Возврат к покупкам из корзины')
    @allure.title('Нажатие на кнопку Continue Shopping')
    @allure.link('#', name='User story')
    def test_continue_shopping(self, browser, url):
        """Тестовая функция для проверки возврата к покупкам при нажатии на кнопку Continue Shopping.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        product_page = ProductPage(browser, url)
        product_page.open_url(path=URLS.PRODUCT_PAGE)
        product_page.add_to_cart()
        product_page.alert.click_link_from_alert()
        cart_page = CartPage(browser, browser.current_url)
        cart_page.click_continue_shopping()
        main_page = MainPage(browser, browser.current_url)
        main_page.is_title_correct('Your Store')

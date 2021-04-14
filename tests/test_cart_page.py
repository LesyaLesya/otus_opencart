"""Модуль с тестами для страницы Корзины."""

import pytest
import allure
from otus_opencart.pages.product_page import ProductPage
from otus_opencart.pages.cart_page import CartPage


@allure.feature("Страница Корзины")
@allure.story("Удаление товара из корзины")
@allure.title("Удаление всех товаров из корзины")
@allure.link("#", name="User story")
def test_remove_all_products_from_cart(browser, url):
    """Тестовая функция для проверки удаления всех товаров
    из корзины.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    """
    url = f'{url}index.php?route=product/product&path=18&product_id=47'
    product_page = ProductPage(browser, url)
    product_page.open_url()
    product_page.add_to_cart()
    product_page.click_cart_from_alert()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.remove_product_from_cart()
    cart_page.check_empty_cart()

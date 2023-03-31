"""Модуль с тестами для Подвала сайта."""

import allure
import pytest

from helpers.urls import URLS
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.search_page import SearchPage


@pytest.fixture(scope='module')
def return_lst():
    lst = ['About Us', 'Delivery Information', 'Privacy Policy',
           'Terms & Conditions', 'Contact Us', 'Returns',
           'Site Map', 'Brands', 'Gift Certificates', 'Affiliate',
           'Specials', 'My Account', 'Order History', 'Wish List',
           'Newsletter']
    return lst


@allure.feature('Подвал сайта')
@pytest.mark.footer_page
class TestFooterPage:
    """Тесты Подвала сайта."""

    @allure.story('Элементы страницы')
    @allure.title('Проверка текста ссылок в подвале на Главной странице')
    @allure.link('#', name='User story')
    def test_check_footer_links_text_on_main_page(self, browser, url, return_lst):
        """Тестовая функция для проверки текста ссылок в подвале на главой странице.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = MainPage(browser, url)
        page.open_url()
        page.footer.check_footer_links(return_lst)

    @allure.story('Элементы страницы')
    @allure.title('Проверка текста ссылок в подвале на странице Корзины')
    @allure.link('#', name='User story')
    def test_check_footer_links_text_on_cart_page(self, browser, url, return_lst):
        """Тестовая функция для проверки текста ссылок в подвале на странице корзины.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = CartPage(browser, url)
        page.open_url(path=URLS.CART_PAGE)
        page.footer.check_footer_links(return_lst)

    @allure.story('Элементы страницы')
    @allure.title('Проверка текста ссылок в подвале на странице Поиска')
    @allure.link('#', name='User story')
    def test_check_footer_links_text_on_search_page(self, browser, url, return_lst):
        """Тестовая функция для проверки текста ссылок в подвале на странице поиска.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = SearchPage(browser, url)
        page.open_url(path=URLS.SEARCH_PAGE)
        page.footer.check_footer_links(return_lst)

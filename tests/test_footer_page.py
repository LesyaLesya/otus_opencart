"""Модуль с тестами для Подвала сайта."""

import allure
import pytest

from helpers.urls import URLS
from pages.cart_page import CartPage
from pages.catalogue_page import CataloguePage
from pages.main_page import MainPage
from pages.product_page import ProductPage
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

    common_args = ('pages, path',
                   [(SearchPage, URLS.SEARCH_PAGE), (CartPage, URLS.CART_PAGE),
                    (MainPage, ''), (ProductPage, URLS.PRODUCT_PAGE),
                    (CataloguePage, URLS.CATALOGUE_PAGE)])

    @allure.story('Элементы страницы')
    @allure.title('Проверка текста ссылок в подвале на странице {pages}')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize(*common_args)
    def test_check_footer_links_text(self, browser, url, return_lst, pages, path):
        """Тестовая функция для проверки текста ссылок в подвале на страницах.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = pages(browser, url)
        page.open_url(path=path)
        page.footer.check_footer_links(return_lst)

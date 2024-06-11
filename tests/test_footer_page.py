"""Модуль с тестами для Подвала сайта."""

import allure
import pytest

from base.base_test import BaseTest


@allure.feature('Подвал сайта')
@pytest.mark.footer_page
class TestFooterPage(BaseTest):
    """Тесты Подвала сайта."""


    common_args = ('page', ['search_page', 'cart_page', 'main_page', 'product_page', 'catalogue_page'])

    @allure.story('Элементы страницы')
    @allure.title('Проверка текста ссылок в подвале на страницах')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize(*common_args)
    def test_check_footer_links_text(self, page):
        """Тестовая функция для проверки текста ссылок в подвале на страницах.

        """
        lst = ['About Us', 'Delivery Information', 'Privacy Policy',
               'Terms & Conditions', 'Contact Us', 'Returns',
               'Site Map', 'Brands', 'Gift Certificates', 'Affiliate',
               'Specials', 'My Account', 'Order History', 'Wish List',
               'Newsletter']
        eval(f"self.{page}").open_url()
        self.footer.check_footer_links(lst)

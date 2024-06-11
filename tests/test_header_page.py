"""Модуль с тестами для Шапки сайта."""

import allure
import pytest

from utils.locators import HeaderPageLocators
from base.base_test import BaseTest


@pytest.fixture(scope='module')
def dropdown_menu():
    dd_menu = [(HeaderPageLocators.DESKTOPS_IN_MENU, HeaderPageLocators.DROPDOWN_FOR_DESKTOPS),
               (HeaderPageLocators.COMPONENTS_IN_MENU, HeaderPageLocators.COMPONENTS_FOR_DROPDOWN),
               (HeaderPageLocators.LAPTOPS_IN_MENU, HeaderPageLocators.LAPTOPS_FOR_DROPDOWN)]
    return dd_menu


@allure.feature('Шапка сайта')
@pytest.mark.header_page
class TestHeaderPage(BaseTest):
    """Тесты Шапки сайта."""

    common_args = ('page', ['search_page', 'cart_page', 'main_page', 'catalogue_page'])

    @allure.story('Видимость элементов шапки')
    @allure.title('Проверка видимости элементов шапки сайта на странице - {page}')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize(*common_args)
    def test_visibility_of_header_elements(self, page):
        """Тестовая функция для проверки видимости элементов шапки сайта.

        """
        eval(f"self.{page}").open_url()
        self.header.check_elements_visibility()

    @allure.story('Переход на другие страницы из шапки сайта')
    @allure.title('Переход на страницу Логина из шапки со страницы {page}')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize(*common_args)
    def test_go_to_login_page_from_header(self, page):
        """Тестовая функция для проверки перехода на страницу логина из шапки сайта.

        """
        eval(f"self.{page}").open_url()
        self.header.go_to_login_page()
        self.login_page.is_title_correct(self.login_page.TITLE)

    @allure.story('Поиск по сайту из шапки')
    @allure.title('Проверка открытия страницы с результатом поиска из шапки со страницы {page}')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize(*common_args)
    @pytest.mark.parametrize('value', ['phone', 'laptop', 'HP'])
    def test_search_result_title_from_header(self, page, value):
        """Тестовая функция для проверки тайтла страницы с результатами поиска из шапки.

        :param value: значение, вводимое в строку поиска
        """
        eval(f"self.{page}").open_url()
        self.header.search_input(value)
        self.header.search_start()
        self.search_page.is_title_correct(f'Search - {value}')

    @allure.story('Проверка стилей элементов шапки')
    @allure.title('Проверка стилей кнопки корзины в шапке на странице {page}')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize(*common_args)
    def test_cart_button_styles_in_header(self, page):
        """Тестовая функция для стилей кнопки корзины в шапке.

        """
        eval(f"self.{page}").open_url()
        self.header.check_cart_button_css()
        self.header.check_cart_button_css_hover()
        self.header.check_cart_button_css_click()

    @allure.story('Проверка выпадающих списков шапки')
    @allure.title('Проверка значений в списке валют в шапке на странице {page}')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize(*common_args)
    def test_currency_values_in_header(self, page):
        """Тестовая функция проверки значений валют в шапке.

        """
        eval(f"self.{page}").open_url()
        self.header.click_on_currency_drop_down()
        self.header.check_currency_values(['€ Euro', '£ Pound Sterling', '$ US Dollar'])

    @allure.story('Проверка выпадающих списков шапки')
    @allure.title('Проверка выпадающих списков горизонтального меню в шапке на странице {page}')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize(*common_args)
    def test_dropdown_in_menu_in_header(self, page, dropdown_menu):
        """Тестовая функция проверки выпадающих списков горизонтального меню в шапке.

        """
        eval(f"self.{page}").open_url()
        self.header.check_dropdown_menu(dropdown_menu)

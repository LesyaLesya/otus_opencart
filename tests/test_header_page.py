"""Модуль с тестами для Шапки сайта."""

import allure
import pytest

from helpers.locators import HeaderPageLocators
from helpers.urls import URLS
from pages.account_page import LoginPage
from pages.catalogue_page import CataloguePage
from pages.main_page import MainPage
from pages.search_page import SearchPage


@pytest.fixture(scope='module')
def dropdown_menu():
    dd_menu = [(HeaderPageLocators.DESKTOPS_IN_MENU, HeaderPageLocators.DROPDOWN_FOR_DESKTOPS),
               (HeaderPageLocators.COMPONENTS_IN_MENU, HeaderPageLocators.COMPONENTS_FOR_DROPDOWN),
               (HeaderPageLocators.LAPTOPS_IN_MENU, HeaderPageLocators.LAPTOPS_FOR_DROPDOWN)]
    return dd_menu


@allure.feature('Шапка сайта')
@pytest.mark.header_page
class TestHeaderPage:
    """Тесты Шапки сайта."""

    common_args = ('pages, path',
                   [(MainPage, ''), (SearchPage, URLS.SEARCH_PAGE), (CataloguePage, URLS.CATALOGUE_PAGE)])

    @allure.story('Видимость элементов шапки')
    @allure.title('Проверка видимости элементов шапки сайта на странице - {pages}')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize(*common_args)
    def test_visibility_of_header_elements(self, browser, url, pages, path):
        """Тестовая функция для проверки видимости элементов шапки сайта.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = pages(browser, url)
        page.open_url(path=path)
        page.header.check_elements_visibility()

    @allure.story('Переход на другие страницы из шапки сайта')
    @allure.title('Переход на страницу Логина из шапки со страницы {pages}')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize(*common_args)
    def test_go_to_login_page_from_header(self, browser, url, pages, path):
        """Тестовая функция для проверки перехода на страницу логина из шапки сайта.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = pages(browser, url)
        page.open_url(path=path)
        page.header.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.is_title_correct('Account Login')

    @allure.story('Поиск по сайту из шапки')
    @allure.title('Проверка открытия страницы с результатом поиска из шапки со страницы {pages}')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize(*common_args)
    @pytest.mark.parametrize('value', ['phone', 'laptop', 'HP'])
    def test_search_result_title_from_header(self, browser, url, pages, path, value):
        """Тестовая функция для проверки тайтла страницы с результатами поиска из шапки.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        :param value: значение, вводимое в строку поиска
        """
        page = pages(browser, url)
        page.open_url(path=path)
        page.header.search(value)
        search_page = SearchPage(browser, browser.current_url)
        search_page.is_title_correct(f'Search - {value}')

    @allure.story('Проверка стилей элементов шапки')
    @allure.title('Проверка стилей кнопки корзины в шапке на странице {pages}')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize(*common_args)
    def test_cart_button_styles_in_header(self, browser, url, pages, path):
        """Тестовая функция для стилей кнопки корзины в шапке.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = pages(browser, url)
        page.open_url(path=path)
        page.header.check_cart_button_css()
        page.header.check_cart_button_css_hover()
        page.header.check_cart_button_css_click()

    @allure.story('Проверка выпадающих списков шапки')
    @allure.title('Проверка значений в списке валют в шапке на странице {pages}')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize(*common_args)
    def test_currency_values_in_header(self, browser, url, pages, path):
        """Тестовая функция проверки значений валют в шапке.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = pages(browser, url)
        page.open_url(path=path)
        page.header.click_on_currency_drop_down()
        page.header.check_currency_values(['€ Euro', '£ Pound Sterling', '$ US Dollar'])

    @allure.story('Проверка выпадающих списков шапки')
    @allure.title('Проверка выпадающих списков горизонтального меню в шапке на странице {pages}')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize(*common_args)
    def test_dropdown_in_menu_in_header(self, browser, url, pages, path, dropdown_menu):
        """Тестовая функция проверки выпадающих списков горизонтального меню в шапке.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = pages(browser, url)
        page.open_url(path=path)
        page.header.check_dropdown_menu(dropdown_menu)

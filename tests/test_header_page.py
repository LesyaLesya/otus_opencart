"""Модуль с тестами для Шапки сайта."""

import allure
import pytest

from helpers.locators import HeaderPageLocators
from helpers.urls import URLS
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.search_page import SearchPage


@allure.feature('Шапка сайта')
@allure.story('Видимость элементов шапки на разных страницах')
@pytest.mark.header_page
class TestHeaderPageVisibilityElements:
    """Тесты Шапки сайта - видимость элементов."""

    @allure.title('Проверка видимости элементов шапки сайта на главной странице')
    @allure.link('#', name='User story')
    def test_visibility_of_header_elements_on_main_page(self, browser, url):
        """Тестовая функция для проверки видимости элементов шапки сайта на главной странице.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = MainPage(browser, url)
        page.open_url()
        page.header.check_elements_visibility()

    @allure.title('Проверка видимости элементов шапки сайта на странице поиска')
    @allure.link('#', name='User story')
    def test_visibility_of_header_elements_on_search_page(self, browser, url):
        """Тестовая функция для проверки видимости элементов шапки сайта на странице поиска.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = SearchPage(browser, url)
        page.open_url(path=URLS.SEARCH_PAGE)
        page.header.check_elements_visibility()


@allure.feature('Шапка сайта')
@allure.story('Переход на другие страницы из шапки сайта на разных страницах')
@pytest.mark.header_page
class TestHeaderPageGoOtherPages:
    """Тесты Шапки сайта - переход на другие страницы из шапки с разных страниц."""

    @allure.title('Переход на страницу Логина из шапки с главной страницы')
    @allure.link('#', name='User story')
    def test_go_to_login_page_from_header_on_main(self, browser, url):
        """Тестовая функция для проверки перехода на страницу логина из шапки сайта с главной страницы.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = MainPage(browser, url)
        page.open_url()
        page.header.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.is_title_correct('Account Login')


@allure.feature('Шапка сайта')
@allure.story('Поиск по сайту из шапки на разных страницах')
@pytest.mark.header_page
class TestHeaderPageSearch:
    """Тесты Шапки сайта - поиск по сайту из шапки на разных страницах."""

    @allure.title('Проверка открытия страницы с результатом поиска из шапки с главной страницы')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('value',
                             ['phone', 'laptop', 'HP'], ids=['phone', 'laptop', 'HP'])
    def test_search_result_title_from_header_on_main(self, browser, url, value):
        """Тестовая функция для проверки тайтла страницы с результатами поиска из шапки с главной страницы.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        :param value: значение, вводимое в строку поиска
        """
        page = MainPage(browser, url)
        page.open_url()
        page.header.search(value)
        search_page = SearchPage(browser, browser.current_url)
        search_page.is_title_correct(f'Search - {value}')


@allure.feature('Шапка сайта')
@allure.story('Проверка стилей элементов из шапки на разных страницах')
@pytest.mark.header_page
class TestHeaderPageElementsStyles:
    """Тесты Шапки сайта - проверка стилей элеемнтов из шапки на разных страницах."""

    @allure.title('Проверка стилей кнопки корзины в шапке на Главной')
    @allure.link('#', name='User story')
    def test_cart_button_styles_in_header_on_main(self, browser, url):
        """Тестовая функция для стилей кнопки корзины в шапке на Главной.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = MainPage(browser, url)
        page.open_url()
        page.header.check_cart_button_css()
        page.header.check_cart_button_css_hover()
        page.header.check_cart_button_css_click()

    @allure.title('Проверка стилей кнопки корзины в шапке на странице Поиска')
    @allure.link('#', name='User story')
    def test_cart_button_styles_in_header_on_search(self, browser, url):
        """Тестовая функция для стилей кнопки корзины в шапке на странице поиска.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = SearchPage(browser, url)
        page.open_url(path=URLS.SEARCH_PAGE)
        page.header.check_cart_button_css()
        page.header.check_cart_button_css_hover()
        page.header.check_cart_button_css_click()


@allure.feature('Шапка сайта')
@allure.story('Проверка выпадающих списков из шапки на разных страницах')
@pytest.mark.header_page
class TestHeaderPageDropDowns:
    """Тесты Шапки сайта - проверка выпадающих списков из шапки на разных страницах."""

    @allure.title('Проверка значений в списке валют в шапке на Главной')
    @allure.link('#', name='User story')
    def test_currency_values_in_header_on_main(self, browser, url):
        """Тестовая функция проверки значений валют в шапке на главной страницы.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = MainPage(browser, url)
        page.open_url()
        page.header.click_on_currency_drop_down()
        page.header.check_currency_values(['€ Euro', '£ Pound Sterling', '$ US Dollar'])

    @allure.title('Проверка выпадающих списков горизонтального меню в шапке на Главной')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('menu_locator, dropdown_locator',
                             [(HeaderPageLocators.DESKTOPS_IN_MENU, HeaderPageLocators.DROPDOWN_FOR_DESKTOPS),
                              (HeaderPageLocators.COMPONENTS_IN_MENU, HeaderPageLocators.COMPONENTS_FOR_DROPDOWN),
                              (HeaderPageLocators.LAPTOPS_IN_MENU, HeaderPageLocators.LAPTOPS_FOR_DROPDOWN)])
    def test_dropdown_in_menu_in_header_on_main(self, browser, url, menu_locator, dropdown_locator):
        """Тестовая функция проверки выпадающих списков горизонтального меню в шапке на Главной.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        :param menu_locator: локатор пункта меню
        :param dropdown_locator: локаторы выпадающих меню
        """
        page = MainPage(browser, url)
        page.open_url()
        page.mouse_move_to_element(*menu_locator)
        page.is_element_visible(*dropdown_locator)

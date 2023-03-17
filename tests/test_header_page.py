"""Модуль с тестами для Шапки сайта."""

import allure
import pytest

from helpers.locators import HeaderPageLocators
from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from pages.search_page import SearchPage


@allure.feature('Шапка сайта')
@pytest.mark.header_page
class TestHeaderPage:
    """Тесты Шапки сайта."""

    @allure.story('Элементы страницы')
    @allure.title('Проверка видимости элементов на странице')
    @allure.link('#', name='User story')
    def test_visibility_of_elements_on_header_page(self, browser, url):
        """Тестовая функция для проверки видимости элементов в шапке сайта.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = HeaderPage(browser, url)
        page.open_url()
        page.check_elements_visibility()

    @allure.story('Переход на другие страницы')
    @allure.title('Переход на страницу Логина')
    @allure.link('#', name='User story')
    def test_go_to_login_page(self, browser, url):
        """Тестовая функция для проверки перехода на другие
        страницы из шапки сайта.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = HeaderPage(browser, url)
        page.open_url()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.is_title_correct('Account Login')

    @allure.story('Работа поиска по сайту')
    @allure.title('Проверка открытия страницы с результатом поиска')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('value',
                             ['phone', 'laptop', 'HP'], ids=['phone', 'laptop', 'HP'])
    def test_search_result_title(self, browser, url, value):
        """Тестовая функция для проверки тайтла страницы с результатами поиска.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        :param value: значение, вводимое в строку поиска
        """
        page = HeaderPage(browser, url)
        page.open_url()
        page.search(value)
        search_page = SearchPage(browser, browser.current_url)
        search_page.is_title_correct(f'Search - {value}')

    @allure.story('Стили страницы')
    @allure.title('Проверка стилей кнопки корзины')
    @allure.link('#', name='User story')
    def test_cart_button_styles(self, browser, url):
        """Тестовая функция для стилей кнопки корзины.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = HeaderPage(browser, url)
        page.open_url()
        page.check_cart_button_css()
        page.check_cart_button_css_hover()
        page.check_cart_button_css_click()

    @allure.story('Проверка выпадающих списков')
    @allure.title('Проверка значений в списке валют')
    @allure.link('#', name='User story')
    def test_currency_values(self, browser, url):
        """Тестовая функция проверки значений валют.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = HeaderPage(browser, url)
        page.open_url()
        page.click_on_currency_drop_down()
        page.check_currency_values(['€ Euro', '£ Pound Sterling', '$ US Dollar'])

    @allure.story('Проверка выпадающих списков')
    @allure.title('Проверка выпадающих списков горизонтального меню')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('menu_locator, dropdown_locator',
                             [(HeaderPageLocators.DESKTOPS_IN_MENU, HeaderPageLocators.DROPDOWN_FOR_DESKTOPS),
                              (HeaderPageLocators.COMPONENTS_IN_MENU, HeaderPageLocators.COMPONENTS_FOR_DROPDOWN),
                              (HeaderPageLocators.LAPTOPS_IN_MENU, HeaderPageLocators.LAPTOPS_FOR_DROPDOWN)])
    def test_dropdown_in_menu(self, browser, url, menu_locator, dropdown_locator):
        """Тестовая функция проверки выпадающих списков горизонтального меню.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        :param menu_locator: локатор пункта меню
        :param dropdown_locator: локаторы выпадающих меню
        """
        page = HeaderPage(browser, url)
        page.open_url()
        page.check_dropdown_menu(menu_locator, dropdown_locator)

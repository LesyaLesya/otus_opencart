"""Модуль с тестами для страницы Каталога."""


import allure
import pytest

from helpers.locators import CataloguePageLocators
from helpers.urls import URLS
from pages.account_page import AccountPage
from pages.catalogue_page import CataloguePage
from pages.comparison_page import ComparisonPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


@allure.feature('Страница Каталога')
@pytest.mark.catalogue_page
class TestCataloguePage:
    """Тесты страницы Каталога."""

    @allure.story('Элементы страницы')
    @allure.title('Проверка видимости элементов на странице')
    @allure.link('#', name='User story')
    def test_visibility_of_elements_on_catalogue_page(self, browser, url):
        """Тестовая функция для проверки видимости элементов на странице Каталога.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = CataloguePage(browser, url)
        page.open_url(path=URLS.CATALOGUE_PAGE)
        page.check_elements_visibility()

    @allure.story('Сортировка товаров')
    @allure.title('Сортировка по названию от A до Z')
    @allure.link('#', name='User story')
    def test_sort_by_name_a_z(self, browser, url):
        """Тестовая функция для проверки сортировки товаров по
        названию от A до Z.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = CataloguePage(browser, url)
        page.open_url(path=URLS.CATALOGUE_PAGE)
        page.select_by_text('Name (A - Z)')
        page.check_sort_by_name_a_z()

    @allure.story('Сортировка товаров')
    @allure.title('Сортировка по названию от Z до A')
    @allure.link('#', name='User story')
    def test_sort_by_name_z_a(self, browser, url):
        """Тестовая функция для проверки сортировки товаров по
        названию от Z до A.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = CataloguePage(browser, url)
        page.open_url(path=URLS.CATALOGUE_PAGE)
        page.select_by_text('Name (Z - A)')
        page.check_sort_by_name_z_a()

    @allure.story('Сортировка товаров')
    @allure.title('Сортировка по цене Low > High')
    @allure.link('#', name='User story')
    def test_sort_by_price_low_to_high(self, browser, url):
        """Тестовая функция для проверки сортировки товаров по
        возрастанию цены.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = CataloguePage(browser, url)
        page.open_url(path=URLS.CATALOGUE_PAGE)
        page.select_by_text("Price (Low > High)")
        page.check_sort_by_price_low_high()

    @allure.story('Переход на другие страницы')
    @allure.title('Переход в карточку товара по клику на товар')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('idx', [0, 1])
    def test_go_to_product_from_catalogue(self, browser, url, idx):
        """Тестовая функция для проверки перехода
        в карточку товара по клику из каталога товаров.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        :param idx: порядковый индекс элемента
        """
        page = CataloguePage(browser, url)
        page.open_url(path=URLS.CATALOGUE_PAGE)
        name = page.go_to_product_from_catalogue(idx)
        product_page = ProductPage(browser, browser.current_url)
        product_page.compare_item_title_on_pages(name)

    @allure.story('Добавление товара в Виш-лист')
    @allure.title('Добавление товара в Виш-лист из каталога')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('idx', [0])
    def test_adding_to_wish_list_from_catalogue(self, browser, url, db_connection, idx):
        """Тестовая функция для проверки добавления продукта
        в виш-лист из каталога.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        :param db_connection: фикстура коннекта к БД
        :param idx: порядковый индекс элемента
        """
        page = CataloguePage(browser, url)
        page.open_url(path=URLS.CATALOGUE_PAGE)
        name = page.add_to_wishlist(idx)
        page.alert.click_login_from_alert()
        login_page = LoginPage(browser, browser.current_url, db_connection)
        login_page.login_user()
        account_page = AccountPage(browser, browser.current_url)
        account_page.open_wishlist()
        account_page.check_item_in_wish_list(name)

    @allure.story('Добавление товара в сравнение')
    @allure.title('Добавление товара в сравнение из каталога')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('idx', [1])
    def test_adding_to_compare_from_catalogue(self, browser, url, idx):
        """Тестовая функция для проверки добавление товара к сравнению
        со страницы каталога.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        :param idx: порядковый индекс элемента
        """
        page = CataloguePage(browser, url)
        page.open_url(path=URLS.CATALOGUE_PAGE)
        name = page.add_to_compare(idx)
        page.check_adding_in_compare_link('1')
        page.go_to_compare_page()
        compare_page = ComparisonPage(browser, browser.current_url)
        compare_page.check_item_in_comparison(name)

    @allure.story('Переключение вида отображения карточек товара')
    @allure.title('Переключение вида отображения карточек товара')
    @allure.link('#', name='User story')
    def test_change_view_carts(self, browser, url):
        """Тестовая функция для проверки изменения отображения вида
        вывода карточек товара.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = CataloguePage(browser, url)
        page.open_url(path=URLS.CATALOGUE_PAGE)
        page.click_list_view()
        page.click_list_grid()

    @allure.story('Переключение валют')
    @allure.title('Изменение валют в цене товаров')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('values, idx, symbol',
                             [('€ Euro', -1, '€'),
                              ('£ Pound Sterling', 0, '£'),
                              ('$ US Dollar', 0, '$')])
    def test_change_currency(self, browser, url, values, idx, symbol):
        """Тестовая функция для проверки изменения валюты
        в ценах товаров в каталоге

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        :param values: валюты
        :param idx: порядковый индекс символа в цене товара
        :param symbol: строковое представление символа валюты
        """
        page = CataloguePage(browser, url)
        page.open_url(path=URLS.CATALOGUE_PAGE)
        page.header.choose_currency(values)
        catalogue_page2 = CataloguePage(browser, browser.current_url)
        catalogue_page2.check_currency_in_price(idx, symbol)

    @allure.story('Стили страницы')
    @allure.title('Проверка стилей кнопки добавления в корзину')
    @allure.link('#', name='User story')
    def test_add_to_cart_css(self, browser, url):
        """Тестовая функция для стилей кнопки добавления в корзину.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = CataloguePage(browser, url)
        page.open_url(path=URLS.CATALOGUE_PAGE)
        page.check_add_to_cart_css()
        page.check_add_to_cart_css_hover()

    @allure.story('Проверка бокового меню')
    @allure.title('Проверка перехода в другие разделы каталога')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('categories, value', [
        (CataloguePageLocators.DESKTOPS_IN_LEFT_MENU, 'Desktops'),
        (CataloguePageLocators.LAPTOPS_IN_LEFT_MENU, 'Laptops & Notebooks'),
        (CataloguePageLocators.COMPONENTS_IN_LEFT_MENU, 'Components'),
        (CataloguePageLocators.TABLETS_IN_LEFT_MENU, 'Tablets'),
        (CataloguePageLocators.SOFTWARE_IN_LEFT_MENU, 'Software'),
        (CataloguePageLocators.PHONES_IN_LEFT_MENU, 'Phones & PDAs'),
        (CataloguePageLocators.CAMERAS_IN_LEFT_MENU, 'Cameras'),
        (CataloguePageLocators.MP3_IN_LEFT_MENU, 'MP3 Players')])
    def test_go_to_others_catalogue_sections(self, browser, url, categories, value):
        """Тестовая функция для проверки перехода в другие разделы каталога.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        :param categories: локаторы разделов каталога в левом меню
        :param value: название категории каталога
        """
        page = CataloguePage(browser, url)
        page.open_url(path=URLS.CATALOGUE_PAGE)
        page.click_on_element(*categories)
        new_catalogue_page = CataloguePage(browser, browser.current_url)
        new_catalogue_page.is_title_correct(value)
        new_catalogue_page.check_catalogue_page_header(value)

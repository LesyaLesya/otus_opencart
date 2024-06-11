"""Модуль с тестами для страницы Каталога."""


import allure
import pytest

from utils.locators import CataloguePageLocators
from base.base_test import BaseTest


@allure.feature('Страница Каталога')
@pytest.mark.catalogue_page
class TestCataloguePage(BaseTest):
    """Тесты страницы Каталога."""

    @allure.story('Элементы страницы')
    @allure.title('Проверка видимости элементов на странице')
    @allure.link('#', name='User story')
    def test_visibility_of_elements_on_catalogue_page(self):
        """Тестовая функция для проверки видимости элементов на странице Каталога.

        """
        self.catalogue_page.open_url()
        self.catalogue_page.check_elements_visibility()

    @allure.story('Сортировка товаров')
    @allure.title('Сортировка по названию от A до Z')
    @allure.link('#', name='User story')
    def test_sort_by_name_a_z(self):
        """Тестовая функция для проверки сортировки товаров по
        названию от A до Z.

        """
        self.catalogue_page.open_url()
        self.catalogue_page.select_by_text(self.catalogue_page.SORT_A_Z)
        self.catalogue_page.check_sort_by_name_a_z()

    @allure.story('Сортировка товаров')
    @allure.title('Сортировка по названию от Z до A')
    @allure.link('#', name='User story')
    def test_sort_by_name_z_a(self):
        """Тестовая функция для проверки сортировки товаров по
        названию от Z до A.

        """
        self.catalogue_page.open_url()
        self.catalogue_page.select_by_text(self.catalogue_page.SORT_Z_A)
        self.catalogue_page.check_sort_by_name_z_a()

    @allure.story('Сортировка товаров')
    @allure.title('Сортировка по цене Low > High')
    @allure.link('#', name='User story')
    def test_sort_by_price_low_to_high(self):
        """Тестовая функция для проверки сортировки товаров по
        возрастанию цены.

        """
        self.catalogue_page.open_url()
        self.catalogue_page.select_by_text(self.catalogue_page.SORT_PRICE_L_H)
        self.catalogue_page.check_sort_by_price_low_high()

    @allure.story('Переход на другие страницы')
    @allure.title('Переход в карточку товара по клику на товар')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('idx', [0, 1])
    def test_go_to_product_from_catalogue(self, idx):
        """Тестовая функция для проверки перехода
        в карточку товара по клику из каталога товаров.

        :param idx: порядковый индекс элемента
        """
        self.catalogue_page.open_url()
        name = self.catalogue_page.go_to_product_from_catalogue(idx)
        self.product_page.compare_item_title_on_pages(name)

    @allure.story('Добавление товара в Виш-лист')
    @allure.title('Добавление товара в Виш-лист из каталога')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('idx', [0])
    def test_adding_to_wish_list_from_catalogue(self, idx, fixture_create_delete_user):
        """Тестовая функция для проверки добавления продукта
        в виш-лист из каталога.

        :param idx: порядковый индекс элемента
        :param fixture_create_delete_user: фикстура создания и удаления тестового пользователя
        """
        email, firstname, lastname, telephone, user_id = fixture_create_delete_user
        self.catalogue_page.open_url()
        name, item_id = self.catalogue_page.add_to_wishlist(idx)
        self.alert.click_login_from_alert()
        self.login_page.login_user(email)
        self.wishlist_page.open_wishlist()
        self.wishlist_page.check_items_in_wish_list(name, 1)
        self.db.check_item_in_wishlist_in_db(self.db_connection, user_id, item_id)

    @allure.story('Добавление товара в сравнение')
    @allure.title('Добавление товара в сравнение из каталога')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('idx', [1])
    def test_adding_to_compare_from_catalogue(self, idx):
        """Тестовая функция для проверки добавление товара к сравнению
        со страницы каталога.

        :param idx: порядковый индекс элемента
        """
        self.catalogue_page.open_url()
        name = self.catalogue_page.add_to_compare(idx)
        self.catalogue_page.check_adding_in_compare_link('1')
        self.catalogue_page.go_to_compare_page()
        self.comparison_page.check_item_in_comparison(name)

    @allure.story('Переключение вида отображения карточек товара')
    @allure.title('Переключение вида отображения карточек товара')
    @allure.link('#', name='User story')
    def test_change_view_carts(self):
        """Тестовая функция для проверки изменения отображения вида
        вывода карточек товара.

        """
        self.catalogue_page.open_url()
        self.catalogue_page.click_list_view()
        self.catalogue_page.click_list_grid()

    @allure.story('Переключение валют')
    @allure.title('Изменение валют в цене товаров')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('values, idx, symbol',
                             [('€ Euro', -1, '€'),
                              ('£ Pound Sterling', 0, '£'),
                              ('$ US Dollar', 0, '$')])
    def test_change_currency(self, values, idx, symbol):
        """Тестовая функция для проверки изменения валюты
        в ценах товаров в каталоге

        :param values: валюты
        :param idx: порядковый индекс символа в цене товара
        :param symbol: строковое представление символа валюты
        """
        self.catalogue_page.open_url()
        self.header.choose_currency(values)
        self.catalogue_page.check_currency_in_price(idx, symbol)

    @allure.story('Стили страницы')
    @allure.title('Проверка стилей кнопки добавления в корзину')
    @allure.link('#', name='User story')
    def test_add_to_cart_css(self):
        """Тестовая функция для стилей кнопки добавления в корзину.

        """
        self.catalogue_page.open_url()
        self.catalogue_page.check_add_to_cart_css()
        self.catalogue_page.check_add_to_cart_css_hover()

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
    def test_go_to_others_catalogue_sections(self, categories, value):
        """Тестовая функция для проверки перехода в другие разделы каталога.

        :param categories: локаторы разделов каталога в левом меню
        :param value: название категории каталога
        """
        self.catalogue_page.open_url()
        self.catalogue_page.click_on_element(*categories)
        self.catalogue_page.is_title_correct(value)
        self.catalogue_page.check_catalogue_page_header(value)

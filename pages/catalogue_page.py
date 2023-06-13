"""Модуль c методами для страницы Каталога."""
import time

import allure

from helpers import allure_helper
from helpers.locators import CataloguePageLocators
from helpers.styles import Colors, Cursor, FontWeight
from pages.base_page import BasePage


class CataloguePage(BasePage):
    """Класс с методами для страницы Каталога."""

    @allure.step('Проверить видимость элементов на странице')
    def check_elements_visibility(self):
        """Проверка видимости элементов."""
        lst = [CataloguePageLocators.BREADCRUMB,
               CataloguePageLocators.CATALOGUE_HEADER,
               CataloguePageLocators.CATALOGUE_IMAGE,
               CataloguePageLocators.LEFT_MENU,
               CataloguePageLocators.BANNER_UNDER_LEFT_MENU]
        for i in lst:
            self.is_element_visible(*i)

    @allure.step('Добавить товар с индексом {index} в сравнение')
    def add_to_compare(self, index):
        """Добавление товара в сравнение. Возвращает название
        добавленного товара.

        :param index: порядковый индекс
        """
        name = self.get_text_of_element(*CataloguePageLocators.ITEM_NAME, index)
        self.click_on_element(*CataloguePageLocators.COMPARE_BUTTON, index)
        return name

    @allure.step('Кликнуть на кнопку Сравнения в алерте')
    def go_to_compare_page(self):
        """Клик по ссылке Сравнения."""
        self.click_on_element(*CataloguePageLocators.COMPARE_LINK)

    @allure.step('Проверить, что товар добавился к сравнению - значение в ссылке увеличилось на {value}')
    def check_adding_in_compare_link(self, value):
        """Проверка изменения количества товаров в сравнении
        после добавления в сравнение.

        :param value: количество товаров в сравнении
        """
        link_txt = self.get_text_of_element(*CataloguePageLocators.COMPARE_LINK)
        with allure.step(f'Проверить, что текст ссылки {link_txt} == Product Compare ({value})'):
            allure_helper.attach(self.browser)
            assert link_txt == f'Product Compare ({value})', f'Текст - {link_txt}'

    @allure.step('Сортировать товары по {txt}')
    def select_by_text(self, txt):
        """Сортировка товаров по значению из списка (тексту).

        :param txt: значения в выпадающем списке
        """
        element = self.select_products(*CataloguePageLocators.SELECT_SORT)
        element.select_by_visible_text(txt)

    @allure.step('Проверить, что товары отсортированы от A до Z')
    def check_sort_by_name_a_z(self):
        """Получение всех названий товаров после сортировки и проверка
        заданной сортировки."""
        elements = self._element(*CataloguePageLocators.ITEM_NAME, all=True)
        names = [i.text for i in elements]
        with allure.step(f'Проверить порядок в списке названий {names}'):
            allure_helper.attach(self.browser)
            assert all(names[i] < names[i+1] for i in range(len(names)-1)), f'Порядок названий - {names}'

    @allure.step('Проверить, что товары отсортированы от Z до A')
    def check_sort_by_name_z_a(self):
        """Получение всех названий товаров после сортировки и проверка
        заданной сортировки."""
        elements = self._element(*CataloguePageLocators.ITEM_NAME, all=True)
        names = [i.text for i in elements]
        with allure.step(f'Проверить порядок в списке названий {names}'):
            allure_helper.attach(self.browser)
            assert all(names[i] > names[i + 1] for i in range(len(names) - 1)), f'Порядок названий - {names}'

    @allure.step('Проверить, что товары отсортированы по возрастанию цены')
    def check_sort_by_price_low_high(self):
        """Получение всех цен товаров после сортировки и проверка
        заданной сортировки."""
        elements = self._element(*CataloguePageLocators.ITEM_PRICE, all=True)
        prices_with_tax = [i.text for i in elements]
        prices_without_tax = [i.split('\nEx')[0] for i in prices_with_tax]
        prices_in_float = [float(i.replace(',', '').replace('$', '')) for i in prices_without_tax]
        with allure.step(f'Проверить порядок в списке цен {prices_in_float}'):
            allure_helper.attach(self.browser)
            assert all(prices_in_float[i] <= prices_in_float[i+1] for i in range(len(prices_in_float)-1)), \
                f'Порядок цен - {prices_in_float}'

    @allure.step('Перейти в карточку продукта с индексом {index} со страницы каталога')
    def go_to_product_from_catalogue(self, index):
        """Клик по товару из каталога.
        Возвращает название товара.

        :param index: порядковый индекс элемента
        """
        name = self.get_text_of_element(*CataloguePageLocators.ITEM_NAME, index)
        self.click_on_element(*CataloguePageLocators.ITEM_NAME, index)
        return name

    @allure.step('Добавить продукт с индексом {index} в виш лист')
    def add_to_wishlist(self, index):
        """Добавление товара в вишлист. Возвращает название
        добавленного товара.

        :param index: порядковый индекс элемента
        """
        name = self.get_text_of_element(*CataloguePageLocators.ITEM_NAME, index)
        item_id = self.get_item_id(*CataloguePageLocators.WISH_LIST_BUTTON, index)
        self.click_on_element(*CataloguePageLocators.WISH_LIST_BUTTON, index)
        time.sleep(1)
        return name, item_id

    @allure.step('Кликнуть на кнопку вида Список')
    def click_list_view(self):
        """Клик по кнопке с видом списка и проверка изменения вида."""
        elements = self._element(*CataloguePageLocators.ITEM_CART, all=True)
        self.click_on_element(*CataloguePageLocators.LIST_VIEW_BUTTON)
        for i in range(len(elements)):
            attr = self.getting_attr('class', *CataloguePageLocators.ITEM_CART, i)
            with allure.step(f'Проверить, что товар с индексом {i} имеет класс со значением product-list'):
                allure_helper.attach(self.browser)
                assert 'product-list' in attr, f'Значение атрибута -  {attr}'

    @allure.step('Кликнуть на кнопку вида Сетка')
    def click_list_grid(self):
        """Клик по кнопке с видом сетки и проверка изменения вида."""
        elements = self._element(*CataloguePageLocators.ITEM_CART, all=True)
        self.click_on_element(*CataloguePageLocators.GRID_VIEW_BUTTON)
        for i in range(len(elements)):
            attr = self.getting_attr('class', *CataloguePageLocators.ITEM_CART, i)
            with allure.step(f'Проверить, что товар с индексом {i} имеет класс со значением product-grid'):
                allure_helper.attach(self.browser)
                assert 'product-grid' in attr, f'Значение атрибута -  {attr}'

    @allure.step('Сравнить символ в ценах товаров с символом выбранной валюты')
    def check_currency_in_price(self, index, symbol):
        """Проверка отображения значка валюты в ценах.

        :param index: порядковый индекс элемента
        :param symbol: символ валюты
        """
        elements = self._element(*CataloguePageLocators.ITEM_PRICE, all=True)
        prices_with_tax = [i.text for i in elements]
        prices_without_tax = [i.split('\nEx')[0] for i in prices_with_tax]
        with allure.step(f'Проверить, что во всех ценах {prices_without_tax} символ {symbol}'):
            allure_helper.attach(self.browser)
            assert all([i[index] == symbol for i in prices_without_tax]), f'{prices_without_tax} - список цен'

    @allure.step('Проверить стиль кнопки добавления в корзину без наведения')
    def check_add_to_cart_css(self):
        """Проверка стилей кнопки добавления в корзину без наведения."""
        elements = self._element(*CataloguePageLocators.ADD_TO_CART_BUTTON, all=True)
        lst = []
        for i in range(len(elements)):
            for prop in ['background-color', 'color', 'font-weight']:
                lst.append(self.get_css_property(*CataloguePageLocators.ADD_TO_CART_BUTTON, prop, i))
            with allure.step(f'Проверить, что background-color - {Colors.GRAY_238}'):
                assert lst[0] == Colors.GRAY_238, f'background-color - {lst[0]}'
            with allure.step(f'Проверить, что color - {Colors.GRAY_136}'):
                assert lst[1] == Colors.GRAY_136, f'color - {lst[1]}'
            with allure.step(f'Проверить, что font-weight - {FontWeight.WEIGHT_700}'):
                assert lst[2] == FontWeight.WEIGHT_700, f'font-weight - {lst[2]}'

    @allure.step('Проверить стиль кнопки добавления в корзину с наведением')
    def check_add_to_cart_css_hover(self):
        """Проверка стилей кнопки добавления в корзину с наведением."""
        elements = self._element(*CataloguePageLocators.ADD_TO_CART_BUTTON, all=True)
        lst = []
        for i in range(len(elements)):
            self.mouse_move_to_element(*CataloguePageLocators.ADD_TO_CART_BUTTON, i)
            for prop in ['color', 'background-color', 'cursor']:
                lst.append(self.get_css_property(*CataloguePageLocators.ADD_TO_CART_BUTTON, prop, i))
            with allure.step(f'Проверить, что color - {Colors.GRAY_68}'):
                assert lst[0] == Colors.GRAY_68, f'color - {lst[0]}'
            with allure.step(f'Проверить, что background-color - {Colors.GRAY_221}'):
                assert lst[1] == Colors.GRAY_221, f'background-color - {lst[1]}'
            with allure.step(f'Проверить, что cursor - {Cursor.POINTER}'):
                assert lst[2] == Cursor.POINTER, f'cursor - {lst[2]}'

    @allure.step('Проверить заголовок страницы каталога')
    def check_catalogue_page_header(self, name):
        """Проверка заголовка страницы каталога.

        :param name: название страницы каталога
        """
        header = self.get_text_of_element(*CataloguePageLocators.CATALOGUE_HEADER)
        with allure.step(f'Проверить что {header} == {name}'):
            allure_helper.attach(self.browser)
            assert name == header, f'Заголовок (ФР) - {header}, name (ОР) - {name}'

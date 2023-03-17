"""Модуль с тестами для страницы Поиска."""

import pytest
import allure

from pages.search_page import SearchPage
from helpers.urls import URLS


@allure.feature('Страница поиска')
@pytest.mark.search_page
class TestSearchPage:
    """Тесты страницы Поиска."""

    @allure.story('Элементы страницы')
    @allure.title('Проверка видимости элементов на странице')
    @allure.link('#', name='User story')
    def test_visibility_of_elements_on_search_page(self, browser, url):
        """Тестовая функция для проверки видимости элементов на странице поиска.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = SearchPage(browser, url)
        page.open_url(path=URLS.SEARCH_PAGE)
        page.check_elements_visibility()

    @allure.story('Работа поиска по сайту')
    @allure.title('Существующий товар во Всех категориях')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('value', ['mac', 'hp'], ids=['mac', 'hp'])
    def test_search_exist_items_in_all_categories(self, browser, url, value):
        """Тестовая функция для проверки результатов поиска
        по существующим товарам во всех категориях.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        :param value: значение, вводимое в строку поиска
        """
        page = SearchPage(browser, url)
        page.open_url(path=URLS.SEARCH_PAGE)
        page.search(value)
        page.is_title_correct(f'Search - {value}')
        page.check_item_from_search_result(value)

    @allure.story('Работа поиска по сайту')
    @allure.title('Несуществующий товар во Всех категориях')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('value', ['123', 'test'], ids=['123', 'test'])
    def test_search_unexist_items_in_all_categories(self, browser, url, value):
        """Тестовая функция для проверки результатов поиска
        по несуществующим товарам во всех категориях.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        :param value: значение, вводимое в строку поиска
        """
        page = SearchPage(browser, url)
        page.open_url(path=URLS.SEARCH_PAGE)
        page.search(value)
        page.is_title_correct(f'Search - {value}')
        page.check_empty_search_result()

    @allure.story('Работа поиска по сайту')
    @allure.title('Существующий товар в категории {categorie}')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('value, categorie',
                             [('mac', 'Desktops'), ('hp', 'Desktops'),
                              ('apple', '      Monitors'), ('samsung', '      Monitors')])
    def test_search_exist_item_in_categorie(self, browser, url, value, categorie):
        """Тестовая функция для проверки результатов поиска
        по существующим товарам в конкретной категории.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        :param value: значение, вводимое в строку поиска
        :param categorie: категория товара в выпадающем списке
        """
        page = SearchPage(browser, url)
        page.open_url(path=URLS.SEARCH_PAGE)
        page.select_category(categorie)
        page.search(value)
        page.is_title_correct(f'Search - {value}')
        page.check_item_from_search_result(value)

    @allure.story('Работа поиска по сайту')
    @allure.title('Несуществующий товар в категории {categorie}')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('value, categorie',
                             [('mac', '      Monitors'), ('samsung', 'Components'), ('lenova', 'Desktops')])
    def test_search_noexist_item_in_categorie(self, browser, url, value, categorie):
        """Тестовая функция для проверки результатов поиска
        по несуществующим товарам в конкретной категории.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        :param value: значение, вводимое в строку поиска
        :param categorie: категория товара в выпадающем списке
        """
        page = SearchPage(browser, url)
        page.open_url(path=URLS.SEARCH_PAGE)
        page.select_category(categorie)
        page.search(value)
        page.is_title_correct(f'Search - {value}')
        page.check_empty_search_result()

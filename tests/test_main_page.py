"""Модуль с тестами для Главной страницы."""

import allure
import pytest

from pages.main_page import MainPage
from pages.product_page import ProductPage



@allure.feature('Главная страница')
@pytest.mark.main_page
class TestMainPage:
    """Тесты главной страницы."""

    @allure.story('Элементы страницы')
    @allure.title('Проверка видимости элементов на странице')
    @allure.link('#', name='User story')
    def test_visibility_of_elements_on_main_page(self, browser, url):
        """Тестовая функция для проверки видимости элементов на Главной странице.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = MainPage(browser, url)
        page.open_url()
        page.check_elements_visibility()

    @allure.story('Элементы страницы')
    @allure.title('Проверка заголовка страницы')
    @allure.link('#', name='User story')
    def test_check_title_on_main_page(self, browser, url):
        """Тестовая функция для проверки корректности заголовка
         на главной странице.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = MainPage(browser, url)
        page.open_url()
        page.is_title_correct('Your Store')

    @allure.story('Проверка смены ротации баннеров и каруселей')
    @allure.title('Проверка смены баннеров по клику на буллеты')
    @allure.link('#', name='User story')
    def test_banners_rotation(self, browser, url):
        """Тестовая функция для проверки смены баннеров
        по клику на кнопки под баннером.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = MainPage(browser, url)
        page.open_url()
        page.click_banner_bullet_active()
        page.click_banner_bullet_inactive()

    @allure.story('Переход на другие страницы')
    @allure.title('Переход к товару с индексом {idx} из Featured')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('idx', [0, 1])
    def test_go_to_product_from_featured(self, browser, url, idx):
        """Тестовая функция для проверки перехода
        в карточку товара по клику из блока Featured.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        :param idx: порядковый индекс элемента
        """
        page = MainPage(browser, url)
        page.open_url()
        name = page.go_to_product_from_featured(idx)
        product_page = ProductPage(browser, browser.current_url)
        product_page.compare_item_title_on_pages(name)

    @allure.story('Проверка смены ротации баннеров и каруселей')
    @allure.title('Проверка смены брендов в карусели по клику на кнопки')
    @allure.link('#', name='User story')
    def test_carousel_rotation(self, browser, url):
        """Тестовая функция для проверки смены брендов в карусели
        по клику на кнопки.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = MainPage(browser, url)
        page.open_url()
        page.click_carousel_bullet()

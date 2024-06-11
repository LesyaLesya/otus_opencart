"""Модуль с тестами для Главной страницы."""

import allure
import pytest

from base.base_test import BaseTest


@allure.feature('Главная страница')
@pytest.mark.main_page
class TestMainPage(BaseTest):
    """Тесты главной страницы."""

    @allure.story('Элементы страницы')
    @allure.title('Проверка видимости элементов на странице')
    @allure.link('#', name='User story')
    def test_visibility_of_elements_on_main_page(self):
        """Тестовая функция для проверки видимости элементов на Главной странице.

        """
        self.main_page.open_url()
        self.main_page.check_elements_visibility()

    @allure.story('Элементы страницы')
    @allure.title('Проверка заголовка страницы')
    @allure.link('#', name='User story')
    def test_check_title_on_main_page(self):
        """Тестовая функция для проверки корректности заголовка
         на главной странице.

        """
        self.main_page.open_url()
        self.main_page.is_title_correct(self.main_page.TITLE)

    @allure.story('Проверка смены ротации баннеров и каруселей')
    @allure.title('Проверка смены баннеров по клику на буллеты')
    @allure.link('#', name='User story')
    def test_banners_rotation(self):
        """Тестовая функция для проверки смены баннеров
        по клику на кнопки под баннером.

        """
        self.main_page.open_url()
        self.main_page.click_banner_bullet_active()
        self.main_page.click_banner_bullet_inactive()

    @allure.story('Переход на другие страницы')
    @allure.title('Переход к товару с индексом {idx} из Featured')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('idx', [0, 1])
    def test_go_to_product_from_featured(self, idx):
        """Тестовая функция для проверки перехода
        в карточку товара по клику из блока Featured.

        :param idx: порядковый индекс элемента
        """
        self.main_page.open_url()
        name = self.main_page.go_to_product_from_featured(idx)
        self.product_page.compare_item_title_on_pages(name)

    @allure.story('Проверка смены ротации баннеров и каруселей')
    @allure.title('Проверка смены брендов в карусели по клику на кнопки')
    @allure.link('#', name='User story')
    def test_carousel_rotation(self):
        """Тестовая функция для проверки смены брендов в карусели
        по клику на кнопки.

        """
        self.main_page.open_url()
        self.main_page.click_carousel_bullet()

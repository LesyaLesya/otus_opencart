"""Модуль с тестами для страницы Товара."""


import allure
import pytest

from helpers.db_helper import check_review_in_db, check_review_not_in_db, check_item_in_wishlist_in_db
from helpers.urls import URLS
from pages.account_page import LoginPage, WishlistPage
from pages.cart_page import CartPage
from pages.comparison_page import ComparisonPage
from pages.product_page import ProductPage


@allure.feature('Страница товара')
@pytest.mark.product_page
class TestProductPage:
    """Тесты страницы товара."""

    @allure.story('Элементы страницы')
    @allure.title('Проверка видимости элементов на странице')
    @allure.link('#', name='User story')
    def test_visibility_of_elements_on_product_page(self, browser, url):
        """Тестовая функция для проверки видимости элементов на странице Товара.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = ProductPage(browser, url)
        page.open_url(path=URLS.PRODUCT_PAGE)
        page.check_elements_visibility()

    @allure.story('Фото товара')
    @allure.title('Открытие главного фото товара по клику')
    @allure.link('#', name='User story')
    def test_open_image_in_window_by_click(self, browser, url):
        """Тестовая функция для проверки открытия фото товара
        во всплывающем окне по клику.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = ProductPage(browser, url)
        page.open_url(path=URLS.PRODUCT_PAGE)
        page.click_main_product_image()
        page.check_main_image_in_window()

    @allure.story('Табы')
    @allure.title('Переход по табам')
    @allure.link('#', name='User story')
    def test_click_on_tabs(self, browser, url):
        """Тестовая функция для проверки перехода по
        табам по клику.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = ProductPage(browser, url)
        page.open_url(path=URLS.PRODUCT_PAGE)
        page.click_on_tab_specification()
        page.click_on_tab_reviews()
        page.click_on_tab_description()

    @allure.story('Добавление товара в Виш-лист')
    @allure.title('Добавление товара в Виш-лист со страницы Товара')
    @allure.link('#', name='User story')
    def test_adding_to_wish_list_from_product(self, browser, url, fixture_create_delete_user, db_connection):
        """Тестовая функция для проверки добавления продукта
        в виш-лист из карточки товара.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        :param fixture_create_delete_user: фикстура создания и удаления тестового пользователя
        """
        email, firstname, lastname, telephone, user_id = fixture_create_delete_user
        page = ProductPage(browser, url)
        page.open_url(path=URLS.PRODUCT_PAGE)
        name, item_id = page.add_to_wishlist()
        page.alert.click_login_from_alert()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_user(email)
        wishlist_page = WishlistPage(browser, browser.current_url)
        wishlist_page.open_wishlist()
        wishlist_page.check_items_in_wish_list(name, 1)
        check_item_in_wishlist_in_db(db_connection, user_id, item_id)

    @allure.story('Добавление товара в сравнение')
    @allure.title('Добавление товара в сравнение из карточки товара')
    @allure.link('#', name='User story')
    def test_adding_to_compare_from_product(self, browser, url):
        """Тестовая функция для проверки добавления продукта
        в сравнение из карточки товара.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = ProductPage(browser, url)
        page.open_url(path=URLS.PRODUCT_PAGE)
        name = page.add_to_compare()
        page.alert.click_link_from_alert()
        compare_page = ComparisonPage(browser, browser.current_url)
        compare_page.check_item_in_comparison(name)

    @allure.story('Добавление товара в корзину')
    @allure.title('Добавление товара в корзину из карточки товара')
    @allure.link('#', name='User story')
    def test_adding_to_cart_from_product(self, browser, url):
        """Тестовая функция для проверки добавления продукта
        в корзину из карточки товара.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = ProductPage(browser, url)
        page.open_url(path=URLS.PRODUCT_PAGE)
        name = page.add_to_cart()
        page.alert.click_link_from_alert()
        cart_page = CartPage(browser, browser.current_url)
        cart_page.check_item_in_cart(name, 1)

    @allure.story('Написание отзыва на товар')
    @allure.title('Написание отзыва на товар из карточки товара')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('name, value, idx',
                             [('TEST1', 'something about the item - good item', 4)])
    def test_write_review(self, browser, url, db_connection, name, value, idx):
        """Тестовая функция для проверки написания отзыва к товару.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        :param db_connection: фикстура коннекта к БД
        :param name: автор отзыва
        :param value: текст отзыва
        :param idx: индекс, соответсвующий рейтингу товара (с 0)
        """
        page = ProductPage(browser, url)
        page.open_url(path=URLS.PRODUCT_PAGE)
        page.write_review(name, value, idx)
        check_review_in_db(db_connection, name, value)

    @allure.story('Инфо блок о товаре')
    @allure.title('Проверка полей инфо блока о товаре')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('path',
                             ['/laptop-notebook/hp-lp3065', '/laptop-notebook/macbook',
                              '/laptop-notebook/macbook-air'])
    def test_check_product_info_block(self, browser, url, path):
        """Проверка полей инфо блока о товаре.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        :param path: urn
        """
        page = ProductPage(browser, url)
        page.open_url(path=path)
        page.check_visibility_of_info_blocks()
        page.check_fields_in_first_info_block()
        page.check_visibility_of_price()
        page.check_fields_in_second_info_block()

    @allure.story('Написание отзыва на товар')
    @allure.title('Нет текста отзыва')
    @allure.link('#', name='User story')
    def test_write_empty_review(self, browser, url, db_connection):
        """Тестовая функция для проверки написания отзыва к товару - без тела отзыва.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        :param db_connection: фикстура коннекта к БД
        """
        name = 'TEST1'
        page = ProductPage(browser, url)
        page.open_url(path=URLS.PRODUCT_PAGE)
        page.write_review(name, '', 4)
        page.alert.check_danger_alert()
        page.alert.check_error_text(page.REVIEW_TEXT_ERROR)
        check_review_not_in_db(db_connection, name, '')

    @allure.story('Написание отзыва на товар')
    @allure.title('Нет автора отзыва')
    @allure.link('#', name='User story')
    def test_write_review_without_author(self, browser, url, db_connection):
        """Тестовая функция для проверки написания отзыва к товару - без автора отзыва.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        :param db_connection: фикстура коннекта к БД
        """
        review = 'Good ithem. I really like it. Great!'
        page = ProductPage(browser, url)
        page.open_url(path=URLS.PRODUCT_PAGE)
        page.write_review('', review, 4)
        page.alert.check_danger_alert()
        page.alert.check_error_text(page.REVIEW_AUTHOR_ERROR)
        check_review_not_in_db(db_connection, '', review)

    @allure.story('Написание отзыва на товар')
    @allure.title('Нет рейтинга отзыва')
    @allure.link('#', name='User story')
    def test_write_review_without_rating(self, browser, url, db_connection):
        """Тестовая функция для проверки написания отзыва к товару - без рейтинга отзыва.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        :param db_connection: фикстура коннекта к БД
        """
        name = 'TEST1'
        review = 'Good ithem. I really like it. Great!'
        page = ProductPage(browser, url)
        page.open_url(path=URLS.PRODUCT_PAGE)
        page.write_review(name, review, None)
        page.alert.check_danger_alert()
        page.alert.check_error_text(page.REVIEW_RATING_ERROR)
        check_review_not_in_db(db_connection, name, review)

"""Модуль с тестами для страницы Товара."""

import allure
import pytest

from base.base_test import BaseTest


@allure.feature('Страница товара')
@pytest.mark.product_page
class TestProductPage(BaseTest):
    """Тесты страницы товара."""

    @allure.story('Элементы страницы')
    @allure.title('Проверка видимости элементов на странице')
    @allure.link('#', name='User story')
    def test_visibility_of_elements_on_product_page(self):
        """Тестовая функция для проверки видимости элементов на странице Товара."""
        self.product_page.open_url()
        self.product_page.check_elements_visibility()

    @allure.story('Фото товара')
    @allure.title('Открытие главного фото товара по клику')
    @allure.link('#', name='User story')
    def test_open_image_in_window_by_click(self):
        """Тестовая функция для проверки открытия фото товара
        во всплывающем окне по клику."""
        self.product_page.open_url()
        self.product_page.click_main_product_image()
        self.product_page.check_main_image_in_window()

    @allure.story('Табы')
    @allure.title('Переход по табам')
    @allure.link('#', name='User story')
    def test_click_on_tabs(self):
        """Тестовая функция для проверки перехода по
        табам по клику."""
        self.product_page.open_url()
        self.product_page.click_on_tab_specification()
        self.product_page.check_tab_specification_active()
        self.product_page.click_on_tab_reviews()
        self.product_page.check_tab_reviews_active()
        self.product_page.click_on_tab_description()
        self.product_page.check_tab_description_active()

    @allure.story('Добавление товара в Виш-лист')
    @allure.title('Добавление товара в Виш-лист со страницы Товара')
    @allure.link('#', name='User story')
    def test_adding_to_wish_list_from_product(self, fixture_create_delete_user):
        """Тестовая функция для проверки добавления продукта
        в виш-лист из карточки товара.

        :param fixture_create_delete_user: фикстура создания и удаления тестового пользователя
        """
        email, firstname, lastname, telephone, user_id = fixture_create_delete_user
        self.product_page.open_url()
        name, item_id = self.product_page.add_to_wishlist()
        self.alert.click_login_from_alert()
        self.login_page.login_user(email)
        self.wishlist_page.open_wishlist()
        self.wishlist_page.check_items_in_wish_list(name, 1)
        self.db.check_item_in_wishlist_in_db(self.db_connection, user_id, item_id)

    @allure.story('Добавление товара в сравнение')
    @allure.title('Добавление товара в сравнение из карточки товара')
    @allure.link('#', name='User story')
    def test_adding_to_compare_from_product(self):
        """Тестовая функция для проверки добавления продукта
        в сравнение из карточки товара.

        """
        self.product_page.open_url()
        name = self.product_page.add_to_compare()
        self.alert.click_link_from_alert()
        self.comparison_page.check_item_in_comparison(name)

    @allure.story('Добавление товара в корзину')
    @allure.title('Добавление товара в корзину из карточки товара')
    @allure.link('#', name='User story')
    def test_adding_to_cart_from_product(self):
        """Тестовая функция для проверки добавления продукта
        в корзину из карточки товара.

        """
        self.product_page.open_url()
        name = self.product_page.add_to_cart()
        self.alert.click_link_from_alert()
        self.cart_page.check_item_in_cart(name, 1)

    @allure.story('Написание отзыва на товар')
    @allure.title('Написание отзыва на товар из карточки товара')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('name, value, idx',
                             [('TEST1', 'something about the item - good item', 4)])
    def test_write_review(self, name, value, idx):
        """Тестовая функция для проверки написания отзыва к товару.

        :param name: автор отзыва
        :param value: текст отзыва
        :param idx: индекс, соответсвующий рейтингу товара (с 0)
        """
        self.product_page.open_url()
        self.product_page.write_review(name, value, idx)
        self.db.check_review_in_db(self.db_connection, name, value)

    @allure.story('Инфо блок о товаре')
    @allure.title('Проверка полей инфо блока о товаре')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('path',
                             ['/laptop-notebook/hp-lp3065', '/laptop-notebook/macbook',
                              '/laptop-notebook/macbook-air'])
    def test_check_product_info_block(self, path):
        """Проверка полей инфо блока о товаре.

        """
        self.product_page.change_link_path(path)
        self.product_page.open_url()
        self.product_page.check_visibility_of_info_blocks()
        self.product_page.check_fields_in_first_info_block()
        self.product_page.check_visibility_of_price()
        self.product_page.check_fields_in_second_info_block()

    @allure.story('Написание отзыва на товар')
    @allure.title('Нет текста отзыва')
    @allure.link('#', name='User story')
    def test_write_empty_review(self):
        """Тестовая функция для проверки написания отзыва к товару - без тела отзыва.
        """
        name = 'TEST1'
        self.product_page.open_url()
        self.product_page.write_review(name, '', 4)
        self.alert.check_danger_alert()
        self.alert.check_error_text(self.product_page.REVIEW_TEXT_ERROR)
        self.db.check_review_not_in_db(self.db_connection, name, '')

    @allure.story('Написание отзыва на товар')
    @allure.title('Нет автора отзыва')
    @allure.link('#', name='User story')
    def test_write_review_without_author(self):
        """Тестовая функция для проверки написания отзыва к товару - без автора отзыва.
        """
        review = 'Good ithem. I really like it. Great!'
        self.product_page.open_url()
        self.product_page.write_review('', review, 4)
        self.alert.check_danger_alert()
        self.alert.check_error_text(self.product_page.REVIEW_AUTHOR_ERROR)
        self.db.check_review_not_in_db(self.db_connection, '', review)

    @allure.story('Написание отзыва на товар')
    @allure.title('Нет рейтинга отзыва')
    @allure.link('#', name='User story')
    def test_write_review_without_rating(self):
        """Тестовая функция для проверки написания отзыва к товару - без рейтинга отзыва.
        """
        name = 'TEST1'
        review = 'Good ithem. I really like it. Great!'
        self.product_page.open_url()
        self.product_page.write_review(name, review, None)
        self.alert.check_danger_alert()
        self.alert.check_error_text(self.product_page.REVIEW_RATING_ERROR)
        self.db.check_review_not_in_db(self.db_connection, name, review)

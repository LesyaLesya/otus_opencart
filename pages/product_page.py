"""Модуль c методами для страницы Каталога."""


import allure

from helpers.locators import ProductPageLocators
from pages.base_page import BasePage


class ProductPage(BasePage):
    """Класс с методами для страницы Товара."""

    TAX = 'Ex Tax:'
    AVAIL = 'Availability:'
    REWARD = 'Reward Points:'
    CODE = 'Product Code:'
    BRAND = 'Brand:'
    REVIEW_TEXT_ERROR = 'Warning: Review Text must be between 25 and 1000 characters!'
    REVIEW_AUTHOR_ERROR = 'Warning: Review Name must be between 3 and 25 characters!'
    REVIEW_RATING_ERROR = 'Warning: Please select a review rating!'

    @allure.step('Проверить видимость элементов на странице')
    def check_elements_visibility(self):
        """Проверка видимости элементов."""
        lst = [ProductPageLocators.PRODUCT_HEADER,
               ProductPageLocators.BUTTON_CART,
               ProductPageLocators.IMAGES_BLOCK,
               ProductPageLocators.RATING_BLOCK,
               ProductPageLocators.PRODUCT_DESCRIPTION]
        for i in lst:
            self.is_element_visible(*i)

    @allure.step('Кликнуть по главному фото товара')
    def click_main_product_image(self):
        """Клик по главной фото товара."""
        self.click_on_element(*ProductPageLocators.MAIN_PRODUCT_IMAGE)

    @allure.step('Проверить, что фото открылось во всплывающем окне')
    def check_main_image_in_window(self):
        """Проверка, что картинка открывается в окне по клику."""
        self.is_element_visible(*ProductPageLocators.PRODUCT_IMAGE_IN_WINDOW)

    @allure.step('Перейти на таб Specification')
    def click_on_tab_specification(self):
        """Клик по табу Specification."""
        self.click_on_element(*ProductPageLocators.TAB_SPECIFICATION_LINK)
        with allure.step('Проверить, что таб Specification активирован'):
            assert self.getting_attr(
                'class', *ProductPageLocators.TAB_CLASS, 1) == 'active',\
                'Таб Specification не активирован'

    @allure.step('Перейти на таб Reviews')
    def click_on_tab_reviews(self):
        """Клик по табу Reviews."""
        self.click_on_element(*ProductPageLocators.TAB_REVIEWS_LINK)
        with allure.step('Проверить, что таб Reviews активирован'):
            assert self.getting_attr('class', *ProductPageLocators.TAB_CLASS, 2) == 'active',\
                'Таб Reviews не активирован'

    @allure.step('Перейти на таб Description')
    def click_on_tab_description(self):
        """Клик по табу Description."""
        self.click_on_element(*ProductPageLocators.TAB_DESCRIPTION_LINK)
        with allure.step('Проверить, что таб Description активирован'):
            assert self.getting_attr(
                'class', *ProductPageLocators.TAB_CLASS, 0) == 'active',\
                'Таб Description не активирован'

    @allure.step('Проверить заголовок товара - {name}')
    def compare_item_title_on_pages(self, name):
        """Получам название товара полученное по переданному селектору и
        сравниваем название товара на страницах.

        :param name: название товара
        """
        name_on_product_page = self.get_text_of_element(*ProductPageLocators.ITEM_TITLE)
        with allure.step(f'Проверить, что название в карточке {name_on_product_page} совпадает с {name}'):
            assert name == name_on_product_page,  \
                f'Название - {name}, в карточке товара - {name_on_product_page}'

    @allure.step('Добавить товар в вишлист')
    def add_to_wishlist(self):
        """Добавление товара в вишлист. Возвращает название
        добавленного товара.
        """
        name = self.get_text_of_element(*ProductPageLocators.ITEM_TITLE)
        item_id = self.get_item_id(*ProductPageLocators.WISH_LIST_BUTTON)
        self.click_on_element(*ProductPageLocators.WISH_LIST_BUTTON)
        return name, item_id

    @allure.step('Добавить товар в сравнение')
    def add_to_compare(self):
        """Добавление товара в сравнение. Возвращает название
        добавленного товара.
        """
        name = self.get_text_of_element(*ProductPageLocators.ITEM_TITLE)
        self.click_on_element(*ProductPageLocators.COMPARE_BUTTON)
        return name

    @allure.step('Добавить товар в корзину')
    def add_to_cart(self):
        """Добавление товара в корзину. Возвращает название
        добавленного товара.
        """
        name = self.get_text_of_element(*ProductPageLocators.ITEM_TITLE)
        self.click_on_element(*ProductPageLocators.BUTTON_CART)
        return name

    @allure.step('Написать отзыв на товар: автор {name}, отзыв {value}, индекс оценки {idx}')
    def write_review(self, name, value, idx):
        """После заполнения полей и отправки формы возвращаются имя автора и текст отзыва.

        :param name: имя автора
        :param value: текст отзыва
        :param idx: индекс оценки
        """
        self.click_on_element(*ProductPageLocators.WRITE_REVIEW_BUTTON)
        self.input_text(*ProductPageLocators.REVIEW_NAME_FIELD, name)
        self.input_text(*ProductPageLocators.REVIEW_FIELD, value)
        if idx:
            self.click_on_element(*ProductPageLocators.RATING_RADIO_BUTTON, idx)
        self.click_on_element(*ProductPageLocators.REVIEW_BUTTON)

    @allure.step('Проверить наличие блоков с информацией')
    def check_visibility_of_info_blocks(self):
        """Проверить наличие блоков с информацией."""
        self.is_element_visible(*ProductPageLocators.RIGHT_BLOCK_INFO, index=0)
        self.is_element_visible(*ProductPageLocators.RIGHT_BLOCK_INFO, index=1)

    @allure.step('Проверить поля в первом инфоблоке')
    def check_fields_in_first_info_block(self):
        """Проверить поля в первом инфоблоке."""
        brand = self.get_text_of_element(*ProductPageLocators.ELEMENTS_OF_RIGHT_BLOCK_INFO_FIRST, index=0)
        with allure.step(f'Проверить, что бренда {brand} начинается с {self.BRAND}'):
            assert brand.startswith(self.BRAND), f'Инфа о бренде - {brand}'

        product_code = self.get_text_of_element(*ProductPageLocators.ELEMENTS_OF_RIGHT_BLOCK_INFO_FIRST, index=1)
        with allure.step(f'Проверить, что код продукта {product_code} начинается с {self.CODE}'):
            assert product_code.startswith(self.CODE), f'Инфа о коде - {product_code}'

        reward = self.get_text_of_element(*ProductPageLocators.ELEMENTS_OF_RIGHT_BLOCK_INFO_FIRST, index=2)
        with allure.step(f'Проверить, что поле награды {reward} начинается с {self.REWARD}'):
            assert reward.startswith(self.REWARD), f'Инфа о награде - {reward}'

        availability = self.get_text_of_element(*ProductPageLocators.ELEMENTS_OF_RIGHT_BLOCK_INFO_FIRST, index=3)
        with allure.step(f'Проверить, что поле доступности {availability} начинается с {self.AVAIL}'):
            assert availability.startswith(self.AVAIL), f'Инфа о доступности - {availability}'

    @allure.step('Проверить наличие цены')
    def check_visibility_of_price(self):
        """Проверить наличие цены."""
        self.is_element_visible(*ProductPageLocators.PRODUCT_PRICE)

    @allure.step('Проверить поля во втором инфоблоке')
    def check_fields_in_second_info_block(self):
        """Проверить поля в первом инфоблоке."""
        tax = self.get_text_of_element(*ProductPageLocators.ELEMENTS_OF_RIGHT_BLOCK_INFO_SECOND, index=1)
        with allure.step(f'Проверить, что поле пошлины {tax} начинается с {self.TAX}'):
            assert tax.startswith(self.TAX), f'Инфа о пошлине - {tax}'

"""Модуль c методами для страницы Каталога."""


import allure
import time
from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from helpers import test_data


class ProductPage(BasePage):
    """Класс с методами для страницы Товара."""

    @allure.step("Кликнуть по главному фото товара")
    def click_main_product_image(self):
        """Клик по главной фото товара."""

        self.click_on_element(*ProductPageLocators.MAIN_PRODUCT_IMAGE)
        return self

    @allure.step("Проверить, что фото открылось во всплывающем окне")
    def get_main_image_in_window(self):
        """Проверка, что картинка открывается в окне по клику."""

        self.is_element_visible(*ProductPageLocators.PRODUCT_IMAGE_IN_WINDOW)
        return self

    @allure.step("Перейти на таб Specification")
    def click_on_tab_specification(self):
        """Клик по табу Specification."""

        with allure.step("Кликнуть по табу Specification"):
            self.click_on_element(*ProductPageLocators.TAB_SPECIFICATION_LINK)
        with allure.step("Проверить, что таб Specification активирован"):
            assert self.getting_attr("class",
                                     *ProductPageLocators.TAB_CLASS, 1) == "active",\
                "Таб Specification не активирован"

    @allure.step("Перейти на таб Reviews")
    def click_on_tab_reviews(self):
        """Клик по табу Reviews."""

        with allure.step("Кликнуть по табу Reviews"):
            self.click_on_element(*ProductPageLocators.TAB_REVIEWS_LINK)
        with allure.step("Проверить, что таб Reviews активирован"):
            assert self.getting_attr("class", *ProductPageLocators.TAB_CLASS, 2) == "active",\
                "Таб Reviews не активирован"

    @allure.step("Перейти на таб Description")
    def click_on_tab_description(self):
        """Клик по табу Description."""

        with allure.step("Кликнуть по табу Description"):
            self.click_on_element(*ProductPageLocators.TAB_DESCRIPTION_LINK)
        with allure.step("Проверить, что таб Description активирован"):
            assert self.getting_attr("class",
                                     *ProductPageLocators.TAB_CLASS, 0) == "active",\
                "Таб Description не активирован"

    @allure.step("Проверить заголовок товара")
    def compare_item_title_on_pages(self, name):
        """Получам название товара полученное по переданному селектору и
        сравниваем название товара на страницах."""

        name_on_product_page = self.get_text_of_element(*ProductPageLocators.ITEM_TITLE)
        assert name == name_on_product_page,  \
            f"Название - {name}, в карточке товара - {name_on_product_page}"

    def add_to_wishlist(self):
        """Добавление товара в вишлист. Возвращает название
        добавленного товара.
        """

        with allure.step(f"Получить название товара"):
            name = self.get_text_of_element(*ProductPageLocators.ITEM_TITLE)
        with allure.step(f"Кликнуть на кнопку добавления в Виш-лист"):
            self.click_on_element(*ProductPageLocators.WISH_LIST_BUTTON)
        return name

    @allure.step("Кликнуть на кнопку Логина в алерте")
    def click_login_from_alert(self):
        """Клик по кнопке Логина в алерте."""

        self.click_on_element(*ProductPageLocators.LINK_LOGIN_ALERT)
        return self

    def add_to_compare(self):
        """Добавление товара в сравнение. Возвращает название
        добавленного товара.
        """

        with allure.step(f"Получить название товара"):
            name = self.get_text_of_element(*ProductPageLocators.ITEM_TITLE)
        with allure.step(f"Кликнуть на кнопку добавления в сравнение"):
            self.click_on_element(*ProductPageLocators.COMPARE_BUTTON)
        return name

    @allure.step("Кликнуть на кнопку Сравнения в алерте")
    def click_compare_from_alert(self):
        """Клик по кнопке Сравнения в алерте."""

        return self.click_on_element(*ProductPageLocators.LINK_COMPARE_ALERT)

    def add_to_cart(self):
        """Добавление товара в корзину. Возвращает название
        добавленного товара.
        """

        with allure.step(f"Получить название товара"):
            name = self.get_text_of_element(*ProductPageLocators.ITEM_TITLE)
        with allure.step(f"Кликнуть на кнопку добавления в корзину"):
            self.click_on_element(*ProductPageLocators.BUTTON_CART)
        return name

    @allure.step("Кликнуть на кнопку Корзины в алерте")
    def click_cart_from_alert(self):
        """Клик по кнопке Корзины в алерте."""

        self.click_on_element(*ProductPageLocators.LINK_CART_ALERT)
        return self

    @allure.step("Написать отзыв на товар")
    def write_review(self, name, value, idx):
        """ После заполнения полей и отправки формы возвращаются имя автора и текст отзыва. """

        with allure.step("Нажать на кнопку написания отзыва"):
            self.click_on_element(*ProductPageLocators.WRITE_REVIEW_BUTTON)
        with allure.step(f"Заполнить имя автора - {name}"):
            self.input_text(*ProductPageLocators.REVIEW_NAME_FIELD, name)
        with allure.step(f"Заполнить текст отзыва - {value}"):
            self.input_text(*ProductPageLocators.REVIEW_FIELD, value)
        if idx:
            with allure.step("Выбрать оценку"):
                self.click_on_element(*ProductPageLocators.RATING_RADIO_BUTTON, idx)
        with allure.step("Нажать на кнопку отправки отзыва"):
            self.click_on_element(*ProductPageLocators.REVIEW_BUTTON)
        return self

    def check_review_in_db(self, author, text):
        self.__get_review_from_db(author, text)
        self.__del_review_from_bd(author, text)

    @allure.step("Проверить, что ревью НЕ появилось в БД")
    def check_review_not_in_db(self, author, text):
        """ Проверить, что ревью НЕ появилось в БД. """

        result = test_data.get_review(self.browser.db, author, text)
        time.sleep(1)
        with allure.step(f"Проверяем, что запись об отзыве НЕ создана в БД "):
            if result == 0:
                assert True
            else:
                assert False, f"Записей найдено - {result}"

    @allure.step("Проверить, что ревью появилось в БД")
    def __get_review_from_db(self, author, text):
        """ Проверка, сколько записей возвращается по заданному условию. """

        result = test_data.get_review(self.browser.db, author, text)
        time.sleep(1)
        with allure.step(f"Проверяем, что запись об отзыве создана в БД "):
            if result > 0:
                assert True
            else:
                assert False, f"Записи не найдены - {result}"

    @allure.step("Удалить ревью из БД")
    def __del_review_from_bd(self, author, text):
        """ Возвращает удаление отзыва из БД. """

        return test_data.delete_review(self.browser.db, author, text)

    @allure.step("Сравнить тайтл страницы и заголовок товара")
    def compare_page_title_and_item_title(self):
        """Сравнить тайтл страницы и заголовок товара."""

        name_on_product_page = (self.get_text_of_element(*ProductPageLocators.ITEM_TITLE)).lower()
        name_in_title = (self.get_title()).lower()
        assert name_on_product_page == name_in_title, \
            f"Название товара - {name_on_product_page}, заголовок - {name_in_title}"

    @allure.step("Проверить наличие блоков с информацией")
    def check_visibility_of_info_blocks(self):
        """Проверить наличие блоков с информацией."""

        assert self.is_element_visible(*ProductPageLocators.RIGHT_BLOCK_INFO, index=0)
        assert self.is_element_visible(*ProductPageLocators.RIGHT_BLOCK_INFO, index=1)

    @allure.step("Проверить поля в первом инфоблоке")
    def check_fields_in_first_info_block(self):
        """Проверить поля в первом инфоблоке."""

        self.__check_brand_fields_in_first_info_block()
        self.__check_product_code_fields_in_first_info_block()
        self.__check_reward_fields_in_first_info_block()
        self.__check_availability_fields_in_first_info_block()

    @allure.step("Проверить поле бренд")
    def __check_brand_fields_in_first_info_block(self):
        """Проверить поле бренд."""

        brand = self.get_text_of_element(*ProductPageLocators.ELEMENTS_OF_RIGHT_BLOCK_INFO_FIRST, index=0)
        assert brand.startswith('Brand:'), f'Инфа о бренде - {brand}'

    @allure.step("Проверить поле кода продута")
    def __check_product_code_fields_in_first_info_block(self):
        """Проверить поле кода продута."""

        product_code = self.get_text_of_element(*ProductPageLocators.ELEMENTS_OF_RIGHT_BLOCK_INFO_FIRST, index=1)
        assert product_code.startswith('Product Code:'), f'Инфа о коде - {product_code}'

    @allure.step("Проверить поле награды")
    def __check_reward_fields_in_first_info_block(self):
        """Проверить поле награды."""

        reward = self.get_text_of_element(*ProductPageLocators.ELEMENTS_OF_RIGHT_BLOCK_INFO_FIRST, index=2)
        assert reward.startswith('Reward Points:'), f'Инфа о награде - {reward}'

    @allure.step("Проверить поле доступности")
    def __check_availability_fields_in_first_info_block(self):
        """Проверить поле доступности."""

        availability = self.get_text_of_element(*ProductPageLocators.ELEMENTS_OF_RIGHT_BLOCK_INFO_FIRST, index=3)
        assert availability.startswith('Availability:'), f'Инфа о доступности - {availability}'

    @allure.step("Проверить наличие цены")
    def check_visibility_of_price(self):
        """Проверить наличие цены."""

        assert self.is_element_visible(*ProductPageLocators.PRODUCT_PRICE)

    @allure.step("Проверить поля во втором инфоблоке")
    def check_fields_in_second_info_block(self):
        """Проверить поля в первом инфоблоке."""

        self.__check_tax_fields_in_second_info_block()

    @allure.step("Проверить поле пошлины")
    def __check_tax_fields_in_second_info_block(self):
        """Проверить поле пошлины."""

        tax = self.get_text_of_element(*ProductPageLocators.ELEMENTS_OF_RIGHT_BLOCK_INFO_SECOND, index=1)
        assert tax.startswith('Ex Tax:'), f'Инфа о пошлине - {tax}'

    @allure.step("Проверить алерт при пустом отзыве")
    def check_error_visibility_review(self):
        """Проверить алерт при пустом отзыве."""

        assert self.is_element_visible(*ProductPageLocators.REVIEW_ALERT)

    @allure.step("Проверить сообщение об ошибке при пустом отзыве")
    def check_error_text_empty_review(self):
        """Проверить сообщение об ошибке при пустом отзыве."""

        error_text = self.get_text_of_element(*ProductPageLocators.REVIEW_ALERT)
        assert error_text == 'Warning: Review Text must be between 25 and 1000 characters!', \
            f'Текст ошибки {error_text}'

    @allure.step("Проверить сообщение об ошибке при пустом авторе отзыва")
    def check_error_text_empty_author_review(self):
        """Проверить сообщение об ошибке при пустом авторе отзыва."""

        error_text = self.get_text_of_element(*ProductPageLocators.REVIEW_ALERT)
        assert error_text == 'Warning: Review Name must be between 3 and 25 characters!', \
            f'Текст ошибки {error_text}'

    @allure.step("Проверить сообщение об ошибке при пустом рейтинге отзыва")
    def check_error_text_empty_rating_review(self):
        """Проверить сообщение об ошибке при пустом рейтинге отзыва."""

        error_text = self.get_text_of_element(*ProductPageLocators.REVIEW_ALERT)
        assert error_text == 'Warning: Please select a review rating!', \
            f'Текст ошибки {error_text}'

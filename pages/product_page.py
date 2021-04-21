"""Модуль c методами для страницы Каталога."""


import allure
from pages.base_page import BasePage
from pages.locators import ProductPageLocators


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

        return self.click_on_element(*ProductPageLocators.LINK_LOGIN_ALERT)

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

        return self.click_on_element(*ProductPageLocators.LINK_CART_ALERT)

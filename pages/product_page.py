"""Модуль c методами для страницы Каталога."""


import allure
from otus_opencart.pages.base_page import BasePage
from otus_opencart.pages.locators import ProductPageLocators


class ProductPage(BasePage):
    """Класс с методами для страницы Товара."""

    @allure.step("Кликнуть по главному фото товара")
    def click_main_product_image(self):
        """Клик по главной фото товара."""

        self.click_on_element(*ProductPageLocators.MAIN_PRODUCT_IMAGE)

    @allure.step("Проверить, что фото открылось во всплывающем окне")
    def get_main_image_in_window(self):
        """Проверка, что картинка открывается в окне по клику."""

        self.is_element_visible(*ProductPageLocators.PRODUCT_IMAGE_IN_WINDOW)

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

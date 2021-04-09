"""Модуль c методами для Главной страницы."""

import allure
from otus_opencart.pages.base_page import BasePage
from otus_opencart.pages.locators import MainPageLocators


class MainPage(BasePage):
    """Класс с методами для  Главной страницы."""

    @allure.step("Кликнуть по выбранной кнопке под баннером")
    def click_banner_bullet_active(self):
        """Клик по выбранной кнопке переключения баннера."""

        if self.is_element_visible(*MainPageLocators.BANNER_IPHONE):
            if self.getting_attr("class", *MainPageLocators.BANNER_BULLET, 0) == \
                    "swiper-pagination-bullet swiper-pagination-bullet-active":
                self.click_on_element(*MainPageLocators.BANNER_BULLET, 0)
                self.is_element_visible(*MainPageLocators.BANNER_IPHONE)
            else:
                raise AssertionError(
                    f'Класс элемента {self.getting_attr("class", *MainPageLocators.BANNER_BULLET, 0)}')
        else:
            if self.getting_attr("class", *MainPageLocators.BANNER_BULLET, 1) == \
                    "swiper-pagination-bullet swiper-pagination-bullet-active":
                self.click_on_element(*MainPageLocators.BANNER_BULLET, 1)
                self.is_element_visible(*MainPageLocators.BANNER_MACBOOK)
            else:
                raise AssertionError(
                    f'Класс элемента {self.getting_attr("class", *MainPageLocators.BANNER_BULLET, 1)}')

    @allure.step("Кликнуть по невыбранной кнопке под баннером")
    def click_banner_bullet_inactive(self):
        """Клик по невыбранной кнопке переключения баннера."""

        if self.is_element_visible(*MainPageLocators.BANNER_IPHONE):
            if self.getting_attr("class", *MainPageLocators.BANNER_BULLET, 0) == \
                    "swiper-pagination-bullet swiper-pagination-bullet-active":
                self.click_on_element(*MainPageLocators.BANNER_BULLET, 1)
                self.is_element_visible(*MainPageLocators.BANNER_MACBOOK)
            else:
                raise AssertionError(
                    f'Класс элемента {self.getting_attr("class", *MainPageLocators.BANNER_BULLET, 0)}')
        else:
            if self.getting_attr("class", *MainPageLocators.BANNER_BULLET, 1) == \
                    "swiper-pagination-bullet swiper-pagination-bullet-active":
                self.click_on_element(*MainPageLocators.BANNER_BULLET, 0)
                self.is_element_visible(*MainPageLocators.BANNER_IPHONE)
            else:
                raise AssertionError(
                    f'Класс элемента {self.getting_attr("class", *MainPageLocators.BANNER_BULLET, 1)}')

    def go_to_product_from_featured(self, index):
        """Клик по товару из блока FEATURED.
        Возвращает название товара.

        :param index: порядковый индекс элемента
        """

        with allure.step(f"Проверить видимость товара с индексом {index}"):
            self.is_element_visible(*MainPageLocators.FEATURED_PRODUCT_LINK, index)
        with allure.step(f"Получить название товара с индексом {index}"):
            name = self.get_text_of_element(*MainPageLocators.FEATURED_PRODUCT_NAME, index)
        with allure.step(f"Кликнуть по превью товара с индексом {index}"):
            self.click_on_element(*MainPageLocators.FEATURED_PRODUCT_LINK, index)
        return name

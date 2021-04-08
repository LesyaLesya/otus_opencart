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

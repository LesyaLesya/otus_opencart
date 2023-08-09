"""Модуль c методами для Главной страницы."""

import allure

from helpers import allure_helper
from helpers.locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    """Класс с методами для Главной страницы."""

    TITLE = 'Your Store'

    @allure.step('Проверить видимость элементов на странице')
    def check_elements_visibility(self):
        """Проверка видимости элементов."""
        lst = [MainPageLocators.BANNER,
               MainPageLocators.BANNER_PAGINATION_BULLETS,
               MainPageLocators.HEADER_FEATURED,
               MainPageLocators.CAROUSEL_BRAND,
               MainPageLocators.CAROUSEL_PAGINATION_BULLETS]
        for i in lst:
            self.is_element_visible(*i)

    @allure.step('Кликнуть по выбранной кнопке под баннером')
    def click_banner_bullet_active(self):
        """Клик по выбранной кнопке переключения баннера."""
        if self.getting_attr('class', *MainPageLocators.BANNER_BULLET, 0) == \
                    'swiper-pagination-bullet swiper-pagination-bullet-active':
            self.click_on_element(*MainPageLocators.BANNER_BULLET, 0)
            self.is_element_visible(*MainPageLocators.BANNER_IPHONE)
        elif self.getting_attr('class', *MainPageLocators.BANNER_BULLET, 1) == \
                    'swiper-pagination-bullet swiper-pagination-bullet-active':
            self.click_on_element(*MainPageLocators.BANNER_BULLET, 1)
            self.is_element_visible(*MainPageLocators.BANNER_MACBOOK)

    @allure.step('Кликнуть по невыбранной кнопке под баннером')
    def click_banner_bullet_inactive(self):
        """Клик по невыбранной кнопке переключения баннера."""
        if self.getting_attr('class', *MainPageLocators.BANNER_BULLET, 0) == \
                    'swiper-pagination-bullet swiper-pagination-bullet-active':
            self.click_on_element(*MainPageLocators.BANNER_BULLET, 1)
            self.is_element_visible(*MainPageLocators.BANNER_MACBOOK)
        elif self.getting_attr('class', *MainPageLocators.BANNER_BULLET, 1) == \
                    'swiper-pagination-bullet swiper-pagination-bullet-active':
            self.click_on_element(*MainPageLocators.BANNER_BULLET, 0)
            self.is_element_visible(*MainPageLocators.BANNER_IPHONE)

    @allure.step('Кликнуть по товару с индексом {index} в блоке Featured')
    def go_to_product_from_featured(self, index):
        """Клик по товару из блока FEATURED.
        Возвращает название товара.

        :param index: порядковый индекс элемента
        """
        name = self.get_text_of_element(*MainPageLocators.FEATURED_PRODUCT_NAME, index)
        self.click_on_element(*MainPageLocators.FEATURED_PRODUCT_LINK, index)
        return name

    @allure.step('Кликнуть по кнопкам переключения карусели брендов')
    def click_carousel_bullet(self):
        """Клик по кнопкам переключения карусели."""
        with allure.step('Получить все элементы из карусели'):
            elements = self._element_presence(*MainPageLocators.BRAND_IMAGE_IN_CAROUSEL, all=True)
        with allure.step('Кликнуть поочереди по кнопкам карусели'):
            for i in range(11):
                with allure.step(f'Кликнуть на кнопку с индексом {i}'):
                    self.click_on_element(*MainPageLocators.CAROUSEL_PAGINATION_BULLET, i)
                    for k in elements:
                        with allure.step('Получить значение атрибута data-swiper-slide-index'):
                            attr = k.get_attribute('data-swiper-slide-index')
                            with allure.step(f'Проверить, что атрибут {attr} равен {i}'):
                                if attr == str(i):
                                    with allure.step('Получить список атрибутов класса элемента'):
                                        actual_class = k.get_attribute('class').split()
                                        with allure.step(f'Проверить, что классы swiper-slide-active или swiper-slide-duplicate-active есть в {actual_class}'):
                                            allure_helper.attach(self.browser)
                                            assert 'swiper-slide-active' or 'swiper-slide-duplicate-active' \
                                                   in actual_class, f'Класс - {actual_class}'
                                        break

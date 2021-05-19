"""Модуль c методами для Главной страницы."""

import allure
from pages.base_page import BasePage
from pages.locators import MainPageLocators


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
                return self
            else:
                raise AssertionError(
                    f'Класс элемента {self.getting_attr("class", *MainPageLocators.BANNER_BULLET, 0)}')
        else:
            if self.getting_attr("class", *MainPageLocators.BANNER_BULLET, 1) == \
                    "swiper-pagination-bullet swiper-pagination-bullet-active":
                self.click_on_element(*MainPageLocators.BANNER_BULLET, 1)
                self.is_element_visible(*MainPageLocators.BANNER_MACBOOK)
                return self
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
                return self
            else:
                raise AssertionError(
                    f'Класс элемента {self.getting_attr("class", *MainPageLocators.BANNER_BULLET, 0)}')
        else:
            if self.getting_attr("class", *MainPageLocators.BANNER_BULLET, 1) == \
                    "swiper-pagination-bullet swiper-pagination-bullet-active":
                self.click_on_element(*MainPageLocators.BANNER_BULLET, 0)
                self.is_element_visible(*MainPageLocators.BANNER_IPHONE)
                return self
            else:
                raise AssertionError(
                    f'Класс элемента {self.getting_attr("class", *MainPageLocators.BANNER_BULLET, 1)}')

    def go_to_product_from_featured(self, index):
        """Клик по товару из блока FEATURED.
        Возвращает название товара.

        :param index: порядковый индекс элемента
        """

        with allure.step(f"Получить название товара с индексом {index}"):
            name = self.get_text_of_element(*MainPageLocators.FEATURED_PRODUCT_NAME, index)
        with allure.step(f"Кликнуть по превью товара с индексом {index}"):
            self.click_on_element(*MainPageLocators.FEATURED_PRODUCT_LINK, index)
        return name

    @allure.step("Кликнуть по кнопкам переключения карусели брендов")
    def click_carousel_bullet(self):
        """Клик по кнопкам переключения карусели."""

        with allure.step("Получаем все элементы из карусели"):
            elements = self._element(*MainPageLocators.BRAND_IMAGE_IN_CAROUSEL, all=True)
        with allure.step("Кликаем поочереди по кнопкам карусели"):
            for i in range(11):
                with allure.step(f"Кликаем на кнопку с индексом {i}"):
                    self.click_on_element(*MainPageLocators.CAROUSEL_PAGINATION_BULLET, i)
                    for k in elements:
                        with allure.step("Получаем значение атрибута data-swiper-slide-index"):
                            attr = k.get_attribute("data-swiper-slide-index")
                            with allure.step(f"Проверяем, что атрибут {attr} равен {i}"):
                                if attr == str(i):
                                    with allure.step("Получаем список атрибутов класса элемента"):
                                        actual_class = k.get_attribute("class").split()
                                        with allure.step(f"Проверяем классы {actual_class}"):
                                            assert "swiper-slide-active" or "swiper-slide-duplicate-active" \
                                                   in actual_class, f"Класс - {actual_class}"
                                        break

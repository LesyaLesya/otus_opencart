"""Модуль c методами для страницы Сравнение товара."""

import allure

from helpers.locators import ComparePageLocators
from pages.base_page import BasePage


class ComparisonPage(BasePage):
    """Класс с методами для страницы сравнения товаров."""

    @allure.step('Проверить, что товар в сравнении')
    def check_item_in_comparison(self, name):
        """Проверка видимости товара в сравнении.

        :param name: название товара
        """
        name_in_comparison = self.get_text_of_element(*ComparePageLocators.ITEM_NAMES)
        with allure.step(f'Проверить что все товары {name_in_comparison} содержат название {name}'):
            assert name == name_in_comparison, \
                f'Название {name}, название в сравнении {name_in_comparison}'

    @allure.step('Удалить все товары из сравнения')
    def del_from_compare(self):
        """Удаление всех товаров из сравнения."""
        elements = self._element(*ComparePageLocators.REMOVE_BUTTON, all=True)
        for i in range(len(elements)):
            self.click_on_element(*ComparePageLocators.REMOVE_BUTTON, i)

    @allure.step('Проверить видимость успешного алерта')
    def check_success_alert(self):
        """Вывод успешного алерта."""
        self.is_element_visible(*ComparePageLocators.ALERT_SUCCESS)

    @allure.step('Проверить текст на пустой странице Сравнения')
    def check_empty_compare(self):
        """Проверка текста при отсутсвии товаров в сравнении."""
        txt = self.get_text_of_element(*ComparePageLocators.TEXT_FOR_EMTY_COMPARE)
        with allure.step('Проверить, что текст - You have not chosen any products to compare.'):
            assert txt == 'You have not chosen any products to compare.', f'Текст - {txt}'

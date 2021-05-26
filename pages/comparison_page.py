"""Модуль c методами для страницы Сравнение товара."""

import allure
from pages.base_page import BasePage
from pages.locators import ComparePageLocators


class ComparisonPage(BasePage):
    """Класс с методами для страницы сравнения товаров."""

    @allure.step("Проверить, что товар в сравнении")
    def check_item_in_comparison(self, name):
        """Проверка видимости товара в сравнении."""

        name_in_comparison = self.get_text_of_element(*ComparePageLocators.ITEM_NAMES)
        assert name == name_in_comparison, \
            f"Название {name}, название в сравнении {name_in_comparison}"

    @allure.step("Удалить все товары из сравнения")
    def del_from_compare(self):
        """Удаление всех товаров из сравнения."""

        elements = self._element(*ComparePageLocators.REMOVE_BUTTON, all=True)
        for i in range(len(elements)):
            self.click_on_element(*ComparePageLocators.REMOVE_BUTTON, i)
            self.should_be_success_alert()

    @allure.step("Проверить видимость успешного алерта")
    def should_be_success_alert(self):
        """Вывод успешного алерта."""

        self.is_element_visible(*ComparePageLocators.ALERT_SUCCESS)
        return self

    @allure.step("Проверить текст на пустой странице Сравнения")
    def should_be_empty_compare(self):
        """Проверка текста при отсутсвии товаров в сравнении."""

        txt = self.get_text_of_element(*ComparePageLocators.TEXT_FOR_EMTY_COMPARE)
        assert txt == 'You have not chosen any products to compare.', f'Текст - {txt}'

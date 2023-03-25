"""Модуль c методами для Подвала сайта."""


import allure

from helpers import allure_helper
from helpers.locators import FooterPageLocators
from pages.base_page import BasePage


class FooterPage(BasePage):
    """Класс с методами для подвала сайта."""

    @allure.step('Проверить ссылки в подвале')
    def check_footer_links(self, lst):
        """Проверка ссылок в подвале.

        :param lst: список названий ссылок
        """
        elements = self._element(*FooterPageLocators.LINKS, all=True)
        links_text = [i.text for i in elements]
        with allure.step(f'Проверить, что тексты ссылок {links_text} совпадают с {lst}'):
            allure_helper.attach(self.browser)
            assert links_text == lst, f'Список ссылок - {links_text}'

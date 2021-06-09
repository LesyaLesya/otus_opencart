"""Модуль c методами для Подвала сайта."""


import allure
from pages.base_page import BasePage
from pages.locators import FooterPageLocators


class FooterPage(BasePage):
    """Класс с методами для подвала сайта."""

    def check_footer_links(self, lst):
        """Проверка ссылок в подвале."""

        with allure.step("Получаем все ссылки в подвале"):
            elements = self._element(*FooterPageLocators.LINKS, all=True)
        with allure.step("Получаем все тексты из ссылок в подвале"):
            links_text = [i.text for i in elements]
        with allure.step(f"Провереям, что тексты ссылок {lst}"):
            assert links_text == lst, f"Список ссылок - {links_text}"

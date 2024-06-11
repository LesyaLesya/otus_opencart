import allure

from utils.allure_helper import attach
from utils.locators import FooterPageLocators
from base.base_page import BasePage


class Footer(BasePage):

    @allure.step('Проверить ссылки в подвале')
    def check_footer_links(self, lst):
        """Проверка ссылок в подвале.

        :param lst: список названий ссылок
        """
        elements = self._element(*FooterPageLocators.LINKS, all=True)
        links_text = [i.text for i in elements]
        with allure.step(f'Проверить, что тексты ссылок {links_text} совпадают с {lst}'):
            attach(self.browser)
            assert links_text == lst, f'Список ссылок - {links_text}'

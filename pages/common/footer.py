import allure
from selenium.webdriver.support.wait import WebDriverWait

from helpers.allure_helper import attach
from helpers.locators import FooterPageLocators
from helpers.waits import Elements


class Footer:
    def __init__(self, browser):
        self.browser = browser

    @property
    def footer_links(self):
        return WebDriverWait(self.browser, 5).until(Elements(*FooterPageLocators.LINKS))

    @allure.step('Проверить ссылки в подвале')
    def check_footer_links(self, lst):
        """Проверка ссылок в подвале.

        :param lst: список названий ссылок
        """
        links_text = [i.text for i in self.footer_links]
        with allure.step(f'Проверить, что тексты ссылок {links_text} совпадают с {lst}'):
            attach(self.browser)
            assert links_text == lst, f'Список ссылок - {links_text}'

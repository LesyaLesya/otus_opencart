import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.allure_helper import attach
from helpers.locators import FooterPageLocators


class Footer:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)
        self.elements = EC.visibility_of_all_elements_located

    @property
    def footer_links(self):
        return self.wait.until(self.elements(FooterPageLocators.LINKS))

    @allure.step('Проверить ссылки в подвале')
    def check_footer_links(self, lst):
        """Проверка ссылок в подвале.

        :param lst: список названий ссылок
        """
        links_text = [i.text for i in self.footer_links]
        with allure.step(f'Проверить, что тексты ссылок {links_text} совпадают с {lst}'):
            attach(self.browser)
            assert links_text == lst, f'Список ссылок - {links_text}'

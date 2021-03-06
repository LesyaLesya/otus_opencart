"""Модуль с тестами для Подвала сайта."""

import allure
from pages.footer_page import FooterPage


@allure.feature("Подвал сайта")
@allure.story("Проверка элементов")
@allure.title("Проверка текста ссылок в подвале")
@allure.link("#", name="User story")
def test_check_footer_links_text(browser, url):
    """Тестовая функция для проверки текста ссылок в подвале.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    """
    lst = ["About Us", "Delivery Information", "Privacy Policy",
           "Terms & Conditions", "Contact Us", "Returns",
           "Site Map", "Brands", "Gift Certificates", "Affiliate",
           "Specials", "My Account", "Order History", "Wish List",
           "Newsletter"]
    page = FooterPage(browser, url)
    page.open_url()
    page.check_footer_links(lst)

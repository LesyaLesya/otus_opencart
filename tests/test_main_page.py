"""Модуль с тестами для Главной страницы."""

import pytest
import allure
from otus_opencart.pages.locators import MainPageLocators
from otus_opencart.pages.main_page import MainPage
from otus_opencart.pages.product_page import ProductPage


@allure.feature("Главная страница")
@allure.story("Проверка присутствия элементов на Главной странице")
@allure.title("Поиск элемента {locator}")
@allure.link("#", name="User story")
@pytest.mark.parametrize("locator",
                         [MainPageLocators.BANNER,
                          MainPageLocators.BANNER_PAGINATION_BULLETS,
                          MainPageLocators.HEADER_FEATURED,
                          MainPageLocators.CAROUSEL_BRAND,
                          MainPageLocators.CAROUSEL_PAGINATION_BULLETS],
                         ids=["BANNER", "BANNER_PAGINATION_BULLETS",
                              "HEADER_FEATURED", "CAROUSEL_BRAND",
                              "CAROUSEL_PAGINATION_BULLETS"])
def test_presence_of_elements_on_main_page(browser, url, locator):
    """Тестовая функция для проверки видимости элементов на Главной странице.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    :param locator: путь до элемента
    """
    page = MainPage(browser, url)
    page.open_url()
    page.is_element_visible(*locator)


@allure.feature("Главная страница")
@allure.title("Проверка заголовка Главной страницы")
@allure.link("#", name="User story")
def test_check_title_on_main_page(browser, url):
    """Тестовая функция для проверки корректности заголовка
     на главной странице.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    """
    page = MainPage(browser, url)
    page.open_url()
    page.is_title_correct("Your Store")


@allure.feature("Главная страница")
@allure.title("Проверка смены баннеров по клику на буллеты")
@allure.link("#", name="User story")
def test_banners_rotation(browser, url):
    """Тестовая функция для проверки смены баннеров
    по клику на кнопки под баннером.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    """
    page = MainPage(browser, url)
    page.open_url()
    page.click_banner_bullet_active()
    page.click_banner_bullet_inactive()


@allure.feature("Главная страница")
@allure.story("Проверка перехода в карточку товара из Featured")
@allure.title("Переход к товару с индексом {idx}")
@allure.link("#", name="User story")
@pytest.mark.parametrize("idx", [0, 1])
def test_go_to_product_from_featured(browser, url, idx):
    """Тестовая функция для проверки перехода
    в карточку товара по клику из блока Featured.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    :param idx: порядковый индекс элемента
    """
    page = MainPage(browser, url)
    page.open_url()
    name = page.go_to_product_from_featured(idx)
    product_page = ProductPage(browser, browser.current_url)
    product_page.compare_item_title_on_pages(name)

"""Модуль с тестами для страницы Каталога."""


import pytest
import allure
from otus_opencart.pages.locators import CataloguePageLocators
from otus_opencart.pages.catalogue_page import CataloguePage
from otus_opencart.pages.product_page import ProductPage


@allure.feature("Страница Каталога")
@allure.story("Проверка присутствия элементов на странице Каталога")
@allure.title("Поиск элемента {locator}")
@allure.link("#", name="User story")
@pytest.mark.parametrize("locator",
                         [CataloguePageLocators.BREADCRUMB,
                          CataloguePageLocators.CATALOGUE_HEADER,
                          CataloguePageLocators.CATALOGUE_IMAGE,
                          CataloguePageLocators.LEFT_MENU,
                          CataloguePageLocators.BANNER_UNDER_LEFT_MENU],
                         ids=["BREADCRUMB", "CATALOGUE_HEADER",
                              "CATALOGUE_IMAGE", "LEFT_MENU",
                              "BANNER_UNDER_LEFT_MENU"])
def test_presence_of_elements_on_catalogue_page(browser, url, locator):
    """Тестовая функция для проверки видимости элементов на странице Каталога.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    :param locator: путь до элемента
    """
    url = f'{url}index.php?route=product/category&path=18'
    page = CataloguePage(browser, url)
    page.open_url()
    page.is_element_visible(*locator)


@allure.feature("Страница Каталога")
@allure.title("Добавление товара к сравнению")
@allure.link("#", name="User story")
def test_add_to_compare(browser, url):
    """Тестовая функция для проверки добавление товара к сравнению
    со страницы каталога.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    """
    url = f'{url}index.php?route=product/category&path=18'
    page = CataloguePage(browser, url)
    page.open_url()
    page.click_to_compare()
    page.should_be_successful_alert()
    page.should_be_adding_in_compare_link("Product Compare (1)")


@allure.feature("Страница Каталога")
@allure.story("Сортировка товаров")
@allure.title("Сортировка по названию от A до Z")
@allure.link("#", name="User story")
def test_sort_by_name_a_z(browser, url):
    """Тестовая функция для проверки сортировки товаров по
    названию от A до Z.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    """
    url = f'{url}index.php?route=product/category&path=18'
    page = CataloguePage(browser, url)
    page.open_url()
    page.select_by_text("Name (A - Z)")
    page.check_sort_by_name_a_z()


@allure.feature("Страница Каталога")
@allure.story("Сортировка товаров")
@allure.title("Сортировка по цене Low > High")
@allure.link("#", name="User story")
def test_sort_by_price_low_to_high(browser, url):
    """Тестовая функция для проверки сортировки товаров по
    возрастанию цены.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    """
    url = f'{url}index.php?route=product/category&path=18'
    page = CataloguePage(browser, url)
    page.open_url()
    page.select_by_text("Price (Low > High)")
    page.check_sort_by_price_low_high()


@allure.feature("Страница Каталога")
@allure.story("Переход на страницу товара")
@allure.title("Переход в карточку товара по клику на товар")
@allure.link("#", name="User story")
@pytest.mark.parametrize("idx", [0, 1])
def test_go_to_product_from_catalogue(browser, url, idx):
    """Тестовая функция для проверки перехода
    в карточку товара по клику из каталога товаров.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    :param idx: порядковый индекс элемента
    """
    url = f'{url}index.php?route=product/category&path=18'
    page = CataloguePage(browser, url)
    page.open_url()
    name = page.go_to_product_from_catalogue(idx)
    product_page = ProductPage(browser, browser.current_url)
    product_page.compare_item_title_on_pages(name)

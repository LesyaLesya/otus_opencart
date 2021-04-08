"""Модуль с тестами для страницы Товара."""


import pytest
import allure
from otus_opencart.pages.locators import ProductPageLocators
from otus_opencart.pages.product_page import ProductPage


@allure.feature("Страница Товара")
@allure.story("Проверка присутствия элементов на странице Товара")
@allure.title("Поиск элемента {locator}")
@allure.link("#", name="User story")
@pytest.mark.parametrize("locator",
                         [ProductPageLocators.PRODUCT_HEADER,
                          ProductPageLocators.BUTTON_CART,
                          ProductPageLocators.IMAGES_BLOCK,
                          ProductPageLocators.RATING_BLOCK,
                          ProductPageLocators.PRODUCT_DESCRIPTION],
                         ids=["PRODUCT_HEADER", "BUTTON_CART",
                              "IMAGES_BLOCK", "RATING_BLOCK",
                              "PRODUCT_DESCRIPTION"])
def test_presence_of_elements_on_product_page(browser, url, locator):
    """Тестовая функция для проверки видимости элементов на странице Товара.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    :param locator: путь до элемента
    """
    url = f'{url}index.php?route=product/product&path=18&product_id=47'
    page = ProductPage(browser, url)
    page.open_url()
    page.is_element_visible(*locator)


@allure.feature("Страница Товара")
@allure.title("Открытие фото товара по клику")
@allure.link("#", name="User story")
def test_open_image_in_window_by_click(browser, url):
    """Тестовая функция для проверки открытия фото товара
    во всплывающем окне по клику.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    """
    url = f'{url}index.php?route=product/product&path=18&product_id=47'
    page = ProductPage(browser, url)
    page.open_url()
    page.click_main_product_image()
    page.get_main_image_in_window()


@allure.feature("Страница Товара")
@allure.title("Переход по табам")
@allure.link("#", name="User story")
def test_click_on_tabs(browser, url):
    """Тестовая функция для проверки перехода по
    табам по клику.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    """
    url = f'{url}index.php?route=product/product&path=18&product_id=47'
    page = ProductPage(browser, url)
    page.open_url()
    page.click_on_tab_specification()
    page.click_on_tab_reviews()
    page.click_on_tab_description()

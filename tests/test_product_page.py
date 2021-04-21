"""Модуль с тестами для страницы Товара."""


import pytest
import allure
from pages.locators import ProductPageLocators
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.comparison_page import ComparisonPage
from pages.cart_page import CartPage


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


@allure.feature("Страница Товара")
@allure.story("Добавление товара в Виш-лист")
@allure.title("Добавление товара в Виш-лист со страницы Товара")
@allure.link("#", name="User story")
def test_adding_to_wish_list_from_product(browser, url):
    """Тестовая функция для проверки добавления продукта
    в виш-лист из карточки товара.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    """
    url = f'{url}index.php?route=product/product&path=18&product_id=47'
    page = ProductPage(browser, url)
    page.open_url()
    name = page.add_to_wishlist()
    page.click_login_from_alert()
    login_page = LoginPage(browser, browser.current_url)
    login_page.login_user()
    account_page = AccountPage(browser, browser.current_url)
    account_page.open_wishlist()
    account_page.check_item_in_wish_list(name)


@allure.feature("Страница Товара")
@allure.story("Добавление товара в сравнение")
@allure.title("Добавление товара в сравнение из карточки товара")
@allure.link("#", name="User story")
def test_adding_to_compare_from_product(browser, url):
    """Тестовая функция для проверки добавления продукта
    в сравнение из карточки товара.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    """
    url = f'{url}index.php?route=product/product&path=18&product_id=47'
    page = ProductPage(browser, url)
    page.open_url()
    name = page.add_to_compare()
    page.click_compare_from_alert()
    compare_page = ComparisonPage(browser, browser.current_url)
    compare_page.check_item_in_comparison(name)


@allure.feature("Страница Товара")
@allure.story("Добавление товара в корзину")
@allure.title("Добавление товара в корзину из карточки товара")
@allure.link("#", name="User story")
def test_adding_to_cart_from_product(browser, url):
    """Тестовая функция для проверки добавления продукта
    в корзину из карточки товара.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    """
    url = f'{url}index.php?route=product/product&path=18&product_id=47'
    page = ProductPage(browser, url)
    page.open_url()
    name = page.add_to_cart()
    page.click_cart_from_alert()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.check_item_in_cart(name)

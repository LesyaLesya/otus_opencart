"""Модуль с тестами для страницы Каталога."""


import pytest
import allure
from pages.locators import CataloguePageLocators
from pages.catalogue_page import CataloguePage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.header_page import HeaderPage
from pages.comparison_page import ComparisonPage


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


@allure.feature("Страница Каталога")
@allure.story("Добавление товара в Виш-лист")
@allure.title("Добавление товара в Виш-лист из каталога")
@allure.link("#", name="User story")
@pytest.mark.parametrize("idx", [0])
def test_adding_to_wish_list_from_catalogue(browser, url, idx):
    """Тестовая функция для проверки добавления продукта
    в виш-лист из каталога.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    :param idx: порядковый индекс элемента
    """
    url = f'{url}index.php?route=product/category&path=18'
    page = CataloguePage(browser, url)
    page.open_url()
    name = page.add_to_wishlist(idx)
    page.click_login_from_alert()
    login_page = LoginPage(browser, browser.current_url)
    login_page.login_user()
    account_page = AccountPage(browser, browser.current_url)
    account_page.open_wishlist()
    account_page.check_item_in_wish_list(name)


@allure.feature("Страница Каталога")
@allure.story("Добавление товара в сравнение")
@allure.title("Добавление товара в сравнение из каталога")
@allure.link("#", name="User story")
@pytest.mark.parametrize("idx", [1])
def test_adding_to_compare_from_catalogue(browser, url, idx):
    """Тестовая функция для проверки добавление товара к сравнению
    со страницы каталога.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    :param idx: порядковый индекс элемента
    """
    url = f'{url}index.php?route=product/category&path=18'
    page = CataloguePage(browser, url)
    page.open_url()
    name = page.add_to_compare(idx)
    page.should_be_adding_in_compare_link("1")
    page.go_to_compare_page()
    compare_page = ComparisonPage(browser, browser.current_url)
    compare_page.check_item_in_comparison(name)


@allure.feature("Страница Каталога")
@allure.story("Переключение вида отображения карточек товара")
@allure.title("Переключение вида отображения карточек товара")
@allure.link("#", name="User story")
def test_change_view_carts(browser, url):
    """Тестовая функция для проверки изменения отображения вида
    вывода карточек товара.

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    """
    url = f'{url}index.php?route=product/category&path=18'
    page = CataloguePage(browser, url)
    page.open_url()
    page.click_list_view()
    page.click_list_grid()


@allure.feature("Страница Каталога")
@allure.story("Переключение валют")
@allure.title("Изменение валют в цене товаров")
@allure.link("#", name="User story")
@pytest.mark.parametrize("values, idx, symbol", [("€ Euro", -1, "€"),
                                    ("£ Pound Sterling", 0, "£"),
                                    ("$ US Dollar", 0, "$")])
def test_change_currency(browser, url, values, idx, symbol):
    """Тестовая функция для проверки изменения валюты
    в ценах товаров в каталоге

    :param browser: фикстура для запуска драйвера
    :param url: фикстура с урлом тестируемого ресурса
    :param values: валюты
    :param idx: порядковый индекс символа в цене товара
    :param symbol: строковое представление символа валюты
    """
    url = f'{url}index.php?route=product/category&path=18'
    catalogue_page = CataloguePage(browser, url)
    catalogue_page.open_url()
    currency_page = HeaderPage(browser, browser.current_url)
    currency_page.choose_currency(values)
    catalogue_page2 = CataloguePage(browser, browser.current_url)
    catalogue_page2.check_currency_in_price(idx, symbol)

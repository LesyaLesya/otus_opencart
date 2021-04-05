"""Модуль c общими методами для всех страниц."""

import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from otus_opencart.helpers import allure_helper


class BasePage:
    """Класс, описывающий базовую страницу."""

    @allure.step("Открыть {url}")
    def __init__(self, browser, url, wait=5):
        """Конструктор класса.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """

        self.browser = browser
        self.url = url
        self.wait = WebDriverWait(browser, wait)

    def open_url(self):
        """Открытие url методом get."""

        self.browser.get(self.url)
        return self

    @allure.step("Проверить видимость элемента с локатором {locator} по пути {el_path}")
    def is_element_visible(self, locator, el_path):
        """Возвращает результат поиска элемента после ожилания.

        :param locator: тип локатора
        :param el_path: путь до элемента
        """

        try:
            return self.wait.until(
                EC.visibility_of_element_located((locator, el_path)))
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Нет элемента с локатором {locator} по пути {el_path}')

    @allure.step("Проверить корректность заголовка {title}")
    def is_title_correct(self, title):
        """Возвращает результат проверки корректности заголовка страницы.

        :param title: заголовок страницы
        """

        try:
            return self.wait.until(EC.title_is(title))
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f"Заголовок - {title}")

    @allure.step("Кликнуть по элементу с локатором {locator} по пути {el_path}")
    def click_on_element(self, locator, el_path):
        """Возвращает клик по найденному элементу.

        :param locator: тип локатора
        :param el_path: путь до элемента
        """

        try:
            element = self.is_element_visible(locator, el_path)
            element.click()
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Нет элемента с локатором {locator} по пути {el_path}')

    @allure.step("Получить текст элемента с локатором {locator} по пути {el_path}")
    def get_text_of_element(self, locator, el_path):
        """Возвращает текст найденного элемента.

        :param locator: тип локатора
        :param el_path: путь до элемента
        """

        try:
            element = self.is_element_visible(locator, el_path)
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Нет элемента с локатором {locator} по пути {el_path}')
        return element.text

    @allure.step("Найти выпадающий список с локатором {locator} по пути {el_path}")
    def select_products(self, locator, el_path):
        """Возвращает найденный выпадающий список.

        :param locator: тип локатора
        :param el_path: путь до элемента
        """

        try:
            self.is_element_visible(locator, el_path)
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Нет элемента с локатором {locator} по пути {el_path}')
        return Select(self.browser.find_element(locator, el_path))

    @allure.step("Получить атрибут {attr} у элемента с локатором {locator} по пути {el_path}")
    def getting_attr(self, attr, locator, el_path):
        """Возвращает атрибут найденного элемента.

        :param locator: тип локатора
        :param el_path: путь до элемента
        :param attr: атрибут элемента
        """

        try:
            element = self.is_element_visible(locator, el_path)
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Нет элемента с локатором {locator} по пути {el_path}')
        return element.get_attribute(attr)

    @allure.step("Ввести текст {value} в инпут {el_path}")
    def input_text(self, locator, el_path, value):
        """Возвращает ввод текста в найденный инпут.

        :param locator: тип локатора
        :param el_path: путь до элемента
        :param value: вводимое значение в инпут
        """

        try:
            element = self.is_element_visible(locator, el_path)
            element.clear()
            element.send_keys(value)
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Нет элемента с локатором {locator} по пути {el_path}')

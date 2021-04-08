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

    @allure.step("Находим элемент с локатором {locator} по пути {el_path}  и индексом {index}")
    def _element(self, locator, el_path, index=0, all=False):
        """Возвращает результат поиска элементов после ожилания.

                :param locator: тип локатора
                :param el_path: путь до элемента
                :param index: порядковый индекс элемента
                :param all: маркер для поиска одного элемента или группы элементов
                """
        try:
            if all:
                return self.browser.find_elements(locator, el_path)
            return self.browser.find_elements(locator, el_path)[index]

            #     return self.wait.until(waits.Elements(locator, el_path))
            # return self.wait.until(waits.Element(locator, el_path, index))
        except TimeoutException:
            raise AssertionError(f'Нет элемента с локатором {locator} по пути {el_path}')

    @allure.step("Проверить видимость элемента с локатором {locator} по пути {el_path}")
    def is_element_visible(self, locator, el_path, index=0):
        """Возвращает результат ожидания видимости элемента.

        :param locator: тип локатора
        :param el_path: путь до элемента
        :param index: порядковый индекс элемента
        """
        try:
            return self.wait.until(
                EC.visibility_of(self._element(locator, el_path, index)))
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Нет элемента с локатором {locator} по пути {el_path}')

    @allure.step("Кликнуть по элементу с локатором {locator} по пути {el_path}")
    def click_on_element(self, locator, el_path, index=0):
        """Возвращает клик по найденному элементу.

        :param locator: тип локатора
        :param el_path: путь до элемента
        :param index: порядковый индекс элемента
        """
        element = self.is_element_visible(locator, el_path, index)
        try:
            return element.click()
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Нет элемента с локатором {locator} по пути {el_path}')

    @allure.step("Получить текст элемента с локатором {locator} по пути {el_path}")
    def get_text_of_element(self, locator, el_path, index=0):
        """Возвращает текст найденного элемента.

        :param locator: тип локатора
        :param el_path: путь до элемента
        :param index: порядковый индекс элемента
        """

        element = self.is_element_visible(locator, el_path, index)
        try:
            return element.text
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Нет элемента с локатором {locator} по пути {el_path}')

    @allure.step("Проверяем корректность заголовка {title}")
    def is_title_correct(self, title):
        """Проверка тайтла страницы."""
        try:
            return self.wait.until(EC.title_is(title))
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError("Заголовок не совпал")

    @allure.step("Получить title страницы")
    def get_title(self):
        """Возвращает title страницы."""

        try:
            return self.browser.title
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Title - {self.browser.title}')

    @allure.step("Найти выпадающий список с локатором {locator} по пути {el_path}")
    def select_products(self, locator, el_path, index=0):
        """Возвращает найденный выпадающий список.

        :param locator: тип локатора
        :param el_path: путь до элемента
        :param index: порядковый индекс элемента
        """

        try:
            self.is_element_visible(locator, el_path, index)
            return Select(self.browser.find_element(locator, el_path))
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Нет элемента с локатором {locator} по пути {el_path}')

    @allure.step("Получить атрибут {attr} у элемента с локатором {locator} по пути {el_path}")
    def getting_attr(self, attr, locator, el_path, index=0):
        """Возвращает атрибут найденного элемента.

        :param locator: тип локатора
        :param el_path: путь до элемента
        :param attr: атрибут элемента
        :param index: порядковый индекс элемента
        """

        element = self.is_element_visible(locator, el_path, index)
        try:
            return element.get_attribute(attr)
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Нет элемента с локатором {locator} по пути {el_path}')

    @allure.step("Ввести текст {value} в инпут {el_path}")
    def input_text(self, locator, el_path, value, index=0):
        """Возвращает ввод текста в найденный инпут.

        :param locator: тип локатора
        :param el_path: путь до элемента
        :param value: вводимое значение в инпут
        :param index: порядковый индекс элемента
        """

        element = self.is_element_visible(locator, el_path, index)
        try:
            element.clear()
            return element.send_keys(value)
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Нет элемента с локатором {locator} по пути {el_path}')

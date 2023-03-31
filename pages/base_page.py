"""Модуль c общими методами для всех страниц."""

import allure

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from helpers import allure_helper
from helpers.waits import Element, Elements, Clickable

from pages.common.alert import Alert
from pages.common.footer import Footer
from pages.common.header import Header


class BasePage:
    """Класс, описывающий базовую страницу."""

    def __init__(self, browser, url, db_connection=None, wait=10):
        """Конструктор класса.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        :param db_connection: фикстура коннекта к БД
        """
        self.browser = browser
        self.url = url
        self.wait = WebDriverWait(browser, wait)
        self.db_connection = db_connection
        self.alert = Alert(self.browser)
        self.footer = Footer(self.browser)
        self.header = Header(self.browser)

    def open_url(self, path='/'):
        """Открытие url.

        :param path: путь
        """
        with allure.step(f'Перейти по ссылке {self.url}{path}'):
            return self.browser.get(f'{self.url}{path}')

    @allure.step('Найти элемент по локатору {locator} и пути {el_path}, индекс {index}')
    def _element(self, locator, el_path, index=0, all=False):
        """Возвращает результат поиска элементов после ожидания.

        :param locator: тип локатора
        :param el_path: путь до элемента
        :param index: порядковый индекс элемента
        :param all: маркер для поиска одного элемента или группы элементов
        """
        try:
            if all:
                return self.wait.until(Elements(locator, el_path))
            return self.wait.until(Element(locator, el_path, index))
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Нет элемента с локатором {locator} по пути {el_path} и индексом {index}')

    @allure.step('Проверить что элемент {locator}, {el_path} с индексом {index} виден на странице')
    def is_element_visible(self, locator, el_path, index=0):
        """Возвращает результат ожидания видимости элемента.

        :param locator: тип локатора
        :param el_path: путь до элемента
        :param index: порядковый индекс элемента
        """
        element = self._element(locator, el_path, index)
        try:
            assert element.is_displayed()
        except AssertionError:
            allure_helper.attach(self.browser)
            f'Элемент {locator} {el_path} {index} не отображается на странице'

    @allure.step('Кликнуть по элементу с локатором {locator} по пути {el_path} и индексом {index}')
    def click_on_element(self, locator, el_path, index=0):
        """Возвращает клик по найденному элементу.

        :param locator: тип локатора
        :param el_path: путь до элемента
        :param index: порядковый индекс элемента
        """
        element = self._element(locator, el_path, index)
        try:
            self.wait.until(Clickable(element))
            return element.click()
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Не получается кликнуть по элементу {locator} {el_path} {index}')

    @allure.step('Получить текст элемента с локатором {locator} по пути {el_path} и индексом {index}')
    def get_text_of_element(self, locator, el_path, index=0):
        """Возвращает текст найденного элемента.

        :param locator: тип локатора
        :param el_path: путь до элемента
        :param index: порядковый индекс элемента
        """
        element = self._element(locator, el_path, index)
        try:
            return element.text
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Не получается получить текст элемента {locator} {el_path} {index}')

    @allure.step('Проверить корректность заголовка {title}')
    def is_title_correct(self, title):
        """Проверка тайтла страницы."""
        try:
            return self.wait.until(EC.title_is(title))
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Заголовок не совпал: {self.browser.title}, ожидаем {title}')

    @allure.step('Получить title страницы')
    def get_title(self):
        """Возвращает title страницы."""
        try:
            return self.browser.title
        except Exception as e:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Не получается получить тайтл страницы')

    @allure.step('Найти выпадающий список по пути {el_path}')
    def select_products(self, locator, el_path, index=0):
        """Возвращает найденный выпадающий список.

        :param locator: тип локатора
        :param el_path: путь до элемента
        :param index: порядковый индекс элемента
        """
        try:
            return Select(self._element(locator, el_path, index))
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Нет выпадающего списка с локатором {locator} по пути {el_path} и индексом {index}')

    @allure.step('Получить атрибут {attr} у элемента {el_path} с индексом {index}')
    def getting_attr(self, attr, locator, el_path, index=0):
        """Возвращает атрибут найденного элемента.

        :param locator: тип локатора
        :param el_path: путь до элемента
        :param attr: атрибут элемента
        :param index: порядковый индекс элемента
        """
        element = self._element(locator, el_path, index)
        try:
            return element.get_attribute(attr)
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'У элемента {locator} {el_path} {index} нет атрибута {attr}')

    @allure.step('Ввести текст {value} в инпут {el_path} с индексом {index}')
    def input_text(self, locator, el_path, value, index=0):
        """Возвращает ввод текста в найденный инпут.

        :param locator: тип локатора
        :param el_path: путь до элемента
        :param value: вводимое значение в инпут
        :param index: порядковый индекс элемента
        """
        element = self._element(locator, el_path, index)
        try:
            element.clear()
            return element.send_keys(value)
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Не получается ввести текст {value} в элемент {locator} {el_path} {index}')

    @allure.step('Проскроллить до элемента {el}')
    def scroll_to_element(self, el):
        """Возвращает скролл до элемента."""
        try:
            return self.browser.execute_script('return arguments[0].scrollIntoView(true);', el)
        except Exception as e:
            raise AssertionError(f'Ошибка {e}')

    @allure.step('Получить css свойство {css_property} элемента {locator} {el_path} с индексом {index}')
    def get_css_property(self, locator, el_path, css_property, index=0):
        """Возвращает значение css свойства найденного элемента.

        :param locator: тип локатора
        :param el_path: путь до элемента
        :param css_property: css свойство
        :param index: порядковый индекс элемента
        """
        element = self._element(locator, el_path, index)
        try:
            return element.value_of_css_property(css_property)
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'У элемента {locator} {el_path} {index} нет css свойства {css_property}')

    @allure.step('Навести курсор мыши на элемент {locator} {el_path} с индексом {index}')
    def mouse_move_to_element(self, locator, el_path, index=0):
        """Наводит курсор мыши на элемент.

        :param locator: тип локатора
        :param el_path: путь до элемента
        :param index: порядковый индекс элемента
        """
        element = self._element(locator, el_path, index)
        try:
            return ActionChains(self.browser).move_to_element(element).perform()
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Не получается навести на элемент {locator} {el_path} {index}')

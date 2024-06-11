"""Модуль c общими методами для всех страниц."""

import allure

from selenium.common.exceptions import (
    NoSuchElementException, ElementClickInterceptedException)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from utils import allure_helper


class BasePage:
    """Класс, описывающий базовую страницу."""

    def __init__(self, browser):
        """Конструктор класса.

        :param browser: фикстура для запуска драйвера
        """
        self.browser = browser
        self.wait = WebDriverWait(browser, 10, poll_frequency=1)

    def open_url(self):
        """Открытие url."""
        with allure.step(f'Перейти по ссылке {self.PAGE_URL}'):
            self.browser.get(self.PAGE_URL)

    def is_opened(self):
        with allure.step(f"Проверить, что открыта страница {self.PAGE_URL}"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    @allure.step('Дождаться видимости элемента с локатором {locator}  {el_path}, индекс {index}')
    def _element(self, locator, el_path, index=0, all=False):
        """Возвращает найденный видимый элемент после ожидания.

        :param locator: тип локатора
        :param el_path: путь до элемента
        :param index: порядковый индекс элемента
        :param all: маркер для поиска одного элемента или группы элементов
        """
        try:
            if all:
                return self.wait.until(EC.visibility_of_all_elements_located((locator, el_path)))
            return self.wait.until(EC.visibility_of_all_elements_located((locator, el_path)))[index]
        except Exception:
            allure_helper.attach(self.browser)
            raise AssertionError(
                f'На странице не виден элемент с локатором {locator} по пути {el_path} и индексом {index}')

    @allure.step('Дождаться элемента в DOM, локатор {locator} {el_path}, индекс {index}')
    def _element_presence(self, locator, el_path, index=0, all=False):
        """Возвращает найденный элемент после ожидания.

        :param locator: тип локатора
        :param el_path: путь до элемента
        :param index: порядковый индекс элемента
        :param all: маркер для поиска одного элемента или группы элементов
        """
        try:
            if all:
                return self.wait.until(EC.presence_of_all_elements_located((locator, el_path)))
            return self.wait.until(EC.presence_of_all_elements_located((locator, el_path)))[index]
        except Exception:
            allure_helper.attach(self.browser)
            raise AssertionError(
                f'В DOM нет элемента с локатором {locator} по пути {el_path} и индексом {index}')

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
        except NoSuchElementException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Элемент {locator} {el_path} {index} не отображается на странице')

    @allure.step('Кликнуть по элементу с локатором {locator} по пути {el_path} и индексом {index}')
    def click_on_element(self, locator, el_path, index=0):
        """Возвращает клик по найденному элементу.

        :param locator: тип локатора
        :param el_path: путь до элемента
        :param index: порядковый индекс элемента
        """
        element = self._element(locator, el_path, index)
        try:
            if element and element.is_enabled():
                return element.click()
        except ElementClickInterceptedException:
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
        except Exception:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Не получается получить текст элемента {locator} {el_path} {index}')

    @allure.step('Проверить корректность заголовка {title}')
    def is_title_correct(self, title):
        """Проверка тайтла страницы."""
        try:
            return self.wait.until(EC.title_is(title))
        except Exception:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Заголовок не совпал: {self.browser.title}, ожидаем {title}')

    @allure.step('Получить title страницы')
    def get_title(self):
        """Возвращает title страницы."""
        try:
            return self.browser.title
        except Exception:
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
        except Exception:
            allure_helper.attach(self.browser)
            raise AssertionError(
                f'Нет выпадающего списка с локатором {locator} по пути {el_path} и индексом {index}')

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
        except Exception:
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
        except Exception:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Не получается ввести текст {value} в элемент {locator} {el_path} {index}')

    @allure.step('Проскроллить до элемента {el_path} с индексом {index}')
    def scroll_to_element(self, locator, el_path, index=0):
        """Возвращает скролл до элемента."""
        try:
            element = self._element(locator, el_path, index)
            return self.browser.execute_script('return arguments[0].scrollIntoView(true);', element)
        except Exception as e:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Ошибка {e}')

    @allure.step('Проскроллить до низа страницы')
    def scroll_down_page(self):
        """Возвращает скролл до низа страницы"""
        try:
            return self.browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        except Exception as e:
            allure_helper.attach(self.browser)
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
        except Exception:
            allure_helper.attach(self.browser)
            raise AssertionError(
                f'У элемента {locator} {el_path} {index} нет css свойства {css_property}')

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
        except Exception:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Не получается навести на элемент {locator} {el_path} {index}')

    @allure.step('Получить id у товара {el_path} с индексом {index}')
    def get_item_id(self, locator, el_path, index=0):
        """Возвращает id товара.

        :param locator: тип локатора
        :param el_path: путь до элемента
        :param index: порядковый индекс элемента
        """
        element = self._element(locator, el_path, index)
        value = element.get_attribute('onclick')
        return int(''.join([i for i in value if i.isdigit()]))

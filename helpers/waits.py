"""Модуль c вспомогательными методами ожиданий."""

from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Element:
    """Класс с методами ожидания одного элемента."""

    def __init__(self, locator, el_path, index=0):
        self.locator = locator
        self.el_path = el_path
        self.index = index

    def __call__(self, browser):
        try:
            return browser.find_elements(self.locator, self.el_path)[self.index]
        except (IndexError, NoSuchElementException, TimeoutException):
            return False


class Elements:
    """Класс с методами ожидания группы элементов."""

    def __init__(self, locator, el_path):
        self.locator = locator
        self.el_path = el_path

    def __call__(self, browser):
        try:
            return browser.find_elements(self.locator, self.el_path)
        except (IndexError, NoSuchElementException, TimeoutException):
            return False

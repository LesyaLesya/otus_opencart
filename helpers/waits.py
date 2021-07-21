"""Модуль с вспомогательными классами для поиска элементов."""

from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Element:

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

    def __init__(self, locator, el_path):
        self.locator = locator
        self.el_path = el_path

    def __call__(self, browser):
        try:
            return browser.find_elements(self.locator, self.el_path)
        except (IndexError, NoSuchElementException, TimeoutException):
            return False


class Clickable:

    def __init__(self, element):
        self.element = element

    def __call__(self, browser):
        return self.element.is_enabled() and self.element.is_displayed()

"""Модуль c методами для Шапки сайта."""


import allure
from pages.base_page import BasePage
from pages.locators import HeaderPageLocators
from pages.styles import Colors, Cursor, Gradients, Border


class HeaderPage(BasePage):
    """Класс с методами для Шапки сайта."""

    @allure.step("Ввести в поле поиска значение {txt}")
    def set_search_text(self, txt):
        """Ввод текста в поле поиска.

        :param txt: искомое значение
        """

        self.input_text(*HeaderPageLocators.SEARCH_INPUT, txt)
        return self

    @allure.step("Нажать на кнопку поиска")
    def start_search(self):
        """Нажатие на кнопку запуска поиска."""

        self.click_on_element(*HeaderPageLocators.SEARCH_BUTTON)
        return self

    def go_to_login_page(self):
        """Проверка перехода на страницу Логина."""

        with allure.step("Кликнуть на кнопку MY_ACCOUNT"):
            self.click_on_element(*HeaderPageLocators.MY_ACCOUNT_LINK)
        with allure.step("Кликнуть на кнопку Login"):
            self.click_on_element(*HeaderPageLocators.LOGIN_LINK)
        return self

    def check_logo_css(self):
        """Проверка стилей логотипа без наведения."""

        lst = []
        with allure.step("Получить стили элемента"):
            for prop in ["font-size", "font-weight", "cursor", "color"]:
                lst.append(self.get_css_property(*HeaderPageLocators.LOGO, prop))
        with allure.step("Проверить, что шрифт 33px"):
            assert lst[0] == "33px", f"Размер текста - {lst[0]}"
        with allure.step("Проверить, что жирность 500"):
            assert lst[1] == "500", f"Жирность шрифта - {lst[1]}"
        with allure.step("Проверить, что курсор Pointer"):
            assert lst[2] == Cursor.POINTER, f"Курсор - {lst[2]}"
        with allure.step(f"Проверить, что цвет {Colors.LIGHT_BLUE}"):
            assert lst[3] == Colors.LIGHT_BLUE, f"Цвет текста - {lst[3]}"

    def check_logo_css_hover(self):
        """Проверка стилей логотипа при наведении."""

        self.mouse_move_to_element(*HeaderPageLocators.LOGO)
        lst = []
        with allure.step("Получить стили элемента"):
            for prop in ["font-size", "font-weight", "cursor", "color"]:
                lst.append(self.get_css_property(*HeaderPageLocators.LOGO, prop))
        with allure.step("Проверить, что шрифт 33px"):
            assert lst[0] == "33px", f"Размер текста - {lst[0]}"
        with allure.step("Проверить, что жирность 500"):
            assert lst[1] == "500", f"Жирность шрифта - {lst[1]}"
        with allure.step("Проверить, что курсор Pointer"):
            assert lst[2] == Cursor.POINTER, f"Курсор - {lst[2]}"
        with allure.step(f"Проверить, что цвет {Colors.DARK_BLUE}"):
            assert lst[3] == Colors.DARK_BLUE, f"Цвет текста - {lst[3]}"

    def check_cart_button_css(self):
        """Проверка стилей кнопки корзины без наведения."""

        lst = []
        with allure.step("Получить стили элемента"):
            for prop in ["font-size", "line-height", "color", "background-color", "background-image",
                         "border-top-color", "border-right-color", "border-bottom-color",
                         "border-left-color", "border-radius", "cursor"]:
                lst.append(self.get_css_property(*HeaderPageLocators.CART_BUTTON, prop))
        with allure.step("Проверить, что шрифт 12px"):
            assert lst[0] == "12px", f"Размер текста - {lst[0]}"
        with allure.step("Проверить межстрочный интервал 18px"):
            assert lst[1] == "18px", f"Межстрочный интервал - {lst[1]}"
        with allure.step("Проверить, что цвет текста белый"):
            assert lst[2] == Colors.WHITE, f"Цвет текста - {lst[2]}"
        with allure.step("Проверить цвета фона"):
            assert lst[3] == Colors.DARK_GRAY, f"Цвет фона - {lst[3]}"
        with allure.step("Прверить фоновое изображение"):
            assert lst[4] == Gradients.LIGHT_BLACK, f"Фоновое изображение - {lst[4]}"
        with allure.step("Проверит цвет верхней рамки"):
            assert lst[5] == Colors.LIGHT_BLACK, f"Цвет верхней рамки - {lst[5]}"
        with allure.step("Проверит цвет правой рамки"):
            assert lst[6] == Colors.LIGHT_BLACK, f"Цвет правой рамки - {lst[6]}"
        with allure.step("Проверит цвет нижней рамки"):
            assert lst[7] == Colors.BLACK, f"Цвет нижней рамки - {lst[7]}"
        with allure.step("Проверит цвет левой рамки"):
            assert lst[8] == Colors.LIGHT_BLACK, f"Цвет левой рамки - {lst[8]}"
        with allure.step("Проверить радиус скругления"):
            assert lst[9] == "4px", f"Радиус скругления - {lst[9]}"
        with allure.step("Проверить, что курсор Pointer"):
            assert lst[10] == Cursor.POINTER, f"Курсор - {lst[10]}"

    def check_cart_button_css_hover(self):
        """Проверка стилей кнопки корзины при наведении."""

        self.mouse_move_to_element(*HeaderPageLocators.CART_BUTTON)
        lst = []
        with allure.step("Получить стили элемента"):
            for prop in ["font-size", "line-height", "color", "background-color", "background-image",
                         "border-top-color", "border-right-color", "border-bottom-color",
                         "border-left-color", "border-radius", "cursor"]:
                lst.append(self.get_css_property(*HeaderPageLocators.CART_BUTTON, prop))
        with allure.step("Проверить, что шрифт 12px"):
            assert lst[0] == "12px", f"Размер текста - {lst[0]}"
        with allure.step("Проверить межстрочный интервал 18px"):
            assert lst[1] == "18px", f"Межстрочный интервал - {lst[1]}"
        with allure.step("Проверить, что цвет текста белый"):
            assert lst[2] == Colors.WHITE, f"Цвет текста - {lst[2]}"
        with allure.step("Проверить цвета фона"):
            assert lst[3] == Colors.LIGHT_BLACK, f"Цвет фона - {lst[3]}"
        with allure.step("Прверить фоновое изображение"):
            assert lst[4] == Gradients.MEDIUM_BLACK, f"Фоновое изображение - {lst[4]}"
        with allure.step("Проверит цвет верхней рамки"):
            assert lst[5] == Colors.LIGHT_BLACK, f"Цвет верхней рамки - {lst[5]}"
        with allure.step("Проверит цвет правой рамки"):
            assert lst[6] == Colors.LIGHT_BLACK, f"Цвет правой рамки - {lst[6]}"
        with allure.step("Проверит цвет нижней рамки"):
            assert lst[7] == Colors.BLACK, f"Цвет нижней рамки - {lst[7]}"
        with allure.step("Проверит цвет левой рамки"):
            assert lst[8] == Colors.LIGHT_BLACK, f"Цвет левой рамки - {lst[8]}"
        with allure.step("Проверит радиус скругления"):
            assert lst[9] == "4px", f"Радиус скругления - {lst[9]}"
        with allure.step("Проверить, что курсор Pointer"):
            assert lst[10] == Cursor.POINTER, f"Курсор - {lst[10]}"

    def check_cart_button_css_click(self):
        """Проверка стилей кнопки корзины при клике."""

        self.click_on_element(*HeaderPageLocators.CART_BUTTON)
        lst = []
        with allure.step("Получить стили элемента"):
            for prop in ["font-size", "line-height", "color", "background-color", "background-image",
                         "border", "border-radius", "cursor"]:
                lst.append(self.get_css_property(*HeaderPageLocators.CART_BUTTON, prop))
        with allure.step("Проверить, что шрифт 12px"):
            assert lst[0] == "12px", f"Размер текста - {lst[0]}"
        with allure.step("Проверить межстрочный интервал 18px"):
            assert lst[1] == "18px", f"Межстрочный интервал - {lst[1]}"
        with allure.step("Проверить, что цвет текста серый"):
            assert lst[2] == Colors.MEDIUM_GRAY, f"Цвет текста - {lst[2]}"
        with allure.step("Проверить цвета фона"):
            assert lst[3] == Colors.WHITE, f"Цвет фона - {lst[3]}"
        with allure.step("Прверить фоновое изображение"):
            assert lst[4] == "none", f"Фоновое изображение - {lst[4]}"
        with allure.step("Проверит стиль рамки"):
            assert lst[5] == Border.LIGHT_GRAY, f"Рамка - {lst[5]}"
        with allure.step("Проверит радиус скругления"):
            assert lst[6] == "4px", f"Радиус скругления - {lst[6]}"
        with allure.step("Проверить, что курсор Pointer"):
            assert lst[7] == Cursor.POINTER, f"Курсор - {lst[7]}"
        with allure.step("Проверить, что открылась выпадашка"):
            assert self.check_cart_button_dropdown_open() == "true", "Выпадашка не открыта"

    def check_cart_button_dropdown_open(self):
        """Прверка отображения выпадашки у кнопки корзины."""

        return self.getting_attr("aria-expanded", *HeaderPageLocators.CART_BUTTON)

    @allure.step("Кликнуть на выпадающий список валют")
    def click_on_currency_drop_down(self):
        self.click_on_element(*HeaderPageLocators.CURRENCY_DROP_DOWN_BUTTON)
        display_css = self.get_css_property(*HeaderPageLocators.CURRENCY_DROP_DONW, "display")
        with allure.step(f"Проверить, что значение атрибута - block"):
            assert display_css == "block", f"Значение атрибута - {display_css}"

    @allure.step("Проверить значения валют в выпадающем списке")
    def check_currency_values(self, lst):
        elements = self._element(*HeaderPageLocators.CURRENCY_VALUES_BUTTONS, all=True)
        with allure.step("Получить список валют"):
            names = [i.text for i in elements]
            with allure.step(f"Проверить, что полученный список - {names} - совпадает с - {lst}"):
                for i in names:
                    assert i in lst

    @allure.step("Выбрать значение валюты")
    def choose_currency(self, value):
        self.click_on_currency_drop_down()
        elements = self._element(*HeaderPageLocators.CURRENCY_VALUES_BUTTONS, all=True)
        for i in range(len(elements)):
            element = self.get_text_of_element(*HeaderPageLocators.CURRENCY_VALUES_BUTTONS, index=i)
            if element == value:
                with allure.step(f"Кликнуть по значению валюты {value}"):
                    return self.click_on_element(*HeaderPageLocators.CURRENCY_VALUES_BUTTONS, index=i)

    @allure.step("Навести на раздел главного меню и проверить, что есть выпадашка")
    def check_dropdown_menu(self, menu_locator, dropdown_locator):
        self.mouse_move_to_element(*menu_locator)
        assert self.is_element_visible(*dropdown_locator)

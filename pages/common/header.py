import allure

from utils.allure_helper import attach
from utils.locators import HeaderPageLocators
from utils.styles import Border, Colors, Cursor, Gradients, SIZES
from base.base_page import BasePage


class Header(BasePage):

    @allure.step('Проверить видимость элементов на странице')
    def check_elements_visibility(self):
        """Проверка видимости элементов."""
        lst = [HeaderPageLocators.LOGO,
               HeaderPageLocators.MENU,
               HeaderPageLocators.CART_BUTTON,
               HeaderPageLocators.TOP_LINKS,
               HeaderPageLocators.SEARCH_FIELD]
        for i in lst:
            self.is_element_visible(*i)

    @allure.step('Ввести в поиск значение {value}')
    def search_input(self, value):
        """Ввод текста в поле поиска.

        :param value: искомое значение
        """
        self.input_text(*HeaderPageLocators.SEARCH_INPUT, value)

    @allure.step('Нажать кнопку поиска')
    def search_start(self):
        """Нажать кнопку поиска поиска."""
        self.click_on_element(*HeaderPageLocators.SEARCH_BUTTON)

    @allure.step('Перейти на страницу логина')
    def go_to_login_page(self):
        """Проверка перехода на страницу Логина."""
        self.click_on_element(*HeaderPageLocators.MY_ACCOUNT_LINK)
        self.click_on_element(*HeaderPageLocators.LOGIN_LINK)

    @allure.step('Проверить стили кнопки корзины')
    def check_cart_button_css(self):
        """Проверка стилей кнопки корзины без наведения."""
        lst = []
        with allure.step('Получить стили элемента'):
            for prop in ['font-size', 'line-height', 'color', 'background-color', 'background-image',
                         'border-top-color', 'border-right-color', 'border-bottom-color',
                         'border-left-color', 'border-radius', 'cursor']:
                lst.append(self.get_css_property(*HeaderPageLocators.CART_BUTTON, prop))
        with allure.step(f'Проверить, что шрифт {SIZES.SIZE_12}'):
            assert lst[0] == SIZES.SIZE_12, f'Размер текста - {lst[0]}'
        with allure.step(f'Проверить межстрочный интервал {SIZES.SIZE_18}'):
            assert lst[1] == SIZES.SIZE_18, f'Межстрочный интервал - {lst[1]}'
        with allure.step(f'Проверить, что цвет текста {Colors.WHITE}'):
            assert lst[2] == Colors.WHITE, f'Цвет текста - {lst[2]}'
        with allure.step(f'Проверить цвета фона {Colors.DARK_GRAY}'):
            assert lst[3] == Colors.DARK_GRAY, f'Цвет фона - {lst[3]}'
        with allure.step(f'Прверить фоновое изображение {Gradients.LIGHT_BLACK}'):
            assert lst[4] == Gradients.LIGHT_BLACK, f'Фоновое изображение - {lst[4]}'
        with allure.step(f'Проверить цвет верхней рамки {Colors.LIGHT_BLACK}'):
            assert lst[5] == Colors.LIGHT_BLACK, f'Цвет верхней рамки - {lst[5]}'
        with allure.step(f'Проверить цвет правой рамки {Colors.LIGHT_BLACK}'):
            assert lst[6] == Colors.LIGHT_BLACK, f'Цвет правой рамки - {lst[6]}'
        with allure.step(f'Проверить цвет нижней рамки {Colors.BLACK}'):
            assert lst[7] == Colors.BLACK, f'Цвет нижней рамки - {lst[7]}'
        with allure.step(f'Проверить цвет левой рамки {Colors.LIGHT_BLACK}'):
            assert lst[8] == Colors.LIGHT_BLACK, f'Цвет левой рамки - {lst[8]}'
        with allure.step(f'Проверить радиус скругления {SIZES.SIZE_4}'):
            assert lst[9] == SIZES.SIZE_4, f'Радиус скругления - {lst[9]}'
        with allure.step(f'Проверить, что курсор {Cursor.POINTER}'):
            assert lst[10] == Cursor.POINTER, f'Курсор - {lst[10]}'

    @allure.step('Проверить стили кнопки корзины при наведении')
    def check_cart_button_css_hover(self):
        """Проверка стилей кнопки корзины при наведении."""

        self.mouse_move_to_element(*HeaderPageLocators.CART_BUTTON)
        lst = []
        with allure.step('Получить стили элемента'):
            for prop in ['font-size', 'line-height', 'color', 'background-color', 'background-image',
                         'border-top-color', 'border-right-color', 'border-bottom-color',
                         'border-left-color', 'border-radius', 'cursor']:
                lst.append(self.get_css_property(*HeaderPageLocators.CART_BUTTON, prop))
        with allure.step(f'Проверить, что шрифт {SIZES.SIZE_12}'):
            assert lst[0] == SIZES.SIZE_12, f'Размер текста - {lst[0]}'
        with allure.step(f'Проверить межстрочный интервал {SIZES.SIZE_18}'):
            assert lst[1] == SIZES.SIZE_18, f'Межстрочный интервал - {lst[1]}'
        with allure.step(f'Проверить, что цвет текста {Colors.WHITE}'):
            assert lst[2] == Colors.WHITE, f'Цвет текста - {lst[2]}'
        with allure.step(f'Проверить цвета фона {Colors.LIGHT_BLACK}'):
            assert lst[3] == Colors.LIGHT_BLACK, f'Цвет фона - {lst[3]}'
        with allure.step(f'Прверить фоновое изображение {Gradients.MEDIUM_BLACK}'):
            assert lst[4] == Gradients.MEDIUM_BLACK, f'Фоновое изображение - {lst[4]}'
        with allure.step(f'Проверить цвет верхней рамки {Colors.LIGHT_BLACK}'):
            assert lst[5] == Colors.LIGHT_BLACK, f'Цвет верхней рамки - {lst[5]}'
        with allure.step(f'Проверить цвет правой рамки {Colors.LIGHT_BLACK}'):
            assert lst[6] == Colors.LIGHT_BLACK, f'Цвет правой рамки - {lst[6]}'
        with allure.step(f'Проверить цвет нижней рамки {Colors.BLACK}'):
            assert lst[7] == Colors.BLACK, f'Цвет нижней рамки - {lst[7]}'
        with allure.step(f'Проверить цвет левой рамки {Colors.LIGHT_BLACK}'):
            assert lst[8] == Colors.LIGHT_BLACK, f'Цвет левой рамки - {lst[8]}'
        with allure.step(f'Проверить радиус скругления {SIZES.SIZE_4}'):
            assert lst[9] == SIZES.SIZE_4, f'Радиус скругления - {lst[9]}'
        with allure.step(f'Проверить, что курсор {Cursor.POINTER}'):
            assert lst[10] == Cursor.POINTER, f'Курсор - {lst[10]}'

    @allure.step('Проверить стили кнопки корзины при клике')
    def check_cart_button_css_click(self):
        """Проверка стилей кнопки корзины при клике."""
        self.click_on_element(*HeaderPageLocators.CART_BUTTON)
        lst = []
        with allure.step('Получить стили элемента'):
            for prop in ['font-size', 'line-height', 'color', 'background-color', 'background-image',
                         'border', 'border-radius', 'cursor']:
                lst.append(self.get_css_property(*HeaderPageLocators.CART_BUTTON, prop))
        with allure.step(f'Проверить, что шрифт {SIZES.SIZE_12}'):
            assert lst[0] == SIZES.SIZE_12, f'Размер текста - {lst[0]}'
        with allure.step(f'Проверить межстрочный интервал {SIZES.SIZE_18}'):
            assert lst[1] == SIZES.SIZE_18, f'Межстрочный интервал - {lst[1]}'
        with allure.step(f'Проверить, что цвет текста {Colors.MEDIUM_GRAY}'):
            assert lst[2] == Colors.MEDIUM_GRAY, f'Цвет текста - {lst[2]}'
        with allure.step(f'Проверить цвета фона {Colors.WHITE}'):
            assert lst[3] == Colors.WHITE, f'Цвет фона - {lst[3]}'
        with allure.step(f'Прверить фоновое изображение - none'):
            assert lst[4] == 'none', f'Фоновое изображение - {lst[4]}'
        with allure.step(f'Проверить стиль рамки {Border.LIGHT_GRAY}'):
            assert lst[5] == Border.LIGHT_GRAY, f'Рамка - {lst[5]}'
        with allure.step(f'Проверить радиус скругления {SIZES.SIZE_4}'):
            assert lst[6] == SIZES.SIZE_4, f'Радиус скругления - {lst[6]}'
        with allure.step(f'Проверить, что курсор {Cursor.POINTER}'):
            assert lst[7] == Cursor.POINTER, f'Курсор - {lst[7]}'
        with allure.step('Проверить, что открылась выпадашка'):
            attach(self.browser)
            assert self.check_cart_button_dropdown_open() == 'true', 'Выпадашка не открыта'

    def check_cart_button_dropdown_open(self):
        """Прверка отображения выпадашки у кнопки корзины."""
        return self.getting_attr('aria-expanded', *HeaderPageLocators.CART_BUTTON)

    @allure.step('Кликнуть на выпадающий список валют')
    def click_on_currency_drop_down(self):
        """Клик по списку валют и проверка, что список раскрыт."""
        self.click_on_element(*HeaderPageLocators.CURRENCY_DROP_DOWN_BUTTON)
        display_css = self.get_css_property(*HeaderPageLocators.CURRENCY_DROP_DONW, 'display')
        with allure.step(f'Проверить, что значение атрибута {display_css} - block'):
            attach(self.browser)
            assert display_css == 'block', f'Значение атрибута - {display_css}'

    @allure.step('Проверить значения валют в выпадающем списке')
    def check_currency_values(self, lst):
        """Проверка значений валют.

        :param lst: список названий валют
        """
        elements = self._element_presence(*HeaderPageLocators.CURRENCY_VALUES_BUTTONS, all=True)
        names = [i.text for i in elements]
        for i in names:
            with allure.step(f'Проверить, что название {i} есть в {lst}'):
                attach(self.browser)
                assert i in lst, f'ФР - {names}, ОР - {lst}'

    @allure.step('Выбрать значение валюты {value}')
    def choose_currency(self, value):
        """Выбор значения валюты.

        :param value: значение валюты
        """
        self.click_on_currency_drop_down()
        elements = self._element_presence(*HeaderPageLocators.CURRENCY_VALUES_BUTTONS, all=True)
        for i in range(len(elements)):
            element = self._element_presence(*HeaderPageLocators.CURRENCY_VALUES_BUTTONS, i).text
            if element == value:
                with allure.step(f'Кликнуть по значению валюты {value}'):
                    self.click_on_element(*HeaderPageLocators.CURRENCY_VALUES_BUTTONS, i)

    @allure.step('Проверить выпадающие списки горизонтального меню')
    def check_dropdown_menu(self, lst):
        """Проверка выпадающих списков горизонтального меню.

        :param lst: список локторов пунктов меню и выпадающих списков меню
        """
        for i in lst:
            with allure.step(f'Навести курсок на пункт меню {i[0]}'):
                self.mouse_move_to_element(*i[0])
                attach(self.browser)
            with allure.step(f'Проверить выпадающее меню {i[1]}'):
                attach(self.browser)
                self.is_element_visible(*i[1])

    @allure.step('Перейти на страницу корзины')
    def go_to_cart_page(self):
        """Проверка перехода на страницу корзины."""
        self.click_on_element(*HeaderPageLocators.SHOPPING_CART_TOP_LINK)
        self.browser.implicitly_wait(1)

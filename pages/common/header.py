import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from helpers.allure_helper import attach
from helpers.locators import HeaderPageLocators
from helpers.styles import Border, Colors, Cursor, Gradients, SIZES
from helpers.waits import Element, Elements


class Header:
    def __init__(self, browser):
        self.browser = browser

    @property
    def cart_button(self):
        return WebDriverWait(self.browser, 5).until(Element(*HeaderPageLocators.CART_BUTTON))

    @property
    def cart_link(self):
        return WebDriverWait(self.browser, 5).until(Element(*HeaderPageLocators.SHOPPING_CART_TOP_LINK))

    @property
    def search_input(self):
        return WebDriverWait(self.browser, 5).until(Element(*HeaderPageLocators.SEARCH_INPUT))

    @property
    def search_button(self):
        return WebDriverWait(self.browser, 5).until(Element(*HeaderPageLocators.SEARCH_BUTTON))

    @property
    def account_link(self):
        return WebDriverWait(self.browser, 5).until(Element(*HeaderPageLocators.MY_ACCOUNT_LINK))

    @property
    def login_link(self):
        return WebDriverWait(self.browser, 5).until(Element(*HeaderPageLocators.LOGIN_LINK))

    @property
    def currency_dropdown_button(self):
        return WebDriverWait(self.browser, 5).until(Element(*HeaderPageLocators.CURRENCY_DROP_DOWN_BUTTON))

    @property
    def currency_dropdown(self):
        return WebDriverWait(self.browser, 5).until(Element(*HeaderPageLocators.CURRENCY_DROP_DONW))

    @property
    def currency_dropdown_values(self):
        return WebDriverWait(self.browser, 5).until(Elements(*HeaderPageLocators.CURRENCY_VALUES_BUTTONS))

    def currency_dropdown_value(self, idx):
        return WebDriverWait(self.browser, 5).until(Element(*HeaderPageLocators.CURRENCY_VALUES_BUTTONS, idx))

    @allure.step('Проверить видимость элементов на странице')
    def check_elements_visibility(self):
        """Проверка видимости элементов."""
        lst = [HeaderPageLocators.LOGO,
               HeaderPageLocators.MENU,
               HeaderPageLocators.CART_BUTTON,
               HeaderPageLocators.TOP_LINKS,
               HeaderPageLocators.SEARCH_FIELD]
        for i in lst:
            el = WebDriverWait(self.browser, 5).until(Element(*i))
            attach(self.browser)
            assert el.is_displayed(), f'Элемент {i} не отображается на странице'

    @allure.step('Осуществить поиск по значению {value}')
    def search(self, value):
        """Ввод текста в поле поиска.

        :param value: искомое значение
        """
        self.search_input.clear()
        self.search_input.send_keys(value)
        self.search_button.click()

    @allure.step('Перейти на страницу логина')
    def go_to_login_page(self):
        """Проверка перехода на страницу Логина."""
        self.account_link.click()
        self.login_link.click()

    @allure.step('Проверить стили кнопки корзины')
    def check_cart_button_css(self):
        """Проверка стилей кнопки корзины без наведения."""
        lst = []
        with allure.step('Получить стили элемента'):
            for prop in ['font-size', 'line-height', 'color', 'background-color', 'background-image',
                         'border-top-color', 'border-right-color', 'border-bottom-color',
                         'border-left-color', 'border-radius', 'cursor']:
                lst.append(self.cart_button.value_of_css_property(prop))
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
        ActionChains(self.browser).move_to_element(self.cart_button).perform()
        lst = []
        with allure.step('Получить стили элемента'):
            for prop in ['font-size', 'line-height', 'color', 'background-color', 'background-image',
                         'border-top-color', 'border-right-color', 'border-bottom-color',
                         'border-left-color', 'border-radius', 'cursor']:
                lst.append(self.cart_button.value_of_css_property(prop))
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
        self.cart_button.click()
        lst = []
        with allure.step('Получить стили элемента'):
            for prop in ['font-size', 'line-height', 'color', 'background-color', 'background-image',
                         'border', 'border-radius', 'cursor']:
                lst.append(self.cart_button.value_of_css_property(prop))
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
        return self.cart_button.get_attribute('aria-expanded')

    @allure.step('Кликнуть на выпадающий список валют')
    def click_on_currency_drop_down(self):
        """Клик по списку валют и проверка, что список раскрыт."""
        self.currency_dropdown_button.click()
        display_css = self.currency_dropdown.value_of_css_property('display')
        with allure.step(f'Проверить, что значение атрибута {display_css} - block'):
            attach(self.browser)
            assert display_css == 'block', f'Значение атрибута - {display_css}'

    @allure.step('Проверить значения валют в выпадающем списке')
    def check_currency_values(self, lst):
        """Проверка значений валют.

        :param lst: список названий валют
        """
        names = [i.text for i in self.currency_dropdown_values]
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
        for i in range(len(self.currency_dropdown_values)):
            element = self.currency_dropdown_value(i).text
            if element == value:
                with allure.step(f'Кликнуть по значению валюты {value}'):
                    self.currency_dropdown_value(i).click()

    @allure.step('Проверить выпадающие списки горизонтального меню')
    def check_dropdown_menu(self, lst):
        """Проверка выпадающих списков горизонтального меню.

        :param lst: список локторов пунктов меню и выпадающих списков меню
        """
        for i in lst:
            el_menu = WebDriverWait(self.browser, 5).until(Element(*i[0]))
            with allure.step(f'Навести курсок на пункт меню {i[0]}'):
                ActionChains(self.browser).move_to_element(el_menu).perform()
                attach(self.browser)
            with allure.step(f'Проверить выпадающее меню {i[1]}'):
                el_dropdown = WebDriverWait(self.browser, 5).until(Element(*i[1]))
                attach(self.browser)
                assert el_dropdown.is_displayed(), f'Элемент {i[1]} не отображается на странице'

    @allure.step('Перейти на страницу корзины')
    def go_to_cart_page(self):
        """Проверка перехода на страницу корзины."""
        self.cart_link.click()
        self.browser.implicitly_wait(1)

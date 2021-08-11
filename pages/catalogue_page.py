"""Модуль c методами для страницы Каталога."""

import allure
from pages.base_page import BasePage
from pages.locators import CataloguePageLocators


class CataloguePage(BasePage):
    """Класс с методами для страницы Каталога."""

    def add_to_compare(self, idx):
        """Добавление товара в сравнение. Возвращает название
        добавленного товара.
        """

        with allure.step(f"Получить название товара"):
            name = self.get_text_of_element(*CataloguePageLocators.ITEM_NAME, idx)
        with allure.step(f"Кликнуть на кнопку добавления в сравнение"):
            self.click_on_element(*CataloguePageLocators.COMPARE_BUTTON, idx)
        return name

    @allure.step("Кликнуть на кнопку Сравнения в алерте")
    def go_to_compare_page(self):
        """Клик по ссылке Сравнения."""

        self.click_on_element(*CataloguePageLocators.COMPARE_LINK)
        return self

    @allure.step("Проверить, что товар добавился к сравнению - значение в ссылке увеличилось на 1")
    def should_be_adding_in_compare_link(self, txt):
        """Проверка изменения количества товаров в сравнении
        после добавления в сравнение.

        :param txt: искомый текст
        """

        with allure.step("Получить текст из строки сравнения"):
            link_txt = self.get_text_of_element(*CataloguePageLocators.COMPARE_LINK)
        with allure.step("Сравнить тексты"):
            assert link_txt == f'Product Compare ({txt})', f"Текст - {link_txt}"

    @allure.step("Сортировать товары по {txt}")
    def select_by_text(self, txt):
        """Сортировка товаров по значению из списка (тексту).

        :param txt: значения в выпадающем списке
        """

        element = self.select_products(*CataloguePageLocators.SELECT_SORT)
        return element.select_by_visible_text(txt)

    @allure.step("Проверить, что товары отсортированы от A до Z")
    def check_sort_by_name_a_z(self):
        """Получение всех названий товаров после сортировки и проверка
        заданной сортировки."""

        elements = self._element(*CataloguePageLocators.ITEM_NAME, all=True)
        names = [i.text for i in elements]
        assert all(names[i] < names[i+1] for i in range(len(names)-1)), f"Порядок названий - {names}"

    @allure.step("Проверить, что товары отсортированы по возрастанию цены")
    def check_sort_by_price_low_high(self):
        """Получение всех цен товаров после сортировки и проверка
        заданной сортировки."""

        elements = self._element(*CataloguePageLocators.ITEM_PRICE, all=True)
        prices_with_tax = [i.text for i in elements]
        prices_without_tax = [i.split('\nEx')[0] for i in prices_with_tax]
        prices_in_float = [float(i.replace(',', '').replace('$', '')) for i in prices_without_tax]
        assert all(prices_in_float[i] <= prices_in_float[i+1] for i in range(len(prices_in_float)-1)), \
            f"Порядок цен - {prices_in_float}"

    def go_to_product_from_catalogue(self, index):
        """Клик по товару из каталога.
        Возвращает название товара.

        :param index: порядковый индекс элемента
        """

        with allure.step(f"Получить название товара с индексом {index}"):
            name = self.get_text_of_element(*CataloguePageLocators.ITEM_NAME, index)
        with allure.step(f"Кликнуть по превью товара с индексом {index}"):
            self.click_on_element(*CataloguePageLocators.ITEM_NAME, index)
        return name

    def add_to_wishlist(self, index):
        """Добавление товара в вишлист. Возвращает название
        добавленного товара.
        """

        with allure.step(f"Получить название товара с индексом {index}"):
            name = self.get_text_of_element(*CataloguePageLocators.ITEM_NAME, index)
        with allure.step(f"Кликнуть на кнопку добавления в Виш-лист с индексом {index}"):
            self.click_on_element(*CataloguePageLocators.WISH_LIST_BUTTON, index)
        return name

    @allure.step("Кликнуть на кнопку Логина в алерте")
    def click_login_from_alert(self):
        """Клик по кнопке Логина в алерте."""

        self.click_on_element(*CataloguePageLocators.LOGIN_LINK_IN_ALERT)
        return self

    @allure.step("Кликнуть на кнопку вида 'Список'")
    def click_list_view(self):
        """Клик по кнопке с видом списка и проверка изменения вида."""

        elements = self._element(*CataloguePageLocators.ITEM_CART, all=True)
        self.click_on_element(*CataloguePageLocators.LIST_VIEW_BUTTON)
        for i in range(len(elements)):
            attr = self.getting_attr("class", *CataloguePageLocators.ITEM_CART, i)
            assert "product-list" in attr, f"Значение атрибута -  {attr}"

    @allure.step("Кликнуть на кнопку вида 'Сетка'")
    def click_list_grid(self):
        """Клик по кнопке с видом сетки и проверка изменения вида."""

        elements = self._element(*CataloguePageLocators.ITEM_CART, all=True)
        self.click_on_element(*CataloguePageLocators.GRID_VIEW_BUTTON)
        for i in range(len(elements)):
            attr = self.getting_attr("class", *CataloguePageLocators.ITEM_CART, i)
            assert "product-grid" in attr, f"Значение атрибута -  {attr}"

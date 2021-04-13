"""Модуль c методами для страницы Каталога."""

import allure
from otus_opencart.pages.base_page import BasePage
from otus_opencart.pages.locators import CataloguePageLocators


class CataloguePage(BasePage):
    """Класс с методами для страницы Каталога."""

    @allure.step("Добавить товар к сравнению кликом на кнопку")
    def click_to_compare(self):
        """Добавление товара в сравнение."""

        self.click_on_element(*CataloguePageLocators.COMPARE_BUTTON)

    @allure.step("Проверить отображение алерта")
    def should_be_successful_alert(self):
        """Проверка отображения алерта после добавления товара в сравнение."""

        self.is_element_visible(*CataloguePageLocators.ALERT_SUCCESS)

    @allure.step("Проверить, что товар добавился к сравнению - значение в ссылке увеличилось на 1")
    def should_be_adding_in_compare_link(self, txt):
        """Проверка изменения количества товаров в сравнении
        после добавления в сравнение.

        :param txt: искомый текст
        """

        with allure.step("Получить текст из строки сравнения"):
            link_txt = self.get_text_of_element(*CataloguePageLocators.COMPARE_LINK)
        with allure.step("Сравнить тексты"):
            assert link_txt == txt, f"Текст - {link_txt}"

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

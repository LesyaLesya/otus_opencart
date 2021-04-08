"""Модуль c методами для страницы Каталога."""

import allure
from otus_opencart.pages.base_page import BasePage
from otus_opencart.pages.locators import CataloguePageLocators


class CataloguePage(BasePage):
    """Класс с методами для страницы Каталога."""

    @allure.step("Добавить товар к сравнению кликом на кнопку")
    def click_to_compare(self):
        """Добавление товара в сравнение."""

        self.is_element_visible(*CataloguePageLocators.FIRST_PRODUCT)
        self.click_on_element(*CataloguePageLocators.COMPARE_BUTTON)

    @allure.step("Проверить отображение алерта")
    def should_be_successful_alert(self):
        """Проверка отображения алерта после добавления товара в сравнение."""

        self.is_element_visible(*CataloguePageLocators.ALERT_SUCCESS, 0)

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

    def check_names_after_sort_by_name_a_z(self):
        """Проверка сортировки сравнением первой буквы первого и последнего товара в списке."""

        first_product, last_product = self.__get_first_last_names()
        with allure.step(f"Сравнить названия первого товара {first_product} "
                         f"и последнего товара {last_product}."
                         " Проверить, что товары отсортированы от A до Z"):
            assert last_product > first_product, \
                f"Название первого товара {first_product}," \
                f"Название последнего товара {last_product}"

    def __get_first_last_names(self):
        """Возвращает названия первого и последнего элементов в списке товаров."""

        with allure.step("Получить название первого товара"):
            first_product = self.get_text_of_element(*CataloguePageLocators.FIRST_PRODUCT)
        with allure.step("Получить название последнего товара"):
            last_product = self.get_text_of_element(*CataloguePageLocators.LAST_PRODUCT)
        return first_product, last_product

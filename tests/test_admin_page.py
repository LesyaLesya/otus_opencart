"""Модуль с тестами для Административной страницы."""


import allure
import pytest

from helpers.urls import URLS
from pages.admin_page import AdminPage


@allure.feature('Административная страница')
@pytest.mark.admin_page
class TestAdminPage:
    """Тесты административной страницы."""

    @allure.story('Элементы страницы')
    @allure.title('Проверка видимости элементов на странице')
    @allure.link('#', name='User story')
    def test_visibility_of_elements_on_admin_login_page(self, browser, url):
        """Тестовая функция для проверки видимости элементов на странице Каталога.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = AdminPage(browser, url)
        page.open_url(path=URLS.ADMIN_PAGE)
        page.check_elements_visibility()

    @allure.story('Авторизация в админке')
    @allure.title('Валидные креденшелы')
    @allure.link('#', name='User story')
    def test_login_valid(self, browser, url):
        """Тестовая функция для проверки логина в админку с валидными креденшелами.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = AdminPage(browser, url)
        page.open_url(path=URLS.ADMIN_PAGE)
        page.login('user', 'bitnami')
        page.is_title_correct('Dashboard')

    @allure.story('Авторизация в админке')
    @allure.title('Невалидные креденшелы')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('login, passw',
                             [('test', 'test'), ('123', '')])
    def test_login_failed(self, browser, url, login, passw):
        """Тестовая функция для проверки логина в админку с невалидными креденшелами.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        :param login: передаваемый логин
        :param passw: передаваемый пароль
        """
        page = AdminPage(browser, url)
        page.open_url(path=URLS.ADMIN_PAGE)
        page.login(login, passw)
        page.check_fail_login_alert()

    @allure.story('Выход из админки')
    @allure.title('Выход из админки')
    @allure.link('#', name='User story')
    def test_logout(self, browser, url):
        """Тестовая функция для проверки разлогина из админки.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = AdminPage(browser, url)
        page.open_url(path=URLS.ADMIN_PAGE)
        page.login('user', 'bitnami')
        page.logout()
        page.check_successful_logout_text()

    @allure.story('Элементы админки')
    @allure.title('Отображение таблицы с товарами в админке')
    @allure.link('#', name='User story')
    def test_get_products_table(self, browser, url):
        """Тестовая функция для проверки отображения таблицы с товарами в админке.

        :param browser: фикстура для запуска драйвера
        :param url: фикстура с урлом тестируемого ресурса
        """
        page = AdminPage(browser, url)
        page.open_url(path=URLS.ADMIN_PAGE)
        page.login('user', 'bitnami')
        page.get_product_table()
        page.check_products_table()

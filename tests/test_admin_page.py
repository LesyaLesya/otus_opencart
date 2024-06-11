"""Модуль с тестами для Административной страницы."""


import allure
import pytest
from base.base_test import BaseTest


@allure.feature('Административная страница')
@pytest.mark.admin_page
class TestAdminPage(BaseTest):
    """Тесты административной страницы."""

    @allure.story('Элементы страницы')
    @allure.title('Проверка видимости элементов на странице')
    @allure.link('#', name='User story')
    def test_visibility_of_elements_on_admin_login_page(self):
        """Тестовая функция для проверки видимости элементов на странице Каталога.

        """
        self.admin_page.open_url()
        self.admin_page.check_elements_visibility()

    @allure.story('Авторизация в админке')
    @allure.title('Валидные креденшелы')
    @allure.link('#', name='User story')
    def test_login_valid(self):
        """Тестовая функция для проверки логина в админку с валидными креденшелами.

        """
        self.admin_page.open_url()
        self.admin_page.enter_login('user')
        self.admin_page.enter_password('bitnami')
        self.admin_page.click_login()
        self.admin_page.is_title_correct(self.admin_page.TITLE)

    @allure.story('Авторизация в админке')
    @allure.title('Невалидные креденшелы')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('login, passw',
                             [('test', 'test'), ('123', '')])
    def test_login_failed(self, login, passw):
        """Тестовая функция для проверки логина в админку с невалидными креденшелами.

        :param login: передаваемый логин
        :param passw: передаваемый пароль
        """
        self.admin_page.open_url()
        self.admin_page.enter_login(login)
        self.admin_page.enter_password(passw)
        self.admin_page.click_login()
        self.alert.check_danger_alert()

    @allure.story('Выход из админки')
    @allure.title('Выход из админки')
    @allure.link('#', name='User story')
    def test_logout(self):
        """Тестовая функция для проверки разлогина из админки.

        """
        self.admin_page.open_url()
        self.admin_page.enter_login('user')
        self.admin_page.enter_password('bitnami')
        self.admin_page.click_login()
        self.admin_page.logout()
        self.admin_page.check_successful_logout_text()

    @allure.story('Элементы админки')
    @allure.title('Отображение таблицы с товарами в админке')
    @allure.link('#', name='User story')
    def test_get_products_table(self):
        """Тестовая функция для проверки отображения таблицы с товарами в админке.

        """
        self.admin_page.open_url()
        self.admin_page.enter_login('user')
        self.admin_page.enter_password('bitnami')
        self.admin_page.click_login()
        self.admin_page.get_product_table()
        self.admin_page.check_products_table()

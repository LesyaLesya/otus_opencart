"""Модуль с тестами для страницы Аккуанта."""

import allure
import pytest

from utils.locators import LoginPageLocators
from base.base_test import BaseTest


@allure.feature('Страница логаута из аккаунта')
@pytest.mark.account_page
@pytest.mark.account_logout_page
class TestAccountLogoutPage(BaseTest):
    """Тесты страницы Логаута из аккаунта."""

    @allure.story('Логаут')
    @allure.title('Логаут из правого блока')
    @allure.link('#', name='User story')
    def test_logout_from_right_block(self, fixture_create_delete_user):
        """Тестовая функция для проверки логаута из правого блока.

        :param fixture_create_delete_user: фикстура создания и удаления тестового пользователя
        """
        email, firstname, lastname, telephone, user_id = fixture_create_delete_user
        self.login_page.open_url()
        self.login_page.login_user(email)
        self.account_page.logout_from_right_block()
        self.logout_page.is_title_correct(self.logout_page.TITLE)
        self.logout_page.check_text_after_logout()
        self.logout_page.check_right_block_after_logout()
        self.logout_page.click_my_account()
        self.login_page.is_element_visible(*LoginPageLocators.NEW_CUSTOMER_FORM)
        self.login_page.is_element_visible(*LoginPageLocators.OLD_CUSTOMER_FORM)


@allure.feature('Страница логина')
@pytest.mark.account_page
@pytest.mark.account_login_page
class TestAccountLoginPage(BaseTest):
    """Тесты страницы логина."""

    @allure.story('Элементы страницы')
    @allure.title('Проверка видимости элементов на странице')
    @allure.link('#', name='User story')
    def test_visibility_of_elements_on_login_page(self):
        """Тестовая функция для проверки видимости элементов на странице Логина.

        """
        self.login_page.open_url()
        self.login_page.check_elements_visibility()

    @allure.story('Проверка авторизации в ЛК')
    @allure.title('Успешная авторизация')
    @allure.link('#', name='User story')
    def test_success_login(self, fixture_create_delete_user):
        """Тестовая функция для проверки успешного входа пользователья в ЛК.

        :param fixture_create_delete_user: фикстура создания и удаления тестового пользователя
        """
        email, firstname, lastname, telephone, user_id = fixture_create_delete_user
        self.login_page.open_url()
        self.login_page.login_user(email)
        self.account_page.is_title_correct(self.account_page.TITLE)

    @allure.story('Проверка авторизации в ЛК')
    @allure.title('Неуспешная авторизация - невалидный email')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('email', ['123', ''])
    def test_fail_login_invalid_email(self, email):
        """Тестовая функция для проверки неуспешного входа пользователья в ЛК -
        некорректный email.

        :param email: email
        """
        self.login_page.open_url()
        self.login_page.login_user(email)
        self.alert.check_danger_alert()

    @allure.story('Проверка авторизации в ЛК')
    @allure.title('Неуспешная авторизация - невалидный пароль')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('passw', ['oops', ''])
    def test_fail_login_invalid_password(self, passw, fixture_create_delete_user):
        """Тестовая функция для проверки неуспешного входа пользователья в ЛК -
        некорректный пароль.


        :param passw: пароль
        :param fixture_create_delete_user: фикстура создания и удаления тестового пользователя
        """
        email, firstname, lastname, telephone, user_id = fixture_create_delete_user
        self.login_page.open_url()
        self.login_page.login_user(email, passw)
        self.alert.check_danger_alert()


@allure.feature('Страница регистрации')
@pytest.mark.account_page
@pytest.mark.account_register_page
class TestAccountRegisterPage(BaseTest):
    """Тесты страницы регистрации."""

    @allure.story('Элементы страницы')
    @allure.title('Проверка видимости элементов на странице')
    @allure.link('#', name='User story')
    def test_visibility_of_elements_on_register_page(self):
        """Тестовая функция для проверки видимости элементов на странице Регистрации.

        """
        self.register_page.open_url()
        self.register_page.check_elements_visibility()

    @allure.story('Проверка регистрации нового пользователя')
    @allure.title('Успешная регистрация')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('firstname, lastname, email, tel, password, confirm, radio_idx',
                             [('Test1', 'Test2', 'test@test12.com', '89991112233', 'test', 'test', 0),
                              ('Пользователь', 'Фамилия', 'a1@test.ru', '11111111', '12345', '12345', 1)])
    def test_success_register_new_user(
            self, firstname, lastname, email, tel, password, confirm, radio_idx):
        """Тестовая функция для проверки успешной регистрации нового пользователя.

            :param firstname: имя юзера
            :param lastname: фамилия юзера
            :param email: email юзера
            :param tel: телефон юзера
            :param password: пароль
            :param confirm: повторно пароль
            :param radio_idx: согласие на рассылку
            """
        self.register_page.open_url()
        self.register_page.register_user(
            firstname, lastname, email, tel, password, confirm, radio_idx)
        self.account_page.is_title_correct(self.account_page.SUCCESS_CREATE_ACCOUNT)
        self.db.check_user_in_db(self.db_connection, firstname, lastname, email, tel, radio_idx)

    @allure.story('Проверка регистрации нового пользователя')
    @allure.title('Пустые поля')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('firstname, lastname, email, tel, password, confirm, radio_idx',
                             [(None, 'Test2', 'test@test13.com', '89991112233', 'test', 'test', 0),
                              ('Test1', None, 'test@test14.com', '89991112233', 'test', 'test', 0),
                              ('Test1', 'Test2', None, '89991112233', 'test', 'test', 0),
                              ('Test1', 'Test2', 'test@test15.com', None, 'test', 'test', 0),
                              ('Test1', 'Test2', 'test@test16.com', '89991112233', None, 'test', 0),
                              ('Test1', 'Test2', 'test@test17.com', '89991112233', 'test', None, 0)])
    def test_register_new_user_empty_fields(
            self, firstname, lastname, email, tel, password, confirm, radio_idx):
        """Тестовая функция для проверки регистрации нового пользователя - пустые поля.

            :param firstname: имя юзера
            :param lastname: фамилия юзера
            :param email: email юзера
            :param tel: телефон юзера
            :param password: пароль
            :param confirm: повторно пароль
            :param radio_idx: согласие на рассылку
            """
        self.register_page.open_url()
        self.register_page.register_user(
            firstname, lastname, email, tel, password, confirm, radio_idx)
        self.register_page.is_title_correct(self.register_page.TITLE)
        if not email:
            self.db.check_user_not_in_db(self.db_connection, firstname=firstname, lastname=lastname, tel=tel)
            self.register_page.check_fail_register_without_email()
        else:
            self.db.check_user_not_in_db(self.db_connection, email)
            if not firstname:
                self.register_page.check_fail_register_without_firstname()
            if not lastname:
                self.register_page.check_fail_register_without_lastname()
            if not tel:
                self.register_page.check_fail_register_without_telephone()
            if not password:
                self.register_page.check_fail_register_without_password()
            if not confirm:
                self.register_page.check_fail_register_without_confirm()

    @allure.story('Проверка регистрации нового пользователя')
    @allure.title('Не принятие пользовательского соглашения')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('firstname, lastname, email, tel, password, confirm, radio_idx, privacy',
                             [('Test1', 'Test2', 'test@test12.com', '89991112233', 'test', 'test', 0, False)])
    def test_register_new_user_without_accept_privacy_policy(
            self, firstname, lastname, email, tel, password, confirm, radio_idx, privacy):
        """Тестовая функция для проверки регистрации нового пользователя - пустые поля.

            :param firstname: имя юзера
            :param lastname: фамилия юзера
            :param email: email юзера
            :param tel: телефон юзера
            :param password: пароль
            :param confirm: повторно пароль
            :param radio_idx: согласие на рассылку
            :param privacy: чек-бокс privacy policy
            """
        self.register_page.open_url()
        self.register_page.register_user(
            firstname, lastname, email, tel, password, confirm, radio_idx, privacy)
        self.register_page.is_title_correct(self.register_page.TITLE)
        self.db.check_user_not_in_db(self.db_connection, email)
        self.alert.check_error_text(self.register_page.REGISTER_PRIVACY_ERROR)


@allure.feature('Страница редактирования аккаунта')
@pytest.mark.account_page
@pytest.mark.account_edit_page
class TestAccountEditPage(BaseTest):
    """Тесты страницы редактирования аккаунта."""

    @allure.story('Редактирование данных аккаунта')
    @allure.title('Проверка изменения имени пользователя')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('new_firstname', ['lala', '123'])
    def test_change_firstname_user(self, fixture_create_delete_user, new_firstname):
        """Тестовая функция для проверки изменения имени пользователя на странице редактирования аккаунт.

        :param fixture_create_delete_user: фикстура создания и удаления тестового пользователя
        :param new_firstname: имя пользователя
        """
        email, firstname, lastname, telephone, user_id = fixture_create_delete_user
        self.login_page.open_url()
        self.login_page.login_user(email)
        self.account_page.click_edit_account()
        self.edit_account_page.is_title_correct(self.edit_account_page.TITLE)
        self.edit_account_page.change_firstname(new_firstname)
        self.edit_account_page.save_changes()
        self.alert.check_success_alert()
        self.account_page.click_edit_account()
        self.edit_account_page.check_firstname(new_firstname)
        self.edit_account_page.check_lastname(lastname)
        self.edit_account_page.check_email(email)
        self.edit_account_page.check_phone(telephone)
        self.db.check_user_in_db(self.db_connection, new_firstname, lastname, email, telephone)

    @allure.story('Редактирование данных аккаунта')
    @allure.title('Проверка, что изменения не были сохранены при нажатии на back')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('new_firstname', ['lala'])
    def test_change_firstname_user_back(self, fixture_create_delete_user, new_firstname):
        """Тестовая функция для проверки, что изменения не были сохранены при
        нажатии на back на странице редактирования аккаунта.

        :param fixture_create_delete_user: фикстура создания и удаления тестового пользователя
        :param new_firstname: имя пользователя
        """
        email, firstname, lastname, telephone, user_id = fixture_create_delete_user
        self.login_page.open_url()
        self.login_page.login_user(email)
        self.account_page.click_edit_account()
        self.edit_account_page.is_title_correct(self.edit_account_page.TITLE)
        self.edit_account_page.change_firstname(new_firstname)
        self.edit_account_page.press_back()
        self.account_page.click_edit_account()
        self.edit_account_page.check_firstname(firstname)
        self.edit_account_page.check_lastname(lastname)
        self.edit_account_page.check_email(email)
        self.edit_account_page.check_phone(telephone)
        self.db.check_user_in_db(self.db_connection, firstname, lastname, email, telephone)


@allure.feature('Страница вишлиста')
@pytest.mark.account_page
@pytest.mark.account_wishlist
class TestAccountWishlist(BaseTest):
    """Тесты страницы вишлиста."""

    @allure.story('Редактирование вишлиста')
    @allure.title('Проверка пустого вишлиста')
    @allure.link('#', name='User story')
    def test_check_empty_wishlist(self, fixture_create_delete_user):
        """Тестовая функция для проверки пустого вишлиста.

        :param fixture_create_delete_user: фикстура создания и удаления тестового пользователя
        """
        email, firstname, lastname, telephone, user_id = fixture_create_delete_user
        self.login_page.open_url()
        self.login_page.login_user(email)
        self.wishlist_page.open_wishlist()
        self.wishlist_page.is_title_correct(self.wishlist_page.TITLE)
        self.wishlist_page.check_empty_wish_list()

    @allure.story('Редактирование вишлиста')
    @allure.title('Проверка удаления товара из вишлиста')
    @allure.link('#', name='User story')
    def test_delete_item_from_wishlist(self, fixture_create_delete_user):
        """Тестовая функция для проверки удаления товара из вишлиста.

        :param fixture_create_delete_user: фикстура создания и удаления тестового пользователя
        """
        email, firstname, lastname, telephone, user_id = fixture_create_delete_user
        self.login_page.open_url()
        self.login_page.login_user(email)
        self.catalogue_page.open_url()
        name1, item_id1 = self.catalogue_page.add_to_wishlist(0)
        name2, item_id2 = self.catalogue_page.add_to_wishlist(1)
        self.wishlist_page.open_wishlist()
        self.wishlist_page.check_items_in_wish_list([name1, name2], 2)
        self.wishlist_page.del_items_from_wish_list(idx=0)
        self.alert.check_success_alert(txt=self.wishlist_page.WISHLIST_CHANGE)
        self.wishlist_page.check_items_in_wish_list(name1, 1)
        self.db.check_items_in_wishlist_in_db(self.db_connection, user_id, 1, item_id1)

    @allure.story('Редактирование вишлиста')
    @allure.title('Проверка удаления всех товаров из вишлиста')
    @allure.link('#', name='User story')
    def test_delete_all_items_from_wishlist(self, fixture_create_delete_user):
        """Тестовая функция для проверки удаления всех товаров из вишлиста.

        :param fixture_create_delete_user: фикстура создания и удаления тестового пользователя
        """
        email, firstname, lastname, telephone, user_id = fixture_create_delete_user
        self.login_page.open_url()
        self.login_page.login_user(email)
        self.catalogue_page.open_url()
        name1, item_id1 = self.catalogue_page.add_to_wishlist(0)
        name2, item_id2 = self.catalogue_page.add_to_wishlist(1)
        self.wishlist_page.open_wishlist()
        self.wishlist_page.check_items_in_wish_list([name1, name2], 2)
        self.wishlist_page.del_items_from_wish_list(all=True)
        self.wishlist_page.check_empty_wish_list()
        self.db.check_empty_wishlist_in_db(self.db_connection, user_id)

"""Модуль с методами для работы с тестовыми данными БД."""

import allure
import time

from helpers import db_queries
from helpers.db_queries import (
    delete_user, del_item_in_wishlist_for_user, del_all_items_in_wishlist_for_user)


@allure.step('Проверить, что пользователь не появился в БД')
def check_user_not_in_db(db_connection, email=None, firstname=None, lastname=None, tel=None):
    """Проверка пользователя в БД."""

    result = db_queries.get_new_user(db_connection, email, firstname, lastname, tel)
    assert len(result) == 0, f'Найдено записей {len(result)}'


@allure.step(
    'Проверить, что пользователь появился в БД - с email {email}, '
    'именем {firstname}, фамилией {lastname}, телефоном {tel}')
def check_user_in_db(db_connection, firstname, lastname, email, tel, radio_idx=None):
    try:
        result = db_queries.get_new_user(db_connection, email)
        firstname_db = result[0][4]
        lastname_db = result[0][5]
        email_db = result[0][6]
        tel_db = result[0][7]
        newsletter_db = result[0][13]
        active_db = result[0][17]
        user_id = result[0][0]
        assert firstname_db == firstname, f'Имя пользователя в базе {firstname_db}, ОР {firstname}'
        assert lastname_db == lastname, f'Фамилия пользователя в базе {lastname_db}, ОР {lastname}'
        assert email_db == email, f'Email пользователя в базе {email_db}, ОР {email}'
        assert tel_db == tel, f'Телефон пользователя в базе {tel_db}, ОР {tel}'
        assert active_db == 1, f'Активность пользователя в базе {active_db}, ОР 1'
        if radio_idx == 0:
            assert newsletter_db == 1, f'Рассылка пользователя в базе {newsletter_db}, ОР 1'
        elif radio_idx == 1:
            assert newsletter_db == 0, f'Рассылка пользователя в базе {newsletter_db}, ОР 0'
        else:
            pass
    finally:
        delete_user(db_connection, user_id)


@allure.step('Проверить, что ревью НЕ появилось в БД')
def check_review_not_in_db(db_connection, author, text):
    """Проверить, что ревью НЕ появилось в БД."""

    time.sleep(3)
    result = db_queries.get_review(db_connection, author, text)
    assert not result, f'Записей найдено - {result}'


@allure.step('Проверить, что ревью появилось в БД - автор {author}, текст {text}')
def check_review_in_db(db_connection, author, text):
    try:
        time.sleep(3)
        result = db_queries.get_review(db_connection, author, text)
        assert result > 0, f'Записи не найдены - {result}'
    finally:
        db_queries.delete_review(db_connection, author, text)


@allure.step('Проверить, что товар {item_id} появился в вишлисте у юзера {user_id} в БД')
def check_item_in_wishlist_in_db(db_connection, user_id, item_id):
    """Проверка записи о товаре в вишлисте в БД."""

    try:
        result = db_queries.get_item_in_wishlist(db_connection, user_id, item_id)
        user_id_db = result[0][0]
        item_id_db = result[0][1]
        assert user_id_db == user_id, f'ID пользователя в базе {user_id_db}, ОР {user_id}'
        assert item_id_db == item_id, f'ID товара в базе {item_id_db}, ОР {item_id}'
    finally:
        del_item_in_wishlist_for_user(db_connection, user_id, item_id)


@allure.step('Проверить, что товар {item_id} появился в вишлисте у юзера {user_id} в БД')
def check_items_in_wishlist_in_db(db_connection, user_id, l, item_id):
    """Проверка записи о товарах в вишлисте в БД."""

    try:
        result = db_queries.get_all_items_in_wishlist_for_user(db_connection, user_id)
        assert len(result) == l, f'Количество товаров в вишлисте {len(result)}'
        if type(item_id) == list:
            for i in item_id:
                assert i in result, f'Название {i}, названия продуктов в вишлисте {result}'
        else:
            assert item_id == result[0], f'{item_id} нет в {result}'
    finally:
        del_all_items_in_wishlist_for_user(db_connection, user_id)


@allure.step('Проверить, что в БД у юзера {user_id} нет избранных товаров')
def check_empty_wishlist_in_db(db_connection, user_id):
    """Проверка записи о товаре в вишлисте в БД."""

    result = db_queries.get_all_items_in_wishlist_for_user(db_connection, user_id)
    assert len(result) == 0, f'Найдено записей {len(result)}'

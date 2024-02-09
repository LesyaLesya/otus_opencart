"""Модуль с запросами к БД."""

import allure


@allure.step('Создать тестового пользователя с email {email}, именем {fistname}, фамилией {lastname}')
def create_test_user(connection, email, fistname, lastname, telephone):
    """Создает тестового пользователя и возвращает его email."""

    query = 'INSERT INTO oc_customer ' \
            '(customer_group_id, store_id, language_id, firstname, lastname, email, telephone, fax, password, salt, ' \
            'newsletter, custom_field, ip, status, safe, token, code, address_id, date_added) ' \
            'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

    e_mail = email
    fistname = fistname
    lastname = lastname
    telephone = telephone
    test_password = '49dcc5aacf9491668e729c0c46bc815988f641e4'
    salt = 'VGNUpQvgV'
    data = [1, 0, 1, fistname, lastname, e_mail, telephone,
            0, test_password, salt, 1, '12', '123.123.123.123',
            1, 0, '', '', 0, '2020-12-05 23:27:44']
    connection.execute(query, data)
    allure.attach(name=email, body=email)


@allure.step('Получить id пользователя с email {email} и firstname {firstname}')
def get_user_id(connection, email, firstname, lastname, telephone):
    """Удаление тестового пользователя."""

    query = 'SELECT customer_id FROM oc_customer WHERE firstname = %s and email = %s and lastname = %s and telephone = %s'
    data = [firstname, email, lastname, telephone]
    connection.execute(query, data)
    user_id = connection.fetchall()
    return user_id[0][0]


@allure.step('Удалить тестового пользователя с id {user_id}')
def delete_user(connection, user_id):
    """Удаление тестового пользователя."""

    query = 'DELETE FROM oc_customer WHERE customer_id = %s'
    data = [user_id]
    connection.execute(query, data)


@allure.step('Получить тестовый отзыв автора {author} с текстом {text}')
def get_review(connection, author, text):
    """Получение записи о ревью."""

    query = 'SELECT * FROM oc_review WHERE oc_review.author = %s and oc_review.text = %s'
    result = 0
    data = [author, text]
    connection.execute(query, data)
    db_data = connection.fetchall()
    for _ in db_data:
        result = result + 1
    return result


@allure.step('Удалить тестовый отзыв автора {author} с текстом {text}')
def delete_review(connection, author, text):
    """Удаление ревью."""

    query = 'DELETE FROM oc_review WHERE oc_review.author = %s and oc_review.text = %s'
    data = [author, text]
    connection.execute(query, data)


@allure.step(
    'Получить пользователя с email {email}, именем {firstname}, фамилией {lastname}, телефоном {tel}')
def get_new_user(connection, email=None, firstname=None, lastname=None, tel=None):
    """Получение записи о пользователе."""
    query = ''
    data = []
    if email:
        query = 'SELECT * FROM oc_customer WHERE oc_customer.email = %s'
        data = [email]
    if firstname and lastname and tel:
        query = 'SELECT * FROM oc_customer WHERE oc_customer.firstname = %s and oc_customer.lastname = %s and oc_customer.telephone = %s'
        data = [firstname, lastname, tel]
    connection.execute(query, data)
    db_data = connection.fetchall()
    return db_data


@allure.step('Получить запись в БД о товаре {item_id} в вишлисте юзера {user_id}')
def get_item_in_wishlist(connection, user_id, item_id):
    """Получение записи о товаре в вишлисте пользователя."""

    query = 'SELECT * FROM oc_customer_wishlist WHERE customer_id = %s and product_id = %s'
    data = [user_id, item_id]
    connection.execute(query, data)
    db_data = connection.fetchall()
    return db_data


@allure.step('Получить записи в БД о всех товарах в вишлисте юзера {user_id}')
def get_all_items_in_wishlist_for_user(connection, user_id):
    """Получение записей о всех товарах в вишлисте пользователя."""

    query = 'SELECT product_id FROM oc_customer_wishlist WHERE customer_id = %s'
    data = [user_id]
    result = []
    connection.execute(query, data)
    db_data = connection.fetchall()
    for i in db_data:
        result.append(i[0])
    return result


@allure.step('Удалить запись в БД о товаре {item_id} в вишлисте юзера {user_id}')
def del_item_in_wishlist_for_user(connection, user_id, item_id):
    """Удаление записи о  товаре в вишлисте юзера."""

    query = 'DELETE FROM oc_customer_wishlist WHERE customer_id = %s and product_id = %s'
    data = [user_id, item_id]
    connection.execute(query, data)


@allure.step('Удалить все записи в БД о всех товарах в вишлисте юзера {user_id}')
def del_all_items_in_wishlist_for_user(connection, user_id):
    """Удаление записи о всех товарах в вишлисте юзера."""

    query = 'DELETE FROM oc_customer_wishlist WHERE customer_id = %s'
    data = [user_id]
    connection.execute(query, data)

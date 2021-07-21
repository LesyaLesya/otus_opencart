"""Модуль с методами для генерации тестовых данных."""

import allure


@allure.step("Создать тестового пользователя")
def create_test_user(connection, email):
    """Создает тестового пользователя и возвращает его email."""
    query = 'INSERT INTO oc_customer ' \
            '(customer_group_id, store_id, language_id, firstname, lastname, email, telephone, fax, password, salt, newsletter, custom_field, ip, status, safe, token, code, address_id, date_added) ' \
            'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

    e_mail = email
    fistname = "TEST1"
    lastname = "TEST1"
    test_password = "49dcc5aacf9491668e729c0c46bc815988f641e4"
    salt = "VGNUpQvgV"
    data = [1, 0, 1, fistname, lastname, e_mail, 123456,
            0, test_password, salt, 1, "12", "123.123.123.123",
            1, 0, "", "", 0, "2020-12-05 23:27:44"]

    connection.cursor().execute(query, data)
    connection.commit()
    allure.attach(name=email, body=email)
    return email


@allure.step("Удалить тестового пользователя")
def delete_user(connection, email):
    """Удаление тестового пользователя."""
    query = "DELETE FROM oc_customer WHERE firstname = 'TEST1' and email = %s"
    data = [email]
    connection.cursor().execute(query, data)
    connection.commit()


@allure.step("Получить тестовый отзыв")
def get_review(connection, author, text):
    """Получение записи о ревью."""
    query = "SELECT * FROM oc_review WHERE oc_review.author = %s and oc_review.text = %s"
    result = 0
    data = [author, text]
    with connection.cursor() as cursor:
        cursor.execute(query, data)
        db_data = cursor.fetchall()
        for _ in db_data:
            result = result + 1
    return result


@allure.step("Удалить тестовый отзыв")
def delete_review(connection, author, text):
    """Удаление ревью."""
    query = "DELETE FROM oc_review WHERE oc_review.author = %s and oc_review.text = %s"
    data = [author, text]
    connection.cursor().execute(query, data)
    connection.commit()

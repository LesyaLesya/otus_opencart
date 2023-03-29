"""Модуль c методами для Алертов"""

import allure

from helpers import allure_helper
from helpers.locators import AlertsLocators
from pages.base_page import BasePage


class AlertPage(BasePage):
    """Класс с методами для алертов."""

    @allure.step('Проверить, что выведен алерт с ошибкой авторизации')
    def check_fail_login_alert(self):
        """Проверка видимости алерта."""
        self.is_element_visible(*AlertsLocators.FAIL_LOGIN_ALERT)

    @allure.step('Кликнуть на кнопку Логина в алерте')
    def click_login_from_alert(self):
        """Клик по кнопке Логина в алерте."""
        self.click_on_element(*AlertsLocators.LINK_LOGIN_ALERT)

    @allure.step('Кликнуть на кнопку в алерте')
    def click_link_from_alert(self):
        """Клик по кнопке Сравнения в алерте."""
        self.click_on_element(*AlertsLocators.LINK_ALERT)

    @allure.step('Проверить алерт при пустом отзыве')
    def check_error_visibility_review(self):
        """Проверить алерт при пустом отзыве."""
        self.is_element_visible(*AlertsLocators.DANGER_ALERT)

    @allure.step('Проверить сообщение об ошибке при пустом отзыве')
    def check_error_text_empty_review(self):
        """Проверить сообщение об ошибке при пустом отзыве."""
        error_text = self.get_text_of_element(*AlertsLocators.DANGER_ALERT)
        with allure.step(
                'Проверить, что текст ошибки при пустом отзыве - Warning: Review Text must be between 25 and 1000 characters!'):
            assert error_text == 'Warning: Review Text must be between 25 and 1000 characters!', \
                f'Текст ошибки {error_text}'

    @allure.step('Проверить сообщение об ошибке при пустом авторе отзыва')
    def check_error_text_empty_author_review(self):
        """Проверить сообщение об ошибке при пустом авторе отзыва."""
        error_text = self.get_text_of_element(*AlertsLocators.DANGER_ALERT)
        with allure.step(
                'Проверить, что текст ошибки при пустом авторе - Warning: Review Name must be between 3 and 25 characters!'):
            assert error_text == 'Warning: Review Name must be between 3 and 25 characters!', \
                f'Текст ошибки {error_text}'

    @allure.step('Проверить сообщение об ошибке при пустом рейтинге отзыва')
    def check_error_text_empty_rating_review(self):
        """Проверить сообщение об ошибке при пустом рейтинге отзыва."""
        error_text = self.get_text_of_element(*AlertsLocators.DANGER_ALERT)
        with allure.step(
                'Проверить, что текст ошибки при пустом авторе - Warning: Please select a review rating!'):
            assert error_text == 'Warning: Please select a review rating!', \
                f'Текст ошибки {error_text}'

    @allure.step('Проверить видимость успешного алерта')
    def check_success_alert(self):
        """Вывод успешного алерта."""
        self.is_element_visible(*AlertsLocators.SUCCESS_ALERT)

    @allure.step('Проверить, что выведена ошибка  - принятие пользовательского соглашения обязательно')
    def check_fail_register_without_accept_privacy_policy(self):
        """Проверка отображения ошибки регистрации без принятия пользовательского соглашения."""
        self.is_element_visible(*AlertsLocators.DANGER_ALERT)
        error_text = self.get_text_of_element(*AlertsLocators.DANGER_ALERT)
        with allure.step(
                'Проверить, что текст ошибки при пустом имени - Warning: You must agree to the Privacy Policy!'):
            allure_helper.attach(self.browser)
            assert error_text == 'Warning: You must agree to the Privacy Policy!', \
                f'Текст ошибки {error_text}'

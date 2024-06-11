import allure

from utils.allure_helper import attach
from utils.locators import AlertsLocators
from base.base_page import BasePage


class Alert(BasePage):

    @allure.step('Проверить, что выведен алерт с ошибкой')
    def check_danger_alert(self):
        """Проверка видимости алерта."""
        self.is_element_visible(*AlertsLocators.DANGER_ALERT)

    @allure.step('Кликнуть на кнопку Логина в алерте')
    def click_login_from_alert(self):
        """Клик по кнопке Логина в алерте."""
        self.click_on_element(*AlertsLocators.LINK_LOGIN_ALERT)

    @allure.step('Кликнуть на кнопку в алерте')
    def click_link_from_alert(self):
        """Клик по кнопке Сравнения в алерте."""
        el = self._element(*AlertsLocators.SUCCESS_ALERT)
        el.find_element(*AlertsLocators.LINK_ALERT).click()
        # self.click_on_element(*AlertsLocators.LINK_ALERT)
        self.browser.implicitly_wait(2)

    @allure.step('Проверить сообщение об ошибке')
    def check_error_text(self, txt):
        """Проверить сообщение об ошибке."""
        error_text = self.get_text_of_element(*AlertsLocators.DANGER_ALERT)
        with allure.step(f'Проверить, что текст ошибки - {txt}'):
            attach(self.browser)
            assert error_text == txt, \
                f'Текст ошибки {error_text}'

    @allure.step('Проверить видимость успешного алерта')
    def check_success_alert(self, txt=None):
        """Вывод успешного алерта."""
        self.is_element_visible(*AlertsLocators.SUCCESS_ALERT)
        if txt:
            success_text = self.get_text_of_element(*AlertsLocators.SUCCESS_ALERT)
            res = success_text.replace('×', '').strip()
            with allure.step(f'Проверить, что текст - {txt}'):
                attach(self.browser)
                assert res == txt, f'Текст - {res}'

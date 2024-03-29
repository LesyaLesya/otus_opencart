import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.allure_helper import attach
from helpers.locators import AlertsLocators


class Alert:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 5)
        self.element = EC.visibility_of_element_located

    @property
    def success_alert(self):
        return self.wait.until(self.element(AlertsLocators.SUCCESS_ALERT))

    @property
    def danger_alert(self):
        return self.wait.until(self.element(AlertsLocators.DANGER_ALERT))

    @allure.step('Проверить, что выведен алерт с ошибкой')
    def check_danger_alert(self):
        """Проверка видимости алерта."""
        assert self.danger_alert.is_displayed()

    @allure.step('Кликнуть на кнопку Логина в алерте')
    def click_login_from_alert(self):
        """Клик по кнопке Логина в алерте."""
        self.success_alert.find_element(*AlertsLocators.LINK_LOGIN_ALERT).click()

    @allure.step('Кликнуть на кнопку в алерте')
    def click_link_from_alert(self):
        """Клик по кнопке Сравнения в алерте."""
        self.success_alert.find_element(*AlertsLocators.LINK_ALERT).click()
        self.browser.implicitly_wait(2)

    @allure.step('Проверить сообщение об ошибке')
    def check_error_text(self, txt):
        """Проверить сообщение об ошибке."""
        error_text = self.danger_alert.text
        with allure.step(f'Проверить, что текст ошибки - {txt}'):
            attach(self.browser)
            assert error_text == txt, \
                f'Текст ошибки {error_text}'

    @allure.step('Проверить видимость успешного алерта')
    def check_success_alert(self, txt=None):
        """Вывод успешного алерта."""
        assert self.success_alert.is_displayed()
        if txt:
            success_text = self.success_alert.text
            res = success_text.replace('×', '').strip()
            with allure.step(f'Проверить, что текст - {txt}'):
                attach(self.browser)
                assert res == txt, f'Текст - {res}'

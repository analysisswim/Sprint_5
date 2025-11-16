from utils.urls import BASE_URL
from utils.data import EMAIL, PASSWORD
from utils.locators import (
    MAIN_LOGIN_BTN, LK_LINK, LOGIN_EMAIL, LOGIN_PASSWORD, LOGIN_SUBMIT, FORGOT_LINK,
    REG_LOGIN_LINK, ORDER_BTN
)
from helpers.overlays import kill_overlays
from helpers.clicks import safe_click
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TestLogin:

    def _fill_and_submit_login(self, driver, wait):
        wait.until(EC.visibility_of_element_located(LOGIN_EMAIL)).send_keys(EMAIL)
        driver.find_element(*LOGIN_PASSWORD).send_keys(PASSWORD)
        safe_click(driver, wait, LOGIN_SUBMIT)

    def test_login_via_main_button(self, driver):
        driver.get(BASE_URL); kill_overlays(driver)
        wait = WebDriverWait(driver, 15)

        safe_click(driver, wait, MAIN_LOGIN_BTN)
        self._fill_and_submit_login(driver, wait)

        # проверка
        wait.until(EC.visibility_of_element_located(ORDER_BTN))
        assert driver.find_elements(*ORDER_BTN), "Кнопка 'Оформить заказ' не найдена после логина"

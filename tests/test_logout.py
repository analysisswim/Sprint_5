from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.urls import BASE_URL
from utils.data import EMAIL, PASSWORD
from utils.locators import (
    LK_LINK, LOGIN_EMAIL, LOGIN_PASSWORD, LOGIN_SUBMIT,
    ACCOUNT_LOGOUT_BTN, ORDER_BTN
)
from helpers.overlays import kill_overlays
from helpers.clicks import safe_click


class TestLogout:
    def _login(self, driver, wait):
        safe_click(driver, wait, LK_LINK)
        wait.until(EC.url_contains("/login"))

        wait.until(EC.visibility_of_element_located(LOGIN_EMAIL)).send_keys(EMAIL)
        driver.find_element(*LOGIN_PASSWORD).send_keys(PASSWORD)
        safe_click(driver, wait, LOGIN_SUBMIT)

        wait.until(EC.visibility_of_element_located(ORDER_BTN))
        assert driver.find_elements(*ORDER_BTN)

    def test_logout(self, driver):
        driver.get(BASE_URL); kill_overlays(driver)
        wait = WebDriverWait(driver, 15)

        self._login(driver, wait)

        safe_click(driver, wait, LK_LINK)
        wait.until(EC.any_of(
            EC.url_contains("/account"),
            EC.visibility_of_element_located(ACCOUNT_LOGOUT_BTN)
        ))

        safe_click(driver, wait, ACCOUNT_LOGOUT_BTN)

        assert wait.until(EC.any_of(
            EC.url_contains("/login"),
            EC.visibility_of_element_located(MAIN_LOGIN_BTN:=('xpath',"//button[normalize-space()='Войти в аккаунт']"))
        )) is not None

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.urls import BASE_URL
from utils.locators import (
    MAIN_LOGIN_BTN, LOGIN_REGISTER_LINK,
    REG_NAME, REG_EMAIL, REG_PASSWORD, REG_SUBMIT, REG_LOGIN_LINK,
    ORDER_BTN, ERROR_HINT,
    LOGIN_EMAIL, LOGIN_PASSWORD, LOGIN_SUBMIT
)
from helpers.overlays import kill_overlays
from helpers.clicks import safe_click


class TestRegistration:
    def _unique_email(self):
        return f"auto_{int(time.time())}@ya.ru"

    def test_success_registration(self, driver):
        driver.get(BASE_URL); kill_overlays(driver)
        wait = WebDriverWait(driver, 15)

        safe_click(driver, wait, MAIN_LOGIN_BTN)
        wait.until(EC.url_contains("/login"))

        safe_click(driver, wait, LOGIN_REGISTER_LINK)
        wait.until(EC.url_contains("/register"))

        email = self._unique_email()

        wait.until(EC.visibility_of_element_located(REG_NAME)).send_keys("Auto User")
        driver.find_element(*REG_EMAIL).send_keys(email)
        driver.find_element(*REG_PASSWORD).send_keys("12345Zz")
        safe_click(driver, wait, REG_SUBMIT)

        wait.until(EC.any_of(
            EC.url_contains("/login"),
            EC.visibility_of_element_located(ORDER_BTN),
        ))

        if "/login" in driver.current_url:
            wait.until(EC.visibility_of_element_located(LOGIN_EMAIL)).send_keys(email)
            driver.find_element(*LOGIN_PASSWORD).send_keys("12345Zz")
            safe_click(driver, wait, LOGIN_SUBMIT)

        wait.until(EC.visibility_of_element_located(ORDER_BTN))
        assert driver.find_elements(*ORDER_BTN), "После регистрации/логина нет кнопки 'Оформить заказ'"

    def test_invalid_password_shows_error(self, driver):
        driver.get(BASE_URL); kill_overlays(driver)
        wait = WebDriverWait(driver, 15)

        safe_click(driver, wait, MAIN_LOGIN_BTN)
        wait.until(EC.url_contains("/login"))

        safe_click(driver, wait, LOGIN_REGISTER_LINK)
        wait.until(EC.url_contains("/register"))

        wait.until(EC.visibility_of_element_located(REG_NAME)).send_keys("Auto User")
        driver.find_element(*REG_EMAIL).send_keys(self._unique_email())
        driver.find_element(*REG_PASSWORD).send_keys("123")   # меньше 6
        safe_click(driver, wait, REG_SUBMIT)

        wait.until(EC.visibility_of_element_located(ERROR_HINT))
        assert driver.find_elements(*ERROR_HINT), "Не появилась ошибка о некорректном пароле"

        safe_click(driver, wait, REG_LOGIN_LINK)
        wait.until(EC.url_contains("/login"))

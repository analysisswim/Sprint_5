from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.urls import BASE_URL
from utils.locators import (
    MAIN_LOGIN_BTN, LOGIN_REGISTER_LINK,
    REG_NAME, REG_EMAIL, REG_PASSWORD, REG_SUBMIT, REG_LOGIN_LINK,
    ERROR_HINT
)
from helpers.overlays import kill_overlays
from helpers.clicks import safe_click
from helpers.generators import uniq_email


class TestRegistration:

    def test_success_registration(self, driver):
        driver.get(BASE_URL); kill_overlays(driver)
        wait = WebDriverWait(driver, 15)

        safe_click(driver, wait, MAIN_LOGIN_BTN)
        assert wait.until(EC.url_contains("/login")), "Ожидали /login"

        safe_click(driver, wait, LOGIN_REGISTER_LINK)
        assert wait.until(EC.url_contains("/register")), "Ожидали /register"

        wait.until(EC.visibility_of_element_located(REG_NAME)).send_keys("Auto User")
        driver.find_element(*REG_EMAIL).send_keys(uniq_email())
        driver.find_element(*REG_PASSWORD).send_keys("12345Zz")
        safe_click(driver, wait, REG_SUBMIT)

        # Делаем тест атомарным: проверяем именно редирект на /login после регистрации
        assert wait.until(EC.url_contains("/login")), "После регистрации ожидали переход на /login"

    def test_invalid_password_shows_error(self, driver):
        driver.get(BASE_URL); kill_overlays(driver)
        wait = WebDriverWait(driver, 15)

        safe_click(driver, wait, MAIN_LOGIN_BTN)
        assert wait.until(EC.url_contains("/login"))

        safe_click(driver, wait, LOGIN_REGISTER_LINK)
        assert wait.until(EC.url_contains("/register"))

        wait.until(EC.visibility_of_element_located(REG_NAME)).send_keys("Auto User")
        driver.find_element(*REG_EMAIL).send_keys(uniq_email())
        driver.find_element(*REG_PASSWORD).send_keys("123")   # < 6 символов
        safe_click(driver, wait, REG_SUBMIT)

        assert wait.until(EC.visibility_of_element_located(ERROR_HINT)), "Ожидали подсказку об ошибке"

        safe_click(driver, wait, REG_LOGIN_LINK)
        assert wait.until(EC.url_contains("/login")), "Ожидали возврат на /login"

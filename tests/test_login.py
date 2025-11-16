from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.urls import BASE_URL
from utils.data import EMAIL, PASSWORD
from utils.locators import (
    MAIN_LOGIN_BTN, LK_LINK, FORGOT_LINK, LOGIN_REGISTER_LINK, REG_LOGIN_LINK, ORDER_BTN
)
from helpers.overlays import kill_overlays
from helpers.clicks import safe_click
from helpers.auth import submit_login


class TestLogin:

    def test_login_via_main_button(self, driver):
        driver.get(BASE_URL); kill_overlays(driver)
        wait = WebDriverWait(driver, 15)

        safe_click(driver, wait, MAIN_LOGIN_BTN)
        assert wait.until(EC.url_contains("/login")), "Ожидали переход на /login"

        submit_login(driver, wait, EMAIL, PASSWORD)

        el = wait.until(EC.visibility_of_element_located(ORDER_BTN))
        assert el, "Кнопка 'Оформить заказ' не найдена после логина"

    def test_login_via_header_lk(self, driver):
        driver.get(BASE_URL); kill_overlays(driver)
        wait = WebDriverWait(driver, 15)

        safe_click(driver, wait, LK_LINK)
        assert wait.until(EC.url_contains("/login")), "Ожидали переход на /login"

        submit_login(driver, wait, EMAIL, PASSWORD)

        el = wait.until(EC.visibility_of_element_located(ORDER_BTN))
        assert el, "Нет кнопки 'Оформить заказ' после логина через ЛК"

    def test_login_from_register_form(self, driver):
        driver.get(BASE_URL); kill_overlays(driver)
        wait = WebDriverWait(driver, 15)

        safe_click(driver, wait, LK_LINK)
        assert wait.until(EC.url_contains("/login")), "Ожидали /login"

        safe_click(driver, wait, LOGIN_REGISTER_LINK)
        assert wait.until(EC.url_contains("/register")), "Ожидали /register"

        safe_click(driver, wait, REG_LOGIN_LINK)
        assert wait.until(EC.url_contains("/login")), "Ожидали возврат на /login"

        submit_login(driver, wait, EMAIL, PASSWORD)

        el = wait.until(EC.visibility_of_element_located(ORDER_BTN))
        assert el, "Нет кнопки 'Оформить заказ' после логина из формы регистрации"

    def test_login_from_recovery_form(self, driver):
        driver.get(BASE_URL); kill_overlays(driver)
        wait = WebDriverWait(driver, 15)

        safe_click(driver, wait, LK_LINK)
        assert wait.until(EC.url_contains("/login")), "Ожидали /login"

        safe_click(driver, wait, FORGOT_LINK)
        assert wait.until(EC.url_contains("/forgot-password")), "Ожидали /forgot-password"

        safe_click(driver, wait, REG_LOGIN_LINK)
        assert wait.until(EC.url_contains("/login")), "Ожидали возврат на /login"

        submit_login(driver, wait, EMAIL, PASSWORD)

        el = wait.until(EC.visibility_of_element_located(ORDER_BTN))
        assert el, "Нет кнопки 'Оформить заказ' после логина"

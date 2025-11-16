from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.urls import BASE_URL
from utils.data import EMAIL, PASSWORD
from utils.locators import (
    LK_LINK, ACCOUNT_LOGOUT_BTN, ORDER_BTN, MAIN_LOGIN_BTN
)
from helpers.overlays import kill_overlays
from helpers.clicks import safe_click
from helpers.auth import submit_login


class TestLogout:

    def test_logout(self, driver):
        driver.get(BASE_URL); kill_overlays(driver)
        wait = WebDriverWait(driver, 15)

        # Перейти на /login и залогиниться
        safe_click(driver, wait, LK_LINK)
        assert wait.until(EC.url_contains("/login")), "Ожидали /login"
        submit_login(driver, wait, EMAIL, PASSWORD)

        el = wait.until(EC.visibility_of_element_located(ORDER_BTN))
        assert el, "После логина нет кнопки 'Оформить заказ'"

        # Открыть ЛК и дождаться 'Выход'
        safe_click(driver, wait, LK_LINK)
        assert wait.until(EC.any_of(
            EC.url_contains("/account"),
            EC.visibility_of_element_located(ACCOUNT_LOGOUT_BTN)
        )), "Ожидали переход в ЛК или появление кнопки 'Выход'"

        # Разлогин
        safe_click(driver, wait, ACCOUNT_LOGOUT_BTN)

        # Проверяем, что разлогинились
        assert wait.until(EC.any_of(
            EC.url_contains("/login"),
            EC.visibility_of_element_located(MAIN_LOGIN_BTN)
        )), "Ожидали /login или кнопку 'Войти в аккаунт'"

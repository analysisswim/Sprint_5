from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.urls import BASE_URL
from utils.data import EMAIL, PASSWORD
from utils.locators import (
    LK_LINK, BTN_CONSTRUCTOR, ORDER_BTN, LOGO_LINK,
    LOGIN_EMAIL, LOGIN_PASSWORD, LOGIN_SUBMIT
)
from helpers.overlays import kill_overlays
from helpers.clicks import safe_click


class TestNavigation:

    def _login(self, driver, wait):
        safe_click(driver, wait, LK_LINK)  # перейти на /login
        email = wait.until(EC.visibility_of_element_located(LOGIN_EMAIL))
        pwd   = driver.find_element(*LOGIN_PASSWORD)
        email.clear(); email.send_keys(EMAIL)
        pwd.clear();   pwd.send_keys(PASSWORD)
        safe_click(driver, wait, LOGIN_SUBMIT)
        wait.until(EC.visibility_of_element_located(ORDER_BTN))

    def test_back_to_constructor_by_button_and_logo(self, driver):
        driver.get(BASE_URL); kill_overlays(driver)
        wait = WebDriverWait(driver, 10)

        self._login(driver, wait)

        # В аккаунт
        safe_click(driver, wait, LK_LINK)
        wait.until(EC.url_contains("/account"))

        # Назад по кнопке «Конструктор»
        kill_overlays(driver)
        safe_click(driver, wait, BTN_CONSTRUCTOR)
        wait.until(EC.visibility_of_element_located(ORDER_BTN))
        assert driver.find_elements(*ORDER_BTN), "После клика по «Конструктор» нет кнопки «Оформить заказ»"

        # Снова в аккаунт
        safe_click(driver, wait, LK_LINK)
        wait.until(EC.url_contains("/account"))

        # Назад по логотипу
        kill_overlays(driver)
        safe_click(driver, wait, LOGO_LINK)
        wait.until(EC.visibility_of_element_located(ORDER_BTN))
        assert driver.find_elements(*ORDER_BTN), "После клика по логотипу нет кнопки «Оформить заказ»"

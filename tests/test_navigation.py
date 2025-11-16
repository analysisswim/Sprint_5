from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.urls import BASE_URL
from utils.data import EMAIL, PASSWORD
from utils.locators import (
    LK_LINK, BTN_CONSTRUCTOR, ORDER_BTN, LOGO_LINK
)
from helpers.overlays import kill_overlays
from helpers.clicks import safe_click
from helpers.auth import submit_login


class TestNavigation:

    def test_back_to_constructor_by_button_and_logo(self, driver):
        driver.get(BASE_URL); kill_overlays(driver)
        wait = WebDriverWait(driver, 10)

        # Логин
        safe_click(driver, wait, LK_LINK)
        assert wait.until(EC.url_contains("/login")), "Ожидали /login"
        submit_login(driver, wait, EMAIL, PASSWORD)
        assert wait.until(EC.visibility_of_element_located(ORDER_BTN))

        # В аккаунт → обратно по кнопке «Конструктор»
        safe_click(driver, wait, LK_LINK)
        assert wait.until(EC.url_contains("/account")), "Ожидали /account"

        kill_overlays(driver)
        safe_click(driver, wait, BTN_CONSTRUCTOR)
        assert wait.until(EC.visibility_of_element_located(ORDER_BTN)), "Нет кнопки 'Оформить заказ' после «Конструктор»"

        # Снова в аккаунт → обратно по логотипу
        safe_click(driver, wait, LK_LINK)
        assert wait.until(EC.url_contains("/account"))

        kill_overlays(driver)
        safe_click(driver, wait, LOGO_LINK)
        assert wait.until(EC.visibility_of_element_located(ORDER_BTN)), "Нет кнопки 'Оформить заказ' после клика по логотипу"

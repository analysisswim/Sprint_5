from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.overlays import kill_overlays
from helpers.clicks import safe_click
from utils.data import (
    BASE_URL, EMAIL, PASSWORD,
    LK_LINK, EMAIL_LABEL, PASS_LABEL, EMAIL_FALL, PASS_FALL,
    LOGIN_BTN, BTN_CONSTRUCTOR, ORDER_BTN, LOGO_LINK
)

def _login(driver, wait):
    safe_click(driver, wait, LK_LINK)
    try:
        email = wait.until(EC.visibility_of_element_located(EMAIL_LABEL))
        pwd   = driver.find_element(*PASS_LABEL)
    except Exception:
        email = wait.until(EC.visibility_of_element_located(EMAIL_FALL))
        pwd   = driver.find_element(*PASS_FALL)
    email.send_keys(EMAIL); pwd.send_keys(PASSWORD)
    safe_click(driver, wait, LOGIN_BTN)
    wait.until(EC.visibility_of_element_located(ORDER_BTN))

def test_back_to_constructor_by_button_and_logo(driver):
    driver.get(BASE_URL)
    kill_overlays(driver)
    wait = WebDriverWait(driver, 10)

    _login(driver, wait)

    # В аккаунт
    safe_click(driver, wait, LK_LINK)
    wait.until(EC.url_contains("/account"))

    # Назад по кнопке «Конструктор»
    kill_overlays(driver)
    safe_click(driver, wait, BTN_CONSTRUCTOR)
    wait.until(EC.visibility_of_element_located(ORDER_BTN))

    # Снова в аккаунт
    safe_click(driver, wait, LK_LINK)
    wait.until(EC.url_contains("/account"))

    # Назад по ЛОГОТИПУ
    kill_overlays(driver)
    safe_click(driver, wait, LOGO_LINK)
    wait.until(EC.visibility_of_element_located(ORDER_BTN))

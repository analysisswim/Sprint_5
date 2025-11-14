from os import getenv
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.overlays import kill_overlays
from helpers.clicks import safe_click
from utils.data import (
    LK_LINK,
    ACCOUNT_LOGOUT_BTN,
    MAIN_LOGIN_BTN,   # добавим, чтобы не дублировать XPath
    ORDER_BTN,        # якорь успешного логина
    BASE_URL,
)

EMAIL = getenv("STELLAR_EMAIL", "siarhei_ivashyn_34_999@yandex.ru")
PASSWORD = getenv("STELLAR_PASSWORD", "12345Zz")

# Логин-форма (лейблы + fallback по name)
EMAIL_LABEL = (By.XPATH, "//label[normalize-space()='Email']/ancestor::div[contains(@class,'input')]//input")
PASS_LABEL  = (By.XPATH, "//label[normalize-space()='Пароль']/ancestor::div[contains(@class,'input')]//input")
EMAIL_FALL  = (By.NAME, "email")
PASS_FALL   = (By.NAME, "password")
LOGIN_BTN   = (By.XPATH, "//button[normalize-space(.)='Войти']")

def _ensure_logged_in(driver, wait):
    safe_click(driver, wait, LK_LINK)  # перейти в /login
    try:
        email = wait.until(EC.visibility_of_element_located(EMAIL_LABEL))
        pwd   = driver.find_element(*PASS_LABEL)
    except Exception:
        email = wait.until(EC.visibility_of_element_located(EMAIL_FALL))
        pwd   = driver.find_element(*PASS_FALL)
    email.clear(); email.send_keys(EMAIL)
    pwd.clear();   pwd.send_keys(PASSWORD)
    safe_click(driver, wait, LOGIN_BTN)
    wait.until(EC.visibility_of_element_located(ORDER_BTN))  # успешный вход

def _go_account(driver, wait):
    kill_overlays(driver)
    safe_click(driver, wait, LK_LINK)
    try:
        wait.until(EC.any_of(
            EC.url_contains("/account"),
            EC.visibility_of_element_located(ACCOUNT_LOGOUT_BTN)
        ))
    except TimeoutException:
        # жёсткий фоллбэк — прямой переход
        driver.get(BASE_URL + "account/profile")
        sleep(0.3)
        wait.until(EC.any_of(
            EC.url_contains("/account"),
            EC.visibility_of_element_located(ACCOUNT_LOGOUT_BTN)
        ))

def test_logout(driver):
    driver.get(BASE_URL)
    kill_overlays(driver)
    wait = WebDriverWait(driver, 20)

    _ensure_logged_in(driver, wait)
    _go_account(driver, wait)

    # Нажать «Выход»
    kill_overlays(driver)
    safe_click(driver, wait, ACCOUNT_LOGOUT_BTN)

    # Проверка разлогина: либо /login, либо видна кнопка «Войти в аккаунт» на главной
    wait.until(EC.any_of(
        EC.url_contains("/login"),
        EC.visibility_of_element_located(MAIN_LOGIN_BTN)
    ))

from os import getenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.overlays import kill_overlays
from helpers.clicks import safe_click

BASE_URL = "https://stellarburgers.education-services.ru/"
EMAIL = getenv("STELLAR_EMAIL", "siarhei_ivashyn_34_999@yandex.ru")
PASSWORD = getenv("STELLAR_PASSWORD", "12345Zz")


def _fill_and_submit_login(d, wait):
    # Поля Email/Пароль: сначала по лейблам, иначе fallback по name
    try:
        email_el = wait.until(EC.visibility_of_element_located((
            By.XPATH, "//label[normalize-space()='Email']/ancestor::div[contains(@class,'input')]//input"
        )))
        pass_el = d.find_element(
            By.XPATH, "//label[normalize-space()='Пароль']/ancestor::div[contains(@class,'input')]//input"
        )
    except Exception:
        email_el = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        pass_el = d.find_element(By.NAME, "password")

    email_el.clear(); email_el.send_keys(EMAIL)
    pass_el.clear();  pass_el.send_keys(PASSWORD)

    # Жмём кнопку «Войти» (именно на странице логина)
    safe_click(d, wait, (By.XPATH, "//button[normalize-space(.)='Войти']"))

    # Признак успешного входа
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//button[normalize-space(.)='Оформить заказ']"))
    )


def test_login_via_main_button(driver):
    driver.get(BASE_URL)
    kill_overlays(driver)
    wait = WebDriverWait(driver, 15)

    # На главной — «Войти в аккаунт»
    safe_click(driver, wait, (By.XPATH, "//button[normalize-space(.)='Войти в аккаунт']"))
    wait.until(EC.url_contains("/login"))

    _fill_and_submit_login(driver, wait)


def test_login_via_header_lk(driver):
    driver.get(BASE_URL)
    kill_overlays(driver)
    wait = WebDriverWait(driver, 15)

    # «Личный кабинет» → /login
    safe_click(driver, wait, (By.XPATH, "//a[contains(@href,'/account')]"))
    wait.until(EC.url_contains("/login"))

    _fill_and_submit_login(driver, wait)


def test_login_from_register_form(driver):
    driver.get(BASE_URL)
    kill_overlays(driver)
    wait = WebDriverWait(driver, 15)

    safe_click(driver, wait, (By.XPATH, "//a[contains(@href,'/account')]"))
    wait.until(EC.url_contains("/login"))

    safe_click(driver, wait, (By.XPATH, "//a[contains(@href,'/register')]"))
    wait.until(EC.url_contains("/register"))

    safe_click(driver, wait, (By.XPATH, "//a[contains(@href,'/login') and normalize-space()='Войти']"))
    wait.until(EC.url_contains("/login"))

    _fill_and_submit_login(driver, wait)


def test_login_from_recovery_form(driver):
    driver.get(BASE_URL)
    kill_overlays(driver)
    wait = WebDriverWait(driver, 15)

    safe_click(driver, wait, (By.XPATH, "//a[contains(@href,'/account')]"))
    wait.until(EC.url_contains("/login"))

    safe_click(driver, wait, (By.XPATH, "//a[contains(@href,'/forgot-password')]"))
    wait.until(EC.url_contains("/forgot-password"))

    safe_click(driver, wait, (By.XPATH, "//a[contains(@href,'/login') and normalize-space()='Войти']"))
    wait.until(EC.url_contains("/login"))

    _fill_and_submit_login(driver, wait)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.overlays import kill_overlays
from utils.generators import uniq_email

BASE_URL = "https://stellarburgers.education-services.ru/"

LK_LINK       = (By.XPATH, "//a[contains(@href,'/account')]")
REG_LINK      = (By.XPATH, "//a[contains(@href,'/register')]")
BTN_REGISTER  = (By.XPATH, "//button[normalize-space()='Зарегистрироваться']")
TO_LOGIN_LINK = (By.XPATH, "//a[contains(@href,'/login') and normalize-space()='Войти']")
NAME_INPUT_L  = (By.XPATH, "//label[normalize-space()='Имя']/ancestor::div[contains(@class,'input')]//input")
EMAIL_INPUT_L = (By.XPATH, "//label[normalize-space()='Email']/ancestor::div[contains(@class,'input')]//input")
PASS_INPUT_L  = (By.XPATH, "//label[normalize-space()='Пароль']/ancestor::div[contains(@class,'input')]//input")
EMAIL_FALL    = (By.NAME, "email")
NAME_FALL     = (By.NAME, "name")
PASS_FALL     = (By.NAME, "password")

def _open_register(driver, wait):
    driver.get(BASE_URL)
    kill_overlays(driver)
    driver.find_element(*LK_LINK).click()
    wait.until(EC.url_contains("/login"))
    driver.find_element(*REG_LINK).click()
    wait.until(EC.url_contains("/register"))

def test_registration_success(driver):
    wait = WebDriverWait(driver, 15)
    _open_register(driver, wait)

    # поля
    try:
        name  = wait.until(EC.visibility_of_element_located(NAME_INPUT_L))
        email = driver.find_element(*EMAIL_INPUT_L)
        pwd   = driver.find_element(*PASS_INPUT_L)
    except Exception:
        name  = wait.until(EC.visibility_of_element_located(NAME_FALL))
        email = driver.find_element(*EMAIL_FALL)
        pwd   = driver.find_element(*PASS_FALL)

    email_val = uniq_email()
    name.send_keys("Siarhei")
    email.send_keys(email_val)
    pwd.send_keys("12345Zz")            # 6+ символов, буквы разного регистра + цифры — ок
    driver.find_element(*BTN_REGISTER).click()

    # после успешной регистрации должна открыться страница логина
    wait.until(EC.url_contains("/login"))

def test_registration_error_short_password(driver):
    wait = WebDriverWait(driver, 15)
    _open_register(driver, wait)

    try:
        name  = wait.until(EC.visibility_of_element_located(NAME_INPUT_L))
        email = driver.find_element(*EMAIL_INPUT_L)
        pwd   = driver.find_element(*PASS_INPUT_L)
    except Exception:
        name  = wait.until(EC.visibility_of_element_located(NAME_FALL))
        email = driver.find_element(*EMAIL_FALL)
        pwd   = driver.find_element(*PASS_FALL)

    name.send_keys("Siarhei")
    email.send_keys(uniq_email())
    pwd.send_keys("12345")  # короче 6

    driver.find_element(*BTN_REGISTER).click()

    # ожидаем сообщение об ошибке под полем пароля
    err = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[contains(text(),'Некорректный') or contains(text(),'парол')]")
    ))
    assert err.is_displayed()

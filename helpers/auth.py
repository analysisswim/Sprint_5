# helpers/auth.py
from selenium.webdriver.support import expected_conditions as EC
from utils.locators import LOGIN_EMAIL, LOGIN_PASSWORD, LOGIN_SUBMIT
from helpers.clicks import safe_click

def submit_login(driver, wait, email, password):
    """Заполняет форму логина и жмёт «Войти»."""
    email_el = wait.until(EC.visibility_of_element_located(LOGIN_EMAIL))
    email_el.clear(); email_el.send_keys(email)

    pwd_el = driver.find_element(*LOGIN_PASSWORD)
    pwd_el.clear(); pwd_el.send_keys(password)

    safe_click(driver, wait, LOGIN_SUBMIT)

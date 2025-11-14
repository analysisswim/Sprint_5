from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.overlays import kill_overlays

BASE_URL = "https://stellarburgers.education-services.ru/"

# Кликаем по контейнеру вкладки с текстом внутри
TAB_BUNS    = (By.XPATH, "//div[contains(@class,'tab')][.//span[normalize-space()='Булки']]")
TAB_SAUCES  = (By.XPATH, "//div[contains(@class,'tab')][.//span[normalize-space()='Соусы']]")
TAB_FILLING = (By.XPATH, "//div[contains(@class,'tab')][.//span[normalize-space()='Начинки']]")

def safe_click(driver, wait, locator):
    el = wait.until(EC.element_to_be_clickable(locator))
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
    try:
        el.click()
    except Exception:
        driver.execute_script("arguments[0].click();", el)

def _is_active_text(driver, text):
    # 1) активный класс на контейнере вкладки
    xp1 = f"//div[contains(@class,'tab') and (contains(@class,'current') or contains(@class,'tab_type_current'))]" \
          f"//span[normalize-space()='{text}']"
    # 2) aria-selected=true на span
    xp2 = f"//span[normalize-space()='{text}'][@aria-selected='true']"
    return bool(driver.find_elements(By.XPATH, xp1)) or bool(driver.find_elements(By.XPATH, xp2))

def _wait_active_text(driver, wait, text):
    wait.until(lambda d: _is_active_text(d, text))

def test_tabs_switch(driver):
    driver.get(BASE_URL)
    kill_overlays(driver)
    wait = WebDriverWait(driver, 10)

    safe_click(driver, wait, TAB_SAUCES)
    _wait_active_text(driver, wait, "Соусы")

    safe_click(driver, wait, TAB_FILLING)
    _wait_active_text(driver, wait, "Начинки")

    safe_click(driver, wait, TAB_BUNS)
    _wait_active_text(driver, wait, "Булки")

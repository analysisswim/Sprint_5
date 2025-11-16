# helpers/tabs.py
from selenium.webdriver.common.by import By

def is_tab_active(driver, text: str) -> bool:
    # активная вкладка: либо контейнер с классом current, либо span с aria-selected="true"
    xp1 = (
        "//div[contains(@class,'tab') and "
        "(contains(@class,'current') or contains(@class,'tab_type_current'))]"
        f"//span[normalize-space()='{text}']"
    )
    xp2 = f"//span[normalize-space()='{text}'][@aria-selected='true']"
    return bool(driver.find_elements(By.XPATH, xp1)) or bool(driver.find_elements(By.XPATH, xp2))

def wait_tab_active(driver, wait, text: str):
    wait.until(lambda d: is_tab_active(d, text))

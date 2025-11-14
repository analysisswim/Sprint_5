# helpers/clicks.py
from selenium.webdriver.support import expected_conditions as EC

def safe_click(driver, wait, locator):
    from helpers.overlays import kill_overlays, wait_no_overlay
    kill_overlays(driver)
    try:
        el = wait.until(EC.element_to_be_clickable(locator))
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
        el.click()
    except Exception:
        # если перехвачено — ещё раз сносим всё и жмём JS-ом
        kill_overlays(driver)
        try:
            wait_no_overlay(driver, 3)
        except Exception:
            pass
        el = driver.find_element(*locator)
        driver.execute_script("arguments[0].click();", el)

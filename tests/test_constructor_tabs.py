import pytest
from selenium.webdriver.support.ui import WebDriverWait

from utils.urls import BASE_URL
from utils.locators import TAB_BUNS, TAB_SAUCES, TAB_FILLING
from helpers.overlays import kill_overlays
from helpers.clicks import safe_click
from helpers.tabs import wait_tab_active, is_tab_active

class TestConstructorTabs:

    @pytest.mark.parametrize(
        "locator,label",
        [
            (TAB_SAUCES, "Соусы"),
            (TAB_FILLING, "Начинки"),
            (TAB_BUNS, "Булки"),
        ],
    )
    def test_tab_switch(self, driver, locator, label):
        driver.get(BASE_URL)
        kill_overlays(driver)
        wait = WebDriverWait(driver, 10)

        safe_click(driver, wait, locator)
        wait_tab_active(driver, wait, label)

        assert is_tab_active(driver, label), f"Ожидали активную вкладку: {label}"

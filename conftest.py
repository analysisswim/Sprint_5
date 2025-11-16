import sys, os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox"],
        help="Browser to run tests: chrome or firefox",
    )

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        opts = ChromeOptions()
        opts.add_argument("--window-size=1280,1000")
        opts.add_argument("--disable-extensions")
        opts.add_argument("--disable-infobars")
        opts.add_argument("--disable-dev-shm-usage")
        opts.add_argument("--no-sandbox")
        drv = webdriver.Chrome(options=opts)
    else:
        fopts = FirefoxOptions()
        fopts.set_preference("dom.webnotifications.enabled", False)
        drv = webdriver.Firefox(options=fopts)

    yield drv
    try:
        drv.delete_all_cookies()
    finally:
        drv.quit()

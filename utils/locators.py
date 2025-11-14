from selenium.webdriver.common.by import By

# Header / nav
LK_LINK         = (By.XPATH, "//a[contains(@href,'/account')]")
BTN_CONSTRUCTOR = (By.XPATH, "//p[normalize-space()='Конструктор']/ancestor::a")
LOGO_LINK       = (By.CSS_SELECTOR, "header a[class*='AppHeader_header__logo']")

# Main
ORDER_BTN       = (By.XPATH, "//button[normalize-space()='Оформить заказ']")
MAIN_LOGIN_BTN  = (By.XPATH, "//button[normalize-space()='Войти в аккаунт']")

# Constructor tabs
TAB_BUNS        = (By.XPATH, "//span[normalize-space()='Булки']/..")
TAB_SAUCES      = (By.XPATH, "//span[normalize-space()='Соусы']/..")
TAB_FILLING     = (By.XPATH, "//span[normalize-space()='Начинки']/..")

# Auth (single stable set)
LOGIN_EMAIL     = (By.NAME, "email")
LOGIN_PASSWORD  = (By.NAME, "password")
LOGIN_SUBMIT    = (By.XPATH, "//button[normalize-space()='Войти']")

# Registration
REG_NAME        = (By.NAME, "name")
REG_EMAIL       = (By.NAME, "email")
REG_PASSWORD    = (By.NAME, "password")
REG_SUBMIT      = (By.XPATH, "//button[normalize-space()='Зарегистрироваться']")
REG_LOGIN_LINK  = (By.XPATH, "//a[contains(@href,'/login') and normalize-space()='Войти']")

# Recovery
FORGOT_LINK     = (By.XPATH, "//a[contains(@href,'/forgot-password')]")

# Account
ACCOUNT_LOGOUT_BTN = (By.XPATH, "//button[normalize-space()='Выход']")

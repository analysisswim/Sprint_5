from os import getenv
from selenium.webdriver.common.by import By

BASE_URL = "https://stellarburgers.education-services.ru/"
EMAIL = getenv("STELLAR_EMAIL", "siarhei_ivashyn_34_999@yandex.ru")
PASSWORD = getenv("STELLAR_PASSWORD", "12345Zz")

# Хедер / навигация
LK_LINK        = (By.XPATH, "//a[contains(@href,'/account')]")
BTN_CONSTRUCTOR= (By.XPATH, "//p[normalize-space()='Конструктор']/ancestor::a")
LOGO_LINK      = (By.XPATH, "(//header//a[@href='/' or contains(@class,'AppHeader_header__logo')])[1]")

# Главная
ORDER_BTN      = (By.XPATH, "//button[normalize-space()='Оформить заказ']")
MAIN_LOGIN_BTN = (By.XPATH, "//button[normalize-space()='Войти в аккаунт']")

# Вкладки конструктора
TAB_BUNS    = (By.XPATH, "//span[normalize-space()='Булки']/..")
TAB_SAUCES  = (By.XPATH, "//span[normalize-space()='Соусы']/..")
TAB_FILLING = (By.XPATH, "//span[normalize-space()='Начинки']/..")

# Логин-форма (лейблы + fallback по name)
EMAIL_LABEL = (By.XPATH, "//label[normalize-space()='Email']/ancestor::div[contains(@class,'input')]//input")
PASS_LABEL  = (By.XPATH, "//label[normalize-space()='Пароль']/ancestor::div[contains(@class,'input')]//input")
EMAIL_FALL  = (By.NAME, "email")
PASS_FALL   = (By.NAME, "password")
LOGIN_BTN   = (By.XPATH, "//button[normalize-space()='Войти']")

# Профиль
ACCOUNT_LOGOUT_BTN = (By.XPATH, "//button[contains(normalize-space(.),'Выход')]")


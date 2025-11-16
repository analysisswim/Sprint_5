from selenium.webdriver.common.by import By

# Хедер / навигация
LK_LINK         = (By.CSS_SELECTOR, "header a[href*='/account']")
BTN_CONSTRUCTOR = (By.XPATH, "//p[normalize-space()='Конструктор']/ancestor::a")
LOGO_LINK       = (By.CSS_SELECTOR, "header a[href='/']")
MAIN_LOGIN_BTN  = (By.XPATH, "//button[normalize-space()='Войти в аккаунт']")
ORDER_BTN       = (By.XPATH, "//button[normalize-space()='Оформить заказ']")

# Вкладки конструктора
TAB_BUNS    = (By.XPATH, "//span[normalize-space()='Булки']/..")
TAB_SAUCES  = (By.XPATH, "//span[normalize-space()='Соусы']/..")
TAB_FILLING = (By.XPATH, "//span[normalize-space()='Начинки']/..")

# Логин
LOGIN_EMAIL     = (By.XPATH, "//label[normalize-space()='Email']/ancestor::div[contains(@class,'input')]//input")
LOGIN_PASSWORD  = (By.XPATH, "//label[normalize-space()='Пароль']/ancestor::div[contains(@class,'input')]//input")
LOGIN_SUBMIT    = (By.XPATH, "//button[normalize-space()='Войти']")
FORGOT_LINK     = (By.XPATH, "//a[contains(@href,'/forgot-password')]")
LOGIN_REGISTER_LINK = (By.XPATH, "//a[contains(@href,'/register')]")

# Регистрация
REG_NAME        = (By.XPATH, "//label[normalize-space()='Имя']/ancestor::div[contains(@class,'input')]//input")
REG_EMAIL       = (By.XPATH, "//label[normalize-space()='Email']/ancestor::div[contains(@class,'input')]//input")
REG_PASSWORD    = (By.XPATH, "//label[normalize-space()='Пароль']/ancestor::div[contains(@class,'input')]//input")
REG_SUBMIT      = (By.XPATH, "//button[normalize-space()='Зарегистрироваться']")
REG_LOGIN_LINK  = (By.XPATH, "//a[contains(@href,'/login') and normalize-space()='Войти']")

# Аккаунт
ACCOUNT_LOGOUT_BTN = (By.XPATH, "//button[normalize-space()='Выход']")

# Подсказка об ошибке (для короткого пароля)
ERROR_HINT = (By.XPATH, "//*[contains(@class,'input__error') or contains(@class,'Input_error') or contains(@class,'error')][contains(.,'Некоррект')]")

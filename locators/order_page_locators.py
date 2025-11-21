# locators/order_page_locators.py
from selenium.webdriver.common.by import By


class OrderPageLocators:
    # ---------- Шаг 1. Для кого самокат ----------

    # поля ввода
    FIRST_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_FIRST_OPTION = (By.CLASS_NAME, "Order_SelectOption__82bhS")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    # кнопка «Далее»
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # ---------- Шаг 2. Про аренду ----------

    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    # срок аренды
    RENT_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder")
    RENT_OPTION_SUTKI = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")
    # цвет
    COLOR_BLACK_CHECKBOX = (By.ID, "black")
    # комментарий
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    # кнопки оформления заказа
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Buttons')]/button[text()='Заказать']")
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")

    # модалка об успешном заказе
    SUCCESS_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")

    # ---------- Логотипы в шапке ----------

    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3ST0t")

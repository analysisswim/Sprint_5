# locators/main_page_locators.py
from selenium.webdriver.common.by import By


class MainPageLocators:
    # кнопки «Заказать» (верх и низ страницы)
    ORDER_BUTTONS = (By.XPATH, "//button[text()='Заказать']")

    # вопросы и ответы в блоке «Вопросы о важном»
    FAQ_QUESTIONS = (By.CLASS_NAME, "accordion__button")
    FAQ_ANSWERS = (By.CLASS_NAME, "accordion__panel")

    # логотипы
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    # более стабильный вариант: ищем по ссылке на яндекс
    YANDEX_LOGO = (By.CSS_SELECTOR, "a[href*='yandex.ru']")

    # кнопка в баннере с куками (любой button внутри контейнера App_CookieConsent)
    COOKIE_BUTTON = (By.CSS_SELECTOR, "div[class^='App_CookieConsent'] button")

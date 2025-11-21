# pages/main_page.py
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators

    @allure.step("Закрыть баннер с куками, если он есть")
    def close_cookie_banner(self):
        """Пытается закрыть баннер с куками, если он есть."""
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.locators.COOKIE_BUTTON)
            ).click()
        except Exception:
            # баннера нет или уже закрыт — просто игнорируем
            pass

    @allure.step("Клик по кнопке «Заказать» с индексом {index}")
    def click_order_button(self, index):
        """Клик по кнопке «Заказать» (0 — верхняя, 1 — нижняя)."""
        self.close_cookie_banner()
        # ждём, пока хотя бы одна кнопка станет кликабельной
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.ORDER_BUTTONS)
        )
        self.driver.find_elements(*self.locators.ORDER_BUTTONS)[index].click()

    @allure.step("Прокрутка до блока FAQ")
    def scroll_to_faq(self):
        first_question = self.driver.find_elements(*self.locators.FAQ_QUESTIONS)[0]
        self.driver.execute_script("arguments[0].scrollIntoView();", first_question)

    @allure.step("Клик по вопросу FAQ с индексом {index}")
    def click_faq_question(self, index):
        element = self.driver.find_elements(*self.locators.FAQ_QUESTIONS)[index]
        # скроллим конкретный вопрос в видимую область
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        # кликаем по нему через JS, чтобы не мешала картинка
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получение текста ответа FAQ по индексу {index}")
    def get_faq_answer_text(self, index):
        return self.driver.find_elements(*self.locators.FAQ_ANSWERS)[index].text

    @allure.step("Клик по логотипу «Самоката» на главной")
    def click_scooter_logo(self):
        self.close_cookie_banner()
        self.driver.find_element(*self.locators.SCOOTER_LOGO).click()

    @allure.step("Клик по логотипу Яндекса на главной")
    def click_yandex_logo(self):
        self.close_cookie_banner()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.YANDEX_LOGO)
        ).click()

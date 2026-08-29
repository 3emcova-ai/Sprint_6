import time
import allure

from base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Закрываю всплывающее окно с куками')
    def close_cookies(self):
        self.scroll_to_element(MainPageLocators.COOKIE_BUTTON)
        self.click_element_with_wait(MainPageLocators.COOKIE_BUTTON)

    @allure.step('Скролл до раздела Вопросы о важном')
    def scroll_to_questions(self):
        self.scroll_to_element(MainPageLocators.QUESTIONS_SECTION)

    @allure.step('Клик по кнопке Заказать в хедере страницы')
    def click_order_button_header(self):
        self.click_element_with_wait(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step('Клик по логотипу Яндекс')
    def click_logo_yandex(self):
        self.click_element_with_wait(MainPageLocators.LOGO_YANDEX)
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Клик по логотипу Самокат')
    def click_logo_scooter(self):
        self.click_element_with_wait(MainPageLocators.LOGO_SCOOTER)
   
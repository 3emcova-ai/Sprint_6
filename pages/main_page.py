from .base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def scroll_to_questions(self):
        self.scroll_to_element(MainPageLocators.QUESTIONS_SECTION)

    def click_to_question(self, locator):
        self.click_element_with_wait(locator)

    #def get_text_answer(self, locator):
    #    return self.find_element_with_wait(locator).text

    #def click_to_order_button_header(self):
        self.click_element_with_wait(MainPageLocators.ORDER_BUTTON_HEADER)

    #def click_to_order_button_footer(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_FOOTER)
        self.click_element_with_wait(MainPageLocators.ORDER_BUTTON_HEADER)

    def close_cookies(self):
        self.scroll_to_element(MainPageLocators.COOKIE_BUTTON)
        self.click_element_with_wait(MainPageLocators.COOKIE_BUTTON)
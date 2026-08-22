from base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def scroll_to_questions(self):
        self.scroll_to_element(MainPageLocators.QUESTIONS_SECTION)

    
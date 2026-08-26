from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    #def click_to_field(self, locator):
    #    self.click_element_with_wait(locator)

    def send_keys_to_field(self, data):
        self.send_keys(data)

    def select_metro_cherkizovskaya(self):
        self.click_element_with_wait(OrderPageLocators.METRO_FIELD)
        self.wait_for_element_visible(OrderPageLocators.METRO_DROPDOWN_CHERKIZ)
        self.click_element_with_wait(OrderPageLocators.METRO_DROPDOWN_CHERKIZ)

    def click_to_next_button(self):
        self.click_element_with_wait(OrderPageLocators.NEXT_BUTTON)
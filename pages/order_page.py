from .base_page import BasePage
from data import DataOrder
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    #def click_to_field(self, locator):
    #    self.click_element_with_wait(locator)

    def send_keys_to_field_name(self):
        self.send_keys(OrderPageLocators.NAME_FIELD, DataOrder.NAME)

    def send_keys_to_field_surname(self):
        self.send_keys(OrderPageLocators.SURNAME_FIELD, DataOrder.SURNAME)

    def send_keys_to_field_address(self):
        self.send_keys(OrderPageLocators.ADDRESS_FIELD, DataOrder.ADDRESS)

    def select_metro_cherkizovskaya(self):
        self.click_element_with_wait(OrderPageLocators.METRO_FIELD)
        self.wait_for_element_visible(OrderPageLocators.METRO_DROPDOWN_CHERKIZ)
        self.click_element_with_wait(OrderPageLocators.METRO_DROPDOWN_CHERKIZ)

    def send_keys_to_field_phone(self):
        self.send_keys(OrderPageLocators.PHONE_FIELD, DataOrder.PHONE)

    def click_to_next_button(self):
        self.click_element_with_wait(OrderPageLocators.NEXT_BUTTON)
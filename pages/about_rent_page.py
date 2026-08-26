from datetime import datetime, timedelta

from .base_page import BasePage
from locators.about_rent_page_locators import AboutRentPageLocators

class AboutRentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    #def click_to_field(self, locator):
    #    self.click_element_with_wait(locator)

    def get_tomorrow_date(self):
        tomorrow = datetime.now() + timedelta(days=1)
        return tomorrow.day

    def delivery_time_field_fill_tomorrow_date(self):
        self.click_element_with_wait(AboutRentPageLocators.DELIVERY_TIME_FIELD)
        tomorrow_date = self.get_tomorrow_date()
        self.send_keys(AboutRentPageLocators.DELIVERY_TIME_FIELD, tomorrow_date)

    def select_rent_time_day(self):
        self.click_element_with_wait(AboutRentPageLocators.RENT_TIME_FIELD)
        self.wait_for_element_visible(AboutRentPageLocators.RENT_TIME_DROPDOWN_DAY)
        self.click_element_with_wait(AboutRentPageLocators.RENT_TIME_DROPDOWN_DAY)
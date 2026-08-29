from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from .base_page import BasePage
from locators.about_rent_page_locators import AboutRentPageLocators

class AboutRentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_tomorrow_date(self):
        tomorrow = datetime.now() + timedelta(days=1)
        return tomorrow.strftime("%d.%m.%Y")

    def delivery_time_field_fill_tomorrow_date(self):
        self.click_element_with_wait(AboutRentPageLocators.DELIVERY_TIME_FIELD)
        tomorrow_date = self.get_tomorrow_date()
        self.send_keys(AboutRentPageLocators.DELIVERY_TIME_FIELD, tomorrow_date)
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
        
    def select_rent_time_day(self):
        self.click_element_with_wait(AboutRentPageLocators.RENT_TIME_FIELD)
        self.click_element_with_wait(AboutRentPageLocators.RENT_TIME_DROPDOWN_DAY)
import pytest

from data import DataOrder
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.about_rent_page import AboutRentPage
from locators.about_rent_page_locators import AboutRentPageLocators
from locators.order_page_locators import OrderPageLocators


class TestOrderScooter:

    @pytest.mark.parametrize('field, data', [(OrderPageLocators.NAME_FIELD, DataOrder.NAME), (OrderPageLocators.SURNAME_FIELD, DataOrder.SURNAME), (OrderPageLocators.ADDRESS_FIELD, DataOrder.ADDRESS), (OrderPageLocators.PHONE_FIELD, DataOrder.PHONE)])

    def test_button_order_in_header(self, driver, field, data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        about_rent_page = AboutRentPage(driver)

        main_page.click_to_order_button_header()
        order_page.click_element_with_wait(field)
        order_page.send_keys_to_field(data)
        order_page.select_metro_cherkizovskaya()
        order_page.click_to_next_button()
        about_rent_page.delivery_time_field_fill_tomorrow_date()
        about_rent_page.select_rent_time_day()
        about_rent_page.click_element_with_wait(AboutRentPageLocators.COLOR_CHECKBOX_BLACK_PERL)
        about_rent_page.click_element_with_wait(AboutRentPageLocators.ORDER_BUTTON_FINAL)
        about_rent_page.click_element_with_wait(AboutRentPageLocators.ORDER_BUTTON_FINAL_YES)
        assert about_rent_page.get_text(AboutRentPageLocators.HEADER_ORDER_PLACED) == 'Заказ оформлен'
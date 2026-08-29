import allure
import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.about_rent_page import AboutRentPage
from locators.about_rent_page_locators import AboutRentPageLocators
from locators.main_page_locators import MainPageLocators


class TestOrderScooter:

    @allure.title('Проверка заказа самоката')
    @allure.description('Проверка наличия всплывающего окна с сообщением об успешном создании заказа (проверяютя 2 кнопки заказа: вверху и внизу страницы).')
    @pytest.mark.parametrize('order_button', [MainPageLocators.ORDER_BUTTON_HEADER, MainPageLocators.ORDER_BUTTON_FOOTER])
    def test_order_buttons(self, driver, order_button):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        about_rent_page = AboutRentPage(driver)

        main_page.close_cookies()
        main_page.click_element_with_wait(order_button)
        order_page.send_keys_to_field_name()
        order_page.send_keys_to_field_surname()
        order_page.send_keys_to_field_address()
        order_page.select_metro_cherkizovskaya()
        order_page.send_keys_to_field_phone()
        order_page.click_to_next_button()
        about_rent_page.delivery_time_field_fill_tomorrow_date()
        about_rent_page.select_rent_time_day()
        about_rent_page.click_element_with_wait(AboutRentPageLocators.COLOR_CHECKBOX_BLACK_PERL)
        about_rent_page.click_element_with_wait(AboutRentPageLocators.ORDER_BUTTON_FINAL)
        about_rent_page.click_element_with_wait(AboutRentPageLocators.ORDER_BUTTON_FINAL_YES)
        assert 'Номер заказа' in about_rent_page.get_text(AboutRentPageLocators.HEADER_ORDER_PLACED)

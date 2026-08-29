import allure

from .base_page import BasePage
from data import DataOrder
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ввод имени')
    def send_keys_to_field_name(self):
        self.send_keys(OrderPageLocators.NAME_FIELD, DataOrder.NAME)

    @allure.step('Ввод фамилии')
    def send_keys_to_field_surname(self):
        self.send_keys(OrderPageLocators.SURNAME_FIELD, DataOrder.SURNAME)

    @allure.step('Ввод адреса')
    def send_keys_to_field_address(self):
        self.send_keys(OrderPageLocators.ADDRESS_FIELD, DataOrder.ADDRESS)

    @allure.step('Выбор из выпадающего списка станции метро (Черкизовская)')
    def select_metro_cherkizovskaya(self):
        self.click_element_with_wait(OrderPageLocators.METRO_FIELD)
        self.click_element_with_wait(OrderPageLocators.METRO_DROPDOWN_CHERKIZ)

    @allure.step('Ввод телефона')
    def send_keys_to_field_phone(self):
        self.send_keys(OrderPageLocators.PHONE_FIELD, DataOrder.PHONE)

    @allure.step('Клик по кнопке Далее')
    def click_to_next_button(self):
        self.click_element_with_wait(OrderPageLocators.NEXT_BUTTON)

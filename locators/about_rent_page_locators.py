from selenium.webdriver.common.by import By


class AboutRentPageLocators:
    #поля ввода, элементы выпадающих списков, чекбоксы
    DELIVERY_TIME_FIELD = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    RENT_TIME_FIELD = (By.XPATH, ".//div[contains(@class, 'Dropdown-placeholder') and (text()='* Срок аренды')]")
    RENT_TIME_DROPDOWN_DAY = (By.XPATH, ".//div[text()='сутки']")
    COLOR_CHECKBOX_BLACK_PERL = (By.XPATH, ".//input[@id = 'black']")
    #кнопка заказа
    ORDER_BUTTON_FINAL = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    ORDER_BUTTON_FINAL_YES = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]//button[text()='Да']")
    HEADER_ORDER_PLACED = (By.XPATH, ".//div[contains(@class, 'Order_ModalHeader') and (text()='Заказ оформлен')]")
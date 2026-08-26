from selenium.webdriver.common.by import By


class OrderPageLocators:
    #поля ввода
    NAME_FIELD = (By.XPATH, ".//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    METRO_DROPDOWN_CHERKIZ = (By.XPATH, ".//div[text()='Черкизовская']")
    PHONE_FIELD = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    #кнопка Далее
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")

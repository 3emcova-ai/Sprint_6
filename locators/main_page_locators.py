from selenium.webdriver.common.by import By


class MainPageLocators:
    #раздел Вопросы о важном
    QUESTIONS_SECTION = [By.CLASS_NAME, 'Home_SubHeader__zwi_E']
    QUESTION_COST_PAYMENT = [By.ID, 'accordion__heading-0']
    QUESTION_A_FEW_SCOOTERS = [By.ID, 'accordion__heading-1']
    QUESTION_RENTAL_TIME = [By.ID, 'accordion__heading-2']
    QUESTION_ORDER_FOR_TODAY = [By.ID, 'accordion__heading-3']
    QUESTION_RENEW_RETURN_ORDER = [By.ID, 'accordion__heading-4']
    QUESTION_BATTERY = [By.ID, 'accordion__heading-5']
    QUESTION_CANSEL_ORDER = [By.ID, 'accordion__heading-6']
    QUESTION_DELIVERY_MKAD = [By.ID, 'accordion__heading-7']
    ANSWER_COST_PAYMENT = [By.ID, 'accordion__heading-0']
    ANSWER_A_FEW_SCOOTERS = [By.ID, 'accordion__heading-1']
    ANSWER_RENTAL_TIME = [By.ID, 'accordion__heading-2']
    ANSWER_ORDER_FOR_TODAY = [By.ID, 'accordion__heading-3']
    ANSWER_RENEW_RETURN_ORDER = [By.ID, 'accordion__heading-4']
    ANSWER_BATTERY = [By.ID, 'accordion__heading-5']
    ANSWER_CANSEL_ORDER = [By.ID, 'accordion__heading-6']
    ANSWER_DELIVERY_MKAD = [By.ID, 'accordion__heading-7']


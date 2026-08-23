from selenium.webdriver.common.by import By


class MainPageLocators:
    #раздел Вопросы о важном
    QUESTIONS_SECTION = (By.XPATH, ".//div[text()='Вопросы о важном']")
    QUESTION_1_COST_PAYMENT = [By.ID, 'accordion__heading-0']
    QUESTION_2_A_FEW_SCOOTERS = [By.ID, 'accordion__heading-1']
    QUESTION_3_RENTAL_TIME = [By.ID, 'accordion__heading-2']
    QUESTION_4_ORDER_FOR_TODAY = [By.ID, 'accordion__heading-3']
    QUESTION_5_RENEW_RETURN_ORDER = [By.ID, 'accordion__heading-4']
    QUESTION_6_BATTERY = [By.ID, 'accordion__heading-5']
    QUESTION_7_ANSEL_ORDER = [By.ID, 'accordion__heading-6']
    QUESTION_8_DELIVERY_MKAD = [By.ID, 'accordion__heading-7']
    ANSWER_1 = [By.XPATH, ".//p[text()='Сутки — 400 рублей. Оплата курьеру — наличными или картой.']"] 
    ANSWER_2 = [By.XPATH, ".//p[text()='Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.']"]
    ANSWER_3 = [By.XPATH, ".//p[text()='Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.']"]
    ANSWER_4 = [By.XPATH, ".//p[text()='Только начиная с завтрашнего дня. Но скоро станем расторопнее.']"]
    ANSWER_5 = [By.XPATH, ".//p[text()='Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.']"]
    ANSWER_6 = [By.XPATH, ".//p[text()='Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.']"]
    ANSWER_7 = [By.XPATH, ".//p[text()='Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.']"]
    ANSWER_8 = [By.XPATH, ".//p[text()='Да, обязательно. Всем самокатов! И Москве, и Московской области.']"]


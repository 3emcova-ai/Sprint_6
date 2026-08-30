from locators.main_page_locators import MainPageLocators


class Urls:
    SCOOTER_URL = "https://qa-scooter.praktikum-services.ru/"
    
class DataOrder:
    NAME = 'Тест'
    SURNAME = 'Тестовый'
    ADDRESS = 'Тест 1-2'
    PHONE = '+71234567890'

class DataQuestionsAnswers:
    QUESTIONS_ANSWERS_TEXT = [
        (MainPageLocators.QUESTION_1_COST_PAYMENT,
         MainPageLocators.ANSWER_1,
         'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        (MainPageLocators.QUESTION_2_A_FEW_SCOOTERS,
          MainPageLocators.ANSWER_2,
          'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
        (MainPageLocators.QUESTION_3_RENTAL_TIME,
         MainPageLocators.ANSWER_3,
         'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
        (MainPageLocators.QUESTION_4_ORDER_FOR_TODAY,
         MainPageLocators.ANSWER_4,
         'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
        (MainPageLocators.QUESTION_5_RENEW_RETURN_ORDER,
         MainPageLocators.ANSWER_5,
         'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
        (MainPageLocators.QUESTION_6_BATTERY,
         MainPageLocators.ANSWER_6,
         'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
        (MainPageLocators.QUESTION_7_CANSEL_ORDER,
         MainPageLocators.ANSWER_7,
         'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
        (MainPageLocators.QUESTION_8_DELIVERY_MKAD,
         MainPageLocators.ANSWER_8,
         'Да, обязательно. Всем самокатов! И Москве, и Московской области.')]

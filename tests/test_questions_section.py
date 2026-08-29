import allure

from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators

class TestQuestionsSection:

    @allure.title('Проверка вопроса "Сколько это стоит? И как оплатить?"')
    @allure.description('проверка на соответствие ответа')
    def test_dropdown_question_1_correct_answer(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_questions()
        main_page.click_element_with_wait(MainPageLocators.QUESTION_1_COST_PAYMENT)
        assert main_page.get_text(MainPageLocators.ANSWER_1) == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.title('Проверка вопроса "Хочу сразу несколько самокатов! Так можно?"')
    @allure.description('проверка на соответствие ответа')
    def test_dropdown_question_2_correct_answer(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_questions()     
        main_page.click_element_with_wait(MainPageLocators.QUESTION_2_A_FEW_SCOOTERS)
        assert main_page.get_text(MainPageLocators.ANSWER_2) == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.title('Проверка вопроса "Как рассчитывается время аренды?"')
    @allure.description('проверка на соответствие ответа')
    def test_dropdown_question_3_correct_answer(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_questions()
        main_page.click_element_with_wait(MainPageLocators.QUESTION_3_RENTAL_TIME)
        assert main_page.get_text(MainPageLocators.ANSWER_3) == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    @allure.title('Проверка вопроса "Можно ли заказать самокат прямо на сегодня?"')
    @allure.description('проверка на соответствие ответа')
    def test_dropdown_question_4_correct_answer(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_questions()
        main_page.click_element_with_wait(MainPageLocators.QUESTION_4_ORDER_FOR_TODAY)
        assert main_page.get_text(MainPageLocators.ANSWER_4) == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.title('Проверка вопроса "Можно ли продлить заказ или вернуть самокат раньше?"')
    @allure.description('проверка на соответствие ответа')
    def test_dropdown_question_5_correct_answer(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_questions()
        main_page.click_element_with_wait(MainPageLocators.QUESTION_5_RENEW_RETURN_ORDER)
        assert main_page.get_text(MainPageLocators.ANSWER_5) == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    @allure.title('Проверка вопроса "Вы привозите зарядку вместе с самокатом?"')
    @allure.description('проверка на соответствие ответа')
    def test_dropdown_question_6_correct_answer(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_questions()
        main_page.click_element_with_wait(MainPageLocators.QUESTION_6_BATTERY)
        assert main_page.get_text(MainPageLocators.ANSWER_6) == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    @allure.title('Проверка вопроса "Можно ли отменить заказ?"')
    @allure.description('проверка на соответствие ответа')
    def test_dropdown_question_7_correct_answer(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_questions()
        main_page.click_element_with_wait(MainPageLocators.QUESTION_7_ANSEL_ORDER)
        assert main_page.get_text(MainPageLocators.ANSWER_7) == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    @allure.title('Проверка вопроса "Я жизу за МКАДом, привезёте?"')
    @allure.description('проверка на соответствие ответа')
    def test_dropdown_question_8_correct_answer(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_questions()
        main_page.click_element_with_wait(MainPageLocators.QUESTION_8_DELIVERY_MKAD)
        assert main_page.get_text(MainPageLocators.ANSWER_8) == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

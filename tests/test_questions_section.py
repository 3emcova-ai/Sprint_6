import allure
import pytest

from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from data import DataQuestionsAnswers

class TestQuestionsSection:

    @allure.title('Раздел Вопросы о важном')
    @allure.description('проверка вопросов на соответствие ответов')
    @pytest.mark.parametrize('question, answer, answer_text', DataQuestionsAnswers.QUESTIONS_ANSWERS_TEXT)
    def test_dropdown_question_1_correct_answer(self, driver, question, answer, answer_text):
        main_page = MainPage(driver)
        main_page.scroll_to_questions()
        main_page.click_element_with_wait(question)
        assert main_page.get_text(answer) == answer_text

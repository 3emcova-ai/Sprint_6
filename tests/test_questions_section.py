from pages.main_page import MainPage

class TestQuestionsSection:
    def test_dropdown_questions_correct_answer(driver):
        main_page = MainPage(driver)

        main_page.scroll_to_questions()





        @pytest.mark.parametrize('button_locator, section_locator, section_name', [(Locators.SAUCES_BUTTON, Locators.SAUCES_SECTION, 'Соусы'), (Locators.TOPPINGS_BUTTON, Locators.TOPPINGS_SECTION, 'Начинки')])
            def test_section_activation(self, driver, authorization, button_locator, section_locator, section_name):
                WebDriverWait(driver, 3).until(EC.presence_of_element_located(button_locator)).click()
                active_section_tab = WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.ACTIVE_SECTION_TAB)).text
                assert section_name in active_section_tab 
                assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(section_locator))
        
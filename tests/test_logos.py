from pages.main_page import MainPage


class TestLogos:

    def test_logo_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.click_logo_yandex()
        assert 'dzen.ru' in driver.current_url

    def test_logo_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_button_header()
        main_page.click_logo_scooter()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'
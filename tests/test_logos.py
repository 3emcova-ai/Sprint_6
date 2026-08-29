import allure

from pages.main_page import MainPage


class TestLogos:

    @allure.title('Проверка логотипа Яндекс')
    @allure.description('Клик на логотип Яндекса открывает в новом окне главную страницу Дзена')
    def test_logo_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.click_logo_yandex()
        assert 'dzen.ru' in driver.current_url

    @allure.title('Проверка логотипа Самокат')
    @allure.description('Клик на логотип Самоката открывает главную страницу Самоката')
    def test_logo_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_button_header()
        main_page.click_logo_scooter()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'
        
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_text(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)).text

    def send_keys(self, locator, text):
        field = self.driver.find_element(*locator)
        field.click()
        field.send_keys(text)

    def wait_for_element_visible(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    #def click_element_with_js(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].click();", element)
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

        self.wait = WebDriverWait(self.driver, 10)
        self.web_element = None

        self.find_element()

    def find_elements(self):
        elements = self.wait.until(EC.visibility_of_all_elements_located(locator=self.locator))
        return elements

    def find_element(self):
        element = self.wait.until(EC.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        return None

    def input_text(self, text):
        self.web_element.send_keys(text)
        return None

    def clear_text(self):
        self.web_element.clear()
        return None

    def click(self):
        try:
            element = self.wait.until(EC.element_to_be_clickable(mark=self.web_element))
            element.click()
        except ElementClickInterceptedException:
            element = self.wait.until(EC.element_to_be_clickable(mark=self.web_element))
            element.click()
        return None

    def attribute(self, attr_name):
        attribute =self.web_element.get_attribute(attr_name)
        return attribute

    @property
    def text(self):
        text = self.web_element.text
        return text

    @property
    def displayed(self):
        return self.web_element.is_displayed()











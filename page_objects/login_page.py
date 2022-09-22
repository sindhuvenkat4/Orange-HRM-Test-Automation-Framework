from selenium.webdriver.common.by import By

from page_objects.base_element import BaseElement
from page_objects.base_page import BasePage


class Login(BasePage):
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def username(self):
        locator = (By.CSS_SELECTOR, "[name='username']")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def password(self):
        locator = (By.CSS_SELECTOR, "[name='password']")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def login(self):
        locator = (By.CSS_SELECTOR, "[type='submit']")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )












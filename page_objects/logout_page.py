from selenium.webdriver.common.by import By

from page_objects.base_element import BaseElement
from page_objects.base_page import BasePage


class Logout(BasePage):
    def user_profile_dropdown(self):
        locator = (By.XPATH, "//img[@alt='profile picture']/../..")
        return BaseElement(
            driver=self.driver,
            locator= locator
        )

    def logout_button(self):
        locator = (By.LINK_TEXT, "Logout")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

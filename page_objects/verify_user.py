from selenium.webdriver.common.by import By
from page_objects.base_element import BaseElement
from page_objects.add_new_user import AddNewUser


class VerifyUser(AddNewUser):

    def search_button(self):
        locator = (By.XPATH, "//button[text()=' Search ']")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def find_username(self, username):
        locator = (By.XPATH, f"//div[text()='{username}']")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

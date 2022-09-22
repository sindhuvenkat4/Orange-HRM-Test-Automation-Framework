from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from page_objects.base_element import BaseElement


class EmployeeCreation(BasePage):

    def add_employee(self):
        locator = (By.LINK_TEXT, "Add Employee")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def first_name(self):
        locator = (By.CSS_SELECTOR, "[name='firstName']")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def last_name(self):
        locator = (By.CSS_SELECTOR, "[name='lastName']")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def employee_id(self):
        locator = (By.XPATH, "//label[text()='Employee Id']/../following-sibling::*/input")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def profile_picture(self):
        return self.driver.find_element(by=By.CSS_SELECTOR, value="[type='file']")

    def save(self):
        locator = (By.CSS_SELECTOR, "[type='submit']")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def user_profile_name(self):
        locator = (By.XPATH, "//img[@alt='profile picture']/following-sibling::p")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def employee_profile_name(self):
        locator = (By.CSS_SELECTOR, ".orangehrm-edit-employee-name>h6")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def home_page_logo(self):
        locator = (By.CSS_SELECTOR, ".oxd-brand-banner")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

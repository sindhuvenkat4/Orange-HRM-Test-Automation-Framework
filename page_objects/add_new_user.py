import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.base_page import BasePage
from page_objects.base_element import BaseElement
from selenium.webdriver.support import expected_conditions as EC



class AddNewUser(BasePage):
    def admin(self):
        locator = (By.XPATH, "//span[text()='Admin']")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def add_button(self):
        locator = (By.XPATH, "//button[text()=' Add ']")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def user_role(self):
        locator = (By.XPATH, "//label[text()='User Role']/../following-sibling::*/*/*")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def user_role_dropdown(self, select_option):
        user_role_div = self.driver.find_element(by=By.XPATH, value="//label[text()='User Role']/../following-sibling::*")
        user_role_div.click()
        dropdown_div_locator = (By.XPATH, "//div[@loading='false']/div")
        list =  BaseElement(
            driver=self.driver,
            locator=dropdown_div_locator
        ).find_elements()

        for option in list:
            if (select_option == option.text):
                return option

    def status(self):
        locator = (By.XPATH, "//label[text()='Status']/../following-sibling::*/*/*")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def status_dropdown(self, select_option):
        status_div = self.driver.find_element(by=By.XPATH, value="//label[text()='Status']/../following-sibling::*")
        status_div.click()
        dropdown_div_locator = (By.XPATH, "//div[@loading='false']/div")

        list = BaseElement(
            driver=self.driver,
            locator=dropdown_div_locator
        ).find_elements()

        for option in list:
            if (select_option == option.text):
                return option

    def employee_name(self):
        locator = (By.XPATH, "//label[text()='Employee Name']/../following-sibling::*/*/*/input")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def employee_name_dropdown(self, employee_name):
        dropdown_div_locator = (By.CSS_SELECTOR, "[role='listbox'] > [role='option'] > span")

        list = BaseElement(
            driver=self.driver,
            locator=dropdown_div_locator
        ).find_elements()

        for option in list:
            if (employee_name == option.text):
                return option

    def username(self):
        locator = (By.XPATH, "//label[text()='Username']/../following-sibling::*/input")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def password(self):
        locator = (By.XPATH, "//label[text()='Password']/../following-sibling::*/input")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def confirm_password(self):
        locator = (By.XPATH, "//label[text()='Confirm Password']/../following-sibling::*/input")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def save_button(self):
        locator = (By.XPATH, "//button[text()=' Save ']")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )






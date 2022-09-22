from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.add_new_user import AddNewUser
from page_objects.employee_creation import EmployeeCreation
from page_objects.login_page import Login
from jproperties import Properties

from page_objects.logout_page import Logout
from page_objects.verify_user import VerifyUser
from utilities.test_data_holder import TestDataHolder
import time
import random


class Configuration:
    config = Properties()
    with open('D:\\Code\\orange_hrm_user_creation\\configurations\\config.properties', 'rb') as config_file:
        config.load(config_file)
    admin_username = config["admin_username"].data
    admin_password = config["admin_password"].data
    get_employee_username = config["employee_username"].data
    employee_username = get_employee_username + str(int(time.time()))
    TestDataHolder.data["employee_username"] = employee_username
    employee_password = config["employee_password"].data
    first_name = config["first_name"].data
    last_name = config["last_name"].data
    # employee_id = random.randint(1000,9999)
    employee_name = first_name+" "+last_name


def login(driver, username, password):
    login_page = Login(driver=driver)
    login_page.go()
    login_page.username().input_text(username)
    login_page.password().input_text(password)
    login_page.login().click()

def employee_creation(setup, first_name, last_name):
    employee_creation = EmployeeCreation(driver=setup)
    employee_creation.add_employee().click()
    employee_creation.first_name().input_text(first_name)
    employee_creation.last_name().input_text(last_name)
    employee_creation.employee_id().input_text(random.randint(100000, 999999))
    employee_creation.profile_picture().send_keys("D:\\Code\\orange_hrm_user_creation\\test_data\\images.jpg")
    employee_creation.save().click()
    wait = WebDriverWait(setup, 3)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.oxd-toast--success')))

def add_new_user(setup):
    add_new_user = AddNewUser(driver=setup)
    add_new_user.admin().click()
    add_new_user.add_button().click()
    add_new_user.user_role().click()
    add_new_user.user_role_dropdown("ESS").click()
    add_new_user.status().click()
    add_new_user.status_dropdown("Enabled").click()
    add_new_user.employee_name().input_text(Configuration.first_name)
    add_new_user.employee_name_dropdown(Configuration.employee_name).click()
    add_new_user.username().input_text(TestDataHolder.data.get("employee_username"))
    add_new_user.password().input_text(Configuration.employee_password)
    add_new_user.confirm_password().input_text(Configuration.employee_password)
    add_new_user.save_button().click()
    try:
        wait = WebDriverWait(setup, 3)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.oxd-toast--success')))
    except TimeoutException:
        add_new_user.save_button().click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.oxd-toast--success')))

def verify_user(setup):
    verify_user = VerifyUser(driver=setup)
    verify_user.admin().click()
    verify_user.username().input_text(TestDataHolder.data.get("employee_username"))
    verify_user.user_role_dropdown("ESS").click()
    verify_user.employee_name().input_text(Configuration.first_name)
    verify_user.employee_name_dropdown(Configuration.employee_name).click()
    verify_user.status_dropdown("Enabled").click()
    verify_user.search_button().click()

def logout(setup):
    logout = Logout(driver=setup)
    logout.user_profile_dropdown().click()
    logout.logout_button().click()
from page_objects.verify_user import VerifyUser
from test_cases.common_steps import *
from test_cases.common_steps import Configuration as Cf
from utilities.test_data_holder import TestDataHolder
from page_objects.employee_creation import EmployeeCreation
from page_objects.add_new_user import AddNewUser

def test_verify_user(setup):
    login(driver=setup, username=Cf.admin_username, password=Cf.admin_password)
    # Employee Creation
    employee_creation(setup=setup, first_name=Cf.first_name, last_name=Cf.last_name)
    wait = WebDriverWait(setup, 10)
    wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".orangehrm-edit-employee-name>h6"), Cf.employee_name))

    employee_profile_name = EmployeeCreation(driver=setup).employee_profile_name().text
    assert employee_profile_name == Cf.employee_name
    # Add user
    add_new_user(setup=setup)
    # Verify User
    verify_user(setup=setup)
    actual_username = VerifyUser(driver=setup).find_username(username=TestDataHolder.data.get("employee_username")).text
    assert actual_username == TestDataHolder.data.get("employee_username")


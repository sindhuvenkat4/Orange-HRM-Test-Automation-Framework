from test_cases.common_steps import *
from test_cases.common_steps import Configuration as Cf
from utilities.test_data_holder import TestDataHolder
from page_objects.employee_creation import EmployeeCreation

def test_login_as_employee(setup):
    # Login as admin
    login(driver=setup, username=Cf.admin_username, password=Cf.admin_password)
    # Employee Creation
    employee_creation(setup=setup, first_name=Cf.first_name, last_name=Cf.last_name)
    # Add user
    add_new_user(setup=setup)
    # Verify User
    verify_user(setup=setup)
    # Logout
    # login(driver=setup, username=Cf.admin_username, password=Cf.admin_password)
    logout(setup=setup)
    # Login as employee
    login(driver=setup, username=TestDataHolder.data.get("employee_username"), password=Cf.employee_password)
    # TODO VV: addUser takes time to add to database time.sleep(3)
    profile_name = EmployeeCreation(driver=setup).user_profile_name().text
    assert profile_name == Cf.employee_name

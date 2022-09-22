from page_objects.employee_creation import EmployeeCreation
from test_cases.common_steps import *
from test_cases.common_steps import Configuration as Cf


def test_employee_creation(setup):
    login(driver=setup, username=Cf.admin_username, password=Cf.admin_password)
    employee_creation(setup=setup, first_name=Cf.first_name, last_name=Cf.last_name)
    wait = WebDriverWait(setup, 10)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".orangehrm-edit-employee-name>h6"), Cf.employee_name))

    employee_profile_name = EmployeeCreation(driver=setup).employee_profile_name().text
    assert employee_profile_name == Cf.employee_name

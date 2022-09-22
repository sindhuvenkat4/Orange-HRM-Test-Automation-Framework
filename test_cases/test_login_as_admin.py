from test_cases.common_steps import *
from test_cases.common_steps import Configuration as Cf
from page_objects.employee_creation import EmployeeCreation as EC

def test_login_page(setup):
    login(driver=setup, username=Cf.admin_username, password=Cf.admin_password)
    logo = EC(driver=setup).home_page_logo()
    assert logo.displayed

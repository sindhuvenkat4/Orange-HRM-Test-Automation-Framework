from page_objects.add_new_user import AddNewUser
from test_cases.common_steps import *
from test_cases.common_steps import Configuration as Cf
from utilities.test_data_holder import TestDataHolder
import time

def test_add_new_user(setup):
    login(driver=setup, username=Cf.admin_username, password=Cf.admin_password)
    employee_creation(setup=setup, first_name=Cf.first_name, last_name=Cf.last_name)
    add_new_user(setup=setup)

    # add_new_user = AddNewUser(driver=setup)
    # add_new_user.admin().click()
    # add_new_user.add_button().click()
    # add_new_user.user_role().click()
    # add_new_user.user_role_dropdown("ESS").click()
    # add_new_user.status().click()
    # add_new_user.status_dropdown("Enabled").click()
    # add_new_user.employee_name().input_text(Cf.first_name)
    # add_new_user.employee_name_dropdown(Cf.employee_name).click()
    # add_new_user.username().input_text(TestDataHolder.data.get("employee_username"))
    # add_new_user.password().input_text(Cf.employee_password)
    # add_new_user.confirm_password().input_text(Cf.employee_password)
    # time.sleep(1)
    # add_new_user.save_button().click()

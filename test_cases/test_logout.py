from test_cases.common_steps import *
from test_cases.common_steps import Configuration as Cf

def test_add_new_user(setup):
    login(driver=setup, username=Cf.admin_username, password=Cf.admin_password)
    logout(setup=setup)

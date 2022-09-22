import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(name="setup")
def setup_chrome():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    return webdriver.Chrome(service=service)

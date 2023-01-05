import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# this is an example of classic xunit style setup
driver = None
def setup_module(module):
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://google.com")
    driver.implicitly_wait(3)

def teardown_module(module):
    driver.quit()

def test_google():
    assert driver.title == "Google"

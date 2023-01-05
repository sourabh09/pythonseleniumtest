import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#this is an example of using pytest fixtures 1, module level
driver = None

@pytest.fixture(scope="module")
def init_driver():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.get("https://www.google.com/")
    driver.implicitly_wait(5)
    yield
    driver.quit()

@pytest.mark.usefixtures("init_driver")
def test_google_title():
    assert driver.title == "Google"
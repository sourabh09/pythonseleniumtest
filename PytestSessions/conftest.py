import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
driver = None

@pytest.fixture(params=["chrome","edge"],scope="class")
def setup(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == "edge":
        web_driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    request.cls.driver = web_driver
    yield
    web_driver.quit()

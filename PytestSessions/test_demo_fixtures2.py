import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#this is an example of using pytest fixtures 2, class levels
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

@pytest.mark.usefixtures("setup")
class BaseTest:
    pass

class Test_google(BaseTest):

    def test_google_title(self):
        self.driver.get("https://www.google.com/")
        assert self.driver.title == "Google"







import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class BaseTest:
    pass

class TestGnewsParams(BaseTest):

    @pytest.mark.parametrize(
            "username, password",
        [("admin@gmail.com","Password 123"),
          ("sourabh9890@gmail.com","Test123")
        ]
        )
    def test_gnews_params(self, username, password):
        self.driver.get("https://gnews.io/login")
        self.driver.find_element(By.ID, "inputEmail").send_keys(username)
        self.driver.find_element(By.ID, "inputPassword").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "button.btn").click()
        assert self.driver.find_element(By.XPATH, "// li[text() = 'Wrong email or password']").is_displayed()





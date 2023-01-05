import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

browserName = "chrome"
try:
    if browserName == "chrome":
     driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browserName == "edge":
     driver = webdriver.Edge(EdgeChromiumDriverManager().install())
except Exception:
        print("Provided browser is not available")

driver.get("https://www.google.com/")

print(driver.title)
time.sleep(5)
driver.quit()


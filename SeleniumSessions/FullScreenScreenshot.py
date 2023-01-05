import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get("https://testng.org/doc/selenium.html")

print(driver.title)

S = lambda X : driver.execute_script("return document.body.parentNode.scroll"+X)
driver.set_window_size(S('Width'), S('Height'))
print(S('Width'), S('Height'))

driver.find_element(By.TAG_NAME, 'body').screenshot("Fullpagess1.png")
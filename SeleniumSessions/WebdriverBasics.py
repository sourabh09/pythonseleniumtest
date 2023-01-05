from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\Automationtesting\drivers\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://www.google.com/")
driver.maximize_window()

driver.find_element(By.NAME,"q").send_keys("naveen automationlabs")
driver.implicitly_wait(3)
list = driver.find_elements(By.CSS_SELECTOR, "ul.G43f7e li span")

print(len(list))

for ele in list:
    driver.implicitly_wait(2)
    if ele.text == "naveen automationlabs youtube":
        ele.click()
        break

driver.implicitly_wait(5)
driver.quit()


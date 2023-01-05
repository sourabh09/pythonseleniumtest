import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")

print(driver.title)

def clickDropdownValues(dropdown_options, values):
    if not values[0] == "all":
        for ele in dropdown_options:
            for k in range(len(values)):
                if values[k] == ele.text:
                    ele.click()
                    break
    else:
        try:
            for ele in dropdown_options:
                ele.click()
        except Exception as e:
            print(e)



driver.find_element(By.ID, 'justAnInputBox').click()

dropdown_options = driver.find_elements(By.CSS_SELECTOR, "span.comboTreeItemTitle")
driver.implicitly_wait(3)
values = ["choice 7"]
#print(len(dropdown_options))

for ele in dropdown_options:
    print(ele.text)

clickDropdownValues(dropdown_options, values)

time.sleep(10)

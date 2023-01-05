import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

def test_google():
    driver.get("https://google.com")
    print(driver.title)
    assert driver.title == "Google"

def test_facebook():
    driver.get("https://www.facebook.com/")
    print(driver.title)
    assert driver.title == "Facebook – log in or sign up"

def test_instagram():
    driver.get("https://www.instagram.com/")
    print(driver.title)
    assert driver.title == "Instagram"

def test_gnews():
    driver.get("https://gnews.io/register")
    print(driver.title)
    assert driver.title == "Sign up - GNews API"




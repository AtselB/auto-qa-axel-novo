import time
from selenium.webdriver.common.by import By



URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

def login(driver, USERNAME=USERNAME, PASSWORD=PASSWORD):
    
    driver.get(URL)

    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)

    driver.find_element(By.ID, "login-button").click()
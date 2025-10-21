import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_setup import create_driver
from utils.login_setup import login

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

def test_login(driver):
    login(driver)

    wait = WebDriverWait(driver, 5)
    wait.until(EC.url_contains("/inventory.html"))

    assert "/inventory.html" in driver.current_url

    title = driver.find_element(By.CLASS_NAME, "title").text
    assert "Products" in title

def test_incorrect_login(driver):
    login(driver, "incorrect_user", "incorrect_password")

    wait = WebDriverWait(driver, 5)
    
    error_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container")))
    assert "Epic sadface" in error_message.text
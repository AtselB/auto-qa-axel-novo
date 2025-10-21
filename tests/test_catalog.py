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

def test_catalog(driver):
    login(driver)

    wait = WebDriverWait(driver, 5)
    wait.until(EC.url_contains("/inventory.html"))

    assert "/inventory.html" in driver.current_url

    inventory_items = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(inventory_items) > 0

    first_item = inventory_items[0]
    assert "Backpack" in first_item.text

    filters = driver.find_element(By.CLASS_NAME, "product_sort_container").text
    assert "Name (A to Z)" in filters
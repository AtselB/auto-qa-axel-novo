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

def test_shopping_cart(driver):
    login(driver)

    wait = WebDriverWait(driver, 5)
    wait.until(EC.url_contains("/inventory.html"))

    inventory_items = driver.find_elements(By.CLASS_NAME, "inventory_item")
    inventory_items[0].find_element(By.TAG_NAME, "a").click()

    wait.until(EC.url_contains("/inventory-item.html"))
    assert "/inventory-item.html" in driver.current_url

    driver.find_element(By.ID, "add-to-cart").click()

    sc_badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))).text
    assert "1" in sc_badge

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    wait.until(EC.url_contains("/cart.html"))
    assert "/cart.html" in driver.current_url

    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) > 0

    cart_item = cart_items[0]
    assert "Backpack" in cart_item.find_element(By.CLASS_NAME, "cart_item_label").text

    assert "1" in cart_item.find_element(By.CLASS_NAME, "cart_quantity").text

    checkout = driver.find_element(By.ID, "checkout")
    assert "Checkout" in checkout.text


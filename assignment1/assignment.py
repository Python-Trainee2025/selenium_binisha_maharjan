import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def safe_click(driver, by, value):

    time.sleep(1)
    elements = driver.find_elements(by, value)
    if elements:
        elements[0].click()
        return True
    return False


@pytest.mark.parametrize(
    "username,password",[("standard_user", "secret_sauce"),("problem_user", "secret_sauce"),("performance_glitch_user", "secret_sauce"),])
def test_demo(username, password):
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    # Login
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(5)

    # Add two products
    safe_click(driver, By.ID, "add-to-cart-sauce-labs-backpack")
    safe_click(driver, By.ID, "add-to-cart-sauce-labs-bike-light")
    time.sleep(2)

    # Go to cart
    safe_click(driver, By.CLASS_NAME, "shopping_cart_link")
    time.sleep(3)

    # Remove one item
    safe_click(driver, By.ID, "remove-sauce-labs-backpack")
    time.sleep(2)

    # Continue shopping
    safe_click(driver, By.ID, "continue-shopping")
    time.sleep(3)

    # Open backpack product detail page
    safe_click(driver, By.ID, "item_4_title_link")
    time.sleep(2)

    # Add again from detail page
    safe_click(driver, By.ID, "add-to-cart-sauce-labs-backpack")
    time.sleep(2)

    driver.quit()

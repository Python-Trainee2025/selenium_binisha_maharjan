import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.mark.parametrize(
    "username,password",
    [
        ("standard_user", "secret_sauce"),
        ("problem_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce"),
    ]
)
def test_saucedemo_simple(username, password):

    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.saucedemo.com/")
    time.sleep(1)

    # Login
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # Add two products
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    time.sleep(1)

    # Go to cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # IMPORTANT: wait more because cart loads slowly
    time.sleep(3)

    # Remove one item
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    time.sleep(1)

    # Continue shopping
    driver.find_element(By.ID, "continue-shopping").click()
    time.sleep(2)

    # Open product detail
    driver.find_element(By.ID, "item_4_title_link").click()
    time.sleep(1)

    # Add product from details
    driver.find_element(By.ID, "add-to-cart").click()
    time.sleep(2)

    driver.quit()

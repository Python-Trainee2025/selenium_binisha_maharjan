import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



@pytest.mark.parametrize(
    "username,password",
    [("standard_user", "secret_sauce"),("problem_user", "secret_sauce"),("performance_glitch_user", "secret_sauce"),])

def test_demo(username,password):
    def test_demo(username, password):
        chrome_options = Options()
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)

        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        time.sleep(2)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        time.sleep(1)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        time.sleep(1)

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(2)
        items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        cart_items = []
        for i in items:
            cart_items.append(i.text)
        print(cart_items)

        # remove one item from the cart
        driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
        time.sleep(2)

        # Go back to the product page via menu
        # driver.find_element(By.ID,"react-burger-menu-btn").click()
        # time.sleep(2)
        # driver.find_element(By.ID,"inventory_sidebar_link").click()
        # time.sleep(2)

        # goback to product page via continue shopping button
        continue_shopping = driver.find_element(By.ID, "continue-shopping")
        actions = ActionChains(driver)
        actions.move_to_element(continue_shopping).click().perform()
        time.sleep(2)

        # Open a product detail page and add that product to the cart.
        product = driver.find_element(By.CLASS_NAME, "inventory_item_name")
        actions.move_to_element(product).click().perform()
        time.sleep(2)
        driver.find_element(By.ID, "add-to-cart").click()
        time.sleep(2)

        driver.quit()














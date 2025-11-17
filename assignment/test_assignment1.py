import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


@pytest.mark.parametrize(
    "username,password",
    [
        ("standard_user", "secret_sauce"),
        ("problem_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce"),
    ]
)
def test_saucedemo_flow(driver, username, password):

    wait = WebDriverWait(driver, 30)

    # -----------------------------------------------------
    # LOGIN
    # -----------------------------------------------------
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(username)
    time.sleep(1)

    driver.find_element(By.ID, "password").send_keys(password)
    time.sleep(1)

    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))

    # -----------------------------------------------------
    # ADD FIRST 2 ITEMS TO CART
    # -----------------------------------------------------
    add_buttons = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[id*='add-to-cart']"))
    )

    add_buttons[0].click()
    time.sleep(1)

    add_buttons[1].click()
    time.sleep(1)

    # -----------------------------------------------------
    # OPEN CART
    # -----------------------------------------------------
    driver.find_element(By.ID, "shopping_cart_container").click()
    time.sleep(1)

    cart_items = wait.until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item"))
    )

    # -----------------------------------------------------
    # REMOVE ONE ITEM
    # -----------------------------------------------------
    remove_buttons = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[id*='remove']"))
    )

    remove_buttons[0].click()
    time.sleep(1)

    # -----------------------------------------------------
    # BACK TO PRODUCTS
    # -----------------------------------------------------
    wait.until(EC.element_to_be_clickable((By.ID, "continue-shopping"))).click()
    time.sleep(1)

    # -----------------------------------------------------
    # OPEN PRODUCT DETAIL PAGE
    # -----------------------------------------------------
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Sauce Labs Backpack']"))
    ).click()
    time.sleep(1)

    # -----------------------------------------------------
    # ADD PRODUCT FROM DETAIL PAGE
    # -----------------------------------------------------
    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id*='add-to-cart']"))
    ).click()
    time.sleep(1)

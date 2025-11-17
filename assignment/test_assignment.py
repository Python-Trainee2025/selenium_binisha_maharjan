import pytest
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
    [("standard_user", "secret_sauce"),("problem_user", "secret_sauce"),("performance_glitch_user", "secret_sauce"),])
def test_saucedemo_flow(driver, username, password):

    wait = WebDriverWait(driver, 30)
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()


    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))


    add_buttons = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[id*='add-to-cart']"))
    )
    assert len(add_buttons) >= 2

    add_buttons[0].click()
    add_buttons[1].click()

    driver.find_element(By.ID, "shopping_cart_container").click()

    cart_items = wait.until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item"))
    )
    assert len(cart_items) >= 2

    remove_buttons = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[id*='remove']"))
    )
    assert len(remove_buttons) >= 1
    remove_buttons[0].click()

    remaining_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(remaining_items) == 1

    wait.until(EC.element_to_be_clickable((By.ID, "continue-shopping"))).click()

    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Sauce Labs Backpack']"))
    ).click()



    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id*='add-to-cart']"))
    ).click()

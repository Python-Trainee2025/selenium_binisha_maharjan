from selenium.webdriver.common.by import By

class ProductsLocators:
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_BIKE_LIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    CART_BTN = (By.CLASS_NAME, "shopping_cart_link")
    BACKPACK_TITLE = (By.ID, "item_4_title_link")

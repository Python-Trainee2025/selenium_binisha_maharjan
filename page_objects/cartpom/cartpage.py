import time
from page_objects.cartpom.cartprops import CartProperties

class CartPage(CartProperties):

    def __init__(self, driver):
        self.driver = driver

    def remove_one_item(self):
        self.remove_backpack.click()
        time.sleep(2)

    def continue_shopping_click(self):
        self.continue_shopping.click()
        time.sleep(2)

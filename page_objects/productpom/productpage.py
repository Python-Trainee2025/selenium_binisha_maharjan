import time
from page_objects.productpom.produtprops import ProductsProperties

class ProductsPage(ProductsProperties):

    def __init__(self, driver):
        self.driver = driver

    def add_two_products(self):
        self.add_backpack.click()
        time.sleep(1)
        self.add_bike_light.click()
        time.sleep(2)

    def open_cart(self):
        self.cart_button.click()
        time.sleep(2)

    def open_backpack_details(self):
        self.backpack_title.click()
        time.sleep(2)

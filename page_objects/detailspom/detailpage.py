import time
from page_objects.detailspom.detail_props import DetailsProperties

class DetailsPage(DetailsProperties):

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        self.add_backpack.click()
        time.sleep(2)

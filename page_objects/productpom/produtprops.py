from page_objects.productpom.productlocator import ProductsLocators

class ProductsProperties(ProductsLocators):

    @property
    def add_backpack(self):
        return self.driver.find_element(*self.ADD_BACKPACK)

    @property
    def add_bike_light(self):
        return self.driver.find_element(*self.ADD_BIKE_LIGHT)

    @property
    def cart_button(self):
        return self.driver.find_element(*self.CART_BTN)

    @property
    def backpack_title(self):
        return self.driver.find_element(*self.BACKPACK_TITLE)

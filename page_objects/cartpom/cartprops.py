from .cartlocator import CartLocators

class CartProperties(CartLocators):

    @property
    def remove_backpack(self):
        return self.driver.find_element(*self.REMOVE_BACKPACK)

    @property
    def continue_shopping(self):
        return self.driver.find_element(*self.CONTINUE_SHOPPING)

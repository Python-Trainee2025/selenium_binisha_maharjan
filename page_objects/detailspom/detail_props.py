from page_objects.detailspom.detaillocator import DetailLocators

class DetailsProperties(DetailLocators):
    @property
    def add_backpack(self):
        return self.driver.find_element(*self.ADD_BACKPACK)

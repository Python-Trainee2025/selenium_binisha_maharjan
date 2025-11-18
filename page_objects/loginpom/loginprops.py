from page_objects.loginpom.loginlocator import LoginLocators


class LoginProperties(LoginLocators):

    @property
    def username(self):
        return self.driver.find_element(*self.USERNAME)

    @property
    def password(self):
        return self.driver.find_element(*self.PASSWORD)

    @property
    def login_btn(self):
        return self.driver.find_element(*self.LOGIN_BTN)

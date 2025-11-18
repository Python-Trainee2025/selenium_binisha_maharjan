import time
from page_objects.loginpom.loginprops import LoginProperties

class LoginPage(LoginProperties):

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.login_btn.click()
        time.sleep(3)

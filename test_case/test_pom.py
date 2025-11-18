import pytest
from setup.basetest import BaseTest
from page_objects.loginpom.loginpage import LoginPage
from page_objects.productpom.productpage import ProductsPage
from page_objects.cartpom.cartpage import CartPage
from page_objects.detailspom.detailpage import DetailsPage


class TestSauceDemo(BaseTest):

    @pytest.mark.parametrize(
        "username,password",
        [("standard_user", "secret_sauce"),("problem_user", "secret_sauce"),("performance_glitch_user", "secret_sauce"),])
    def test_demo(self, username, password):

        self.open_url("https://www.saucedemo.com/")

        login = LoginPage(self.driver)
        products = ProductsPage(self.driver)
        cart = CartPage(self.driver)
        details = DetailsPage(self.driver)

        login.login(username, password)

        products.add_two_products()
        products.open_cart()

        cart.remove_one_item()
        cart.continue_shopping_click()

        products.open_backpack_details()

        details.add_to_cart()

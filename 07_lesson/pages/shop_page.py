from selenium.webdriver.common.by import By
from .base_page import BasePage

class ShopPage(BasePage):
    BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_BTN = (By.CLASS_NAME, "shopping_cart_link")

    def add_to_cart(self, locator):
        self.click(locator)

    def go_to_cart(self):
        self.click(self.CART_BTN)

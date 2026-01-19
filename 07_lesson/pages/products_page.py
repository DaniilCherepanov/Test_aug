from selenium.webdriver.common.by import By

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    def add_bolt_tshirt(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

    def add_onesie(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()

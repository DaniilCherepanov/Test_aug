from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure


class CartPage(BasePage):
    CHECKOUT_BTN = (By.ID, "checkout")

    @allure.step("Начало оформления заказа")
    def checkout(self):
        """
        Начинает оформление заказа, нажимая на кнопку 'Checkout'.
        """
        self.click(self.CHECKOUT_BTN)

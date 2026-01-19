from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure


class ShopPage(BasePage):
    BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_BTN = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("Добавление товара в корзину")
    def add_to_cart(self, locator):
        """
        Добавляет товар в корзину.

        :param locator: Локатор кнопки добавления товара
        """
        self.click(locator)

    @allure.step("Переход в корзину")
    def go_to_cart(self):
        """
        Переходит в корзину покупок.
        """
        self.click(self.CART_BTN)

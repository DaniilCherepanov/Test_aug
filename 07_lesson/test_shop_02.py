import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from pages.shop_page import ShopPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_shop_checkout(driver):
    login_page = LoginPage(driver)
    shop_page = ShopPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    shop_page.add_to_cart(shop_page.BACKPACK)
    shop_page.add_to_cart(shop_page.TSHIRT)
    shop_page.add_to_cart(shop_page.ONESIE)

    shop_page.go_to_cart()
    cart_page.checkout()

    checkout_page.fill_form("Иван", "Петров", "123456")

    total = checkout_page.get_total()
    print("TOTAL:", total)
    assert total == "Total: $58.29"

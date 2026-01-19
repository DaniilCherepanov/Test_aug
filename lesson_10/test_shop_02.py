import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import allure

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


@allure.title("Тестирование оформления заказа")
@allure.description("Проверка добавления товаров в корзину и оформления заказа")
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.NORMAL)
def test_shop_checkout(driver):
    login_page = LoginPage(driver)
    shop_page = ShopPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    with allure.step("Открытие страницы авторизации"):
        login_page.open("https://www.saucedemo.com/")

    with allure.step("Вход в систему"):
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавление товаров в корзину"):
        shop_page.add_to_cart(shop_page.BACKPACK)
        shop_page.add_to_cart(shop_page.TSHIRT)
        shop_page.add_to_cart(shop_page.ONESIE)

    with allure.step("Переход в корзину"):
        shop_page.go_to_cart()

    with allure.step("Начало оформления заказа"):
        cart_page.checkout()

    with allure.step("Заполнение формы заказа"):
        checkout_page.fill_form("Даниил", "Черепанов", "777777")

    with allure.step("Проверка итоговой суммы"):
        total = checkout_page.get_total()
        print("TOTAL:", total)
        assert total == "Total: $58.29"

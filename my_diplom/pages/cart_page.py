from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """Класс для работы со страницей корзины."""

    def __init__(self, driver):
        """Инициализация страницы.

        Args:
            driver (webdriver.Chrome): экземпляр драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def go_to_cart(self):
        """Переходит в корзину через ссылку.

        Raises:
            Exception: если переход не удался (сохраняет скриншот).
        """
        try:
            cart_link = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/cart')]"))
            )
            cart_link.click()
            self.wait.until(lambda driver: "/cart" in driver.current_url)
        except Exception as e:
            self.driver.save_screenshot("cart_error.png")
            raise e

    def wait_for_cart_to_load(self):
        """Ожидает загрузки корзины."""
        self.wait.until(lambda driver: "/cart" in driver.current_url)

    def get_cart_items_count(self) -> int:
        """Возвращает количество товаров в корзине.

        Returns:
            int: число товаров в корзине.
        """
        items = self.driver.find_elements(By.CSS_SELECTOR, ".cart-item")
        return len(items)

    def is_item_in_cart(self, book_title: str) -> bool:
        """Проверяет, есть ли книга в корзине.

        Args:
            book_title (str): название книги для поиска.

        Returns:
            bool: True, если книга найдена в корзине.
        """
        item_titles = self.driver.find_elements(
            By.CSS_SELECTOR,
            ".cart-item-title, .product-name"
        )
        return any(
            book_title.lower() in title_elem.text.lower()
            for title_elem in item_titles
        )

    def open_from_header(self):
        """Открывает корзину через кнопку в шапке сайта."""
        cart_button = self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                "#__nuxt > div > div.app-header.app-wrapper__sticky-header > div > header > div > div.header-controls.header-sticky__controls > button:nth-child(4) > span.header-controls__text"
            ))
        )
        cart_button.click()

    def increase_item_quantity(self):
        """Увеличивает количество товара в корзине на 1."""
        increase_button = self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                "svg.chg-ui-input-number__input-control.chg-ui-input-number__input-control--increment"
            ))
        )
        increase_button.click()

    def remove_item_from_cart(self):
        """Удаляет товар из корзины."""
        remove_button = self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                "button.cart-item__delete-button"
            ))
        )
        remove_button.click()

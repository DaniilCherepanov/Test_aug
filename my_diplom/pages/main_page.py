from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    """Класс для взаимодействия с главной страницей сайта."""

    def __init__(self, driver):
        """Инициализация страницы.

        Args:
            driver (webdriver.Chrome): экземпляр драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)
        self.search_input = (By.CSS_SELECTOR, "input[name='search']")
        self.search_button = (By.XPATH, "//button[@aria-label='Найти']")

    def open(self, url: str = "https://www.chitai-gorod.ru"):
        """Открывает главную страницу.

        Args:
            url (str): URL для открытия (по умолчанию — основной сайт).
        """
        self.driver.get(url)

    def search_book(self, title: str):
        """Выполняет поиск книги по названию.

        Args:
            title (str): название книги для поиска.
        """
        search_input = self.wait.until(EC.element_to_be_clickable(self.search_input))
        search_input.clear()
        search_input.send_keys(title)
        search_button = self.wait.until(EC.element_to_be_clickable(self.search_button))
        search_button.click()

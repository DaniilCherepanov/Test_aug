from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResultsPage:
    """Класс для работы с страницей результатов поиска."""

    def __init__(self, driver):
        """Инициализация страницы.

        Args:
            driver (webdriver.Chrome): экземпляр драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def get_book_titles(self) -> list[str]:
        """Получает список названий книг на странице.

        Returns:
            list[str]: список названий книг.
        """
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-card__title"))
        )
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".product-card__title")
        titles = []
        for el in elements:
            text = el.text.strip()
            if text:
                titles.append(text)
        return titles

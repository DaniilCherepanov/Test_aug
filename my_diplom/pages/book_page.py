from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BookPage:
    """Класс для работы со страницей книги."""

    def __init__(self, driver):
        """Инициализация страницы.

        Args:
            driver (webdriver.Chrome): экземпляр драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 45)

    def click_buy_button(self):
        """Кликает по кнопке «Купить/В корзину».

        Raises:
            TimeoutException: если кнопка не найдена за 45 секунд.
        """
        try:
            button = self.wait.until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//button[contains(., 'Купить') or contains(., 'В корзину')]"
                ))
            )
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
            button.click()
        except TimeoutException:
            raise TimeoutException("Не удалось найти кнопку «Купить/В корзину» на странице.")

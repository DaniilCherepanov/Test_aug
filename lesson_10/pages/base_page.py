from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    def __init__(self, driver):
        """
        Инициализация базового класса страницы.

        :param driver: WebDriver — объект драйвера Selenium
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открытие страницы")
    def open(self, url: str) -> None:
        """
        Открывает указанную страницу.

        :param url: str — URL страницы
        """
        self.driver.get(url)

    @allure.step("Нажатие на элемент")
    def click(self, locator) -> None:
        """
        Нажимает на указанный элемент.

        :param locator: кортеж (By.ID, "id") или аналогичный локатор
        """
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Заполнение поля")
    def fill(self, locator, text: str) -> None:
        """
        Заполняет указанное поле текстом.

        :param locator: кортеж (By.ID, "id") или аналогичный локатор
        :param text: str — текст для ввода
        """
        elem = self.wait.until(EC.visibility_of_element_located(locator))
        elem.clear()
        elem.send_keys(text)

    @allure.step("Получение текста элемента")
    def get_text(self, locator) -> str:
        """
        Возвращает текст указанного элемента.

        :param locator: кортеж (By.ID, "id") или аналогичный локатор
        :return: str — текст элемента
        """
        return self.wait.until(EC.visibility_of_element_located(locator)).text

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalcPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    @allure.step("Открытие страницы калькулятора")
    def open(self):
        """
        Открывает страницу калькулятора.
        """
        self.driver.get(self.URL)

    @allure.step("Установка задержки {value} секунд")
    def set_delay(self, value: str):
        """
        Устанавливает задержку для выполнения операций на калькуляторе.

        :param value: str — время задержки в секундах.
        """
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(value)

    @allure.step(f"Нажатие кнопки '{symbol}'")
    def click_button(self, symbol: str):
        """
        Нажимает на кнопку калькулятора.

        :param symbol: str — символ на кнопке, которую нужно нажать.
        """
        btn = self.driver.find_element(By.XPATH, f"//span[text()='{symbol}']")
        btn.click()

    @allure.step("Получение результата с экрана калькулятора")
    def get_result(self):
        """
        Возвращает текущий результат с экрана калькулятора.

        :return: str — текст результата на экране калькулятора.
        """
        self.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
        return self.driver.find_element(By.CLASS_NAME, "screen").text

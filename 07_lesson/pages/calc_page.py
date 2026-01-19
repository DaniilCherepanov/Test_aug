from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, value: str):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(value)

    def click_button(self, symbol: str):
        btn = self.driver.find_element(By.XPATH, f"//span[text()='{symbol}']")
        btn.click()

    def get_result(self):
        # ждём, пока результат появится в дисплее
        self.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
        return self.driver.find_element(By.CLASS_NAME, "screen").text

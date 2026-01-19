from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import TimeoutException


def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("http://uitestingplayground.com/ajax")

    driver.find_element(By.ID, "ajaxButton").click()

    wait = WebDriverWait(driver, 20)

    try:

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".bg-success")))

        wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".bg-success"),
                "Data loaded with AJAX get request."
            )
        )

        element = driver.find_element(By.CSS_SELECTOR, ".bg-success")
        print("Текст из плашки:", element.text)

    except TimeoutException:
        print("⛔ Не дождались загрузки текста в плашке")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()

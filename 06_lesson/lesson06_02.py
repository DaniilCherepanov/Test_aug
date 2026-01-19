from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://uitestingplayground.com/textinput")

    wait = WebDriverWait(driver, 10)

    input_field = wait.until(
        EC.presence_of_element_located((By.ID, "newButtonName"))
    )
    input_field.send_keys("SkyPro")

    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    wait.until(EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro"))

    print("Кнопка теперь называется:", button.text)

    driver.quit()


if __name__ == "__main__":
    main()

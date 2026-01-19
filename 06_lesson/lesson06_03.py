from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    wait = WebDriverWait(driver, 20)

    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "img")) >= 3)

    images = driver.find_elements(By.CSS_SELECTOR, "img")

    third_img = images[2]
    src_value = third_img.get_attribute("src")

    print("SRC третьей картинки:", src_value)

    driver.quit()


if __name__ == "__main__":
    main()

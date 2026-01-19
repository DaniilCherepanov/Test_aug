from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/dynamicid")

button = driver.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']")

button.click()

time.sleep(2)

driver.quit()

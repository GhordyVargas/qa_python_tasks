from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://demoqa.com/elements")

button = driver.find_element(By.ID, "doubleClickBtn")
button.click()

result = driver.find_element(By.ID, "doubleClickMessage").text
print(f"Double click result: {result}")

time.sleep(2)
driver.quit()

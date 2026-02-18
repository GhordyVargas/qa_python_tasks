from selenium import webdriver

URL = "https://around-v1.nm.tripleten-services.com/signin?lng=es"

driver = webdriver.Chrome()
try:
    driver.get(URL)
    assert "/signin" in driver.current_url, f"URL incorrecta: {driver.current_url}"
finally:
    driver.quit()

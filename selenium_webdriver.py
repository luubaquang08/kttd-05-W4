import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_submit_form():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        assert driver.title == "Web form"

        wait = WebDriverWait(driver, timeout=10)
        text_box = wait.until(EC.presence_of_element_located((By.NAME, "my-text")))
        submit_button = driver.find_element(By.CSS_SELECTOR, "button")

        text_box.send_keys("Selenium")
        submit_button.click()

        message = wait.until(EC.visibility_of_element_located((By.ID, "message")))
        assert message.text == "Received!"
    finally:
        driver.quit()
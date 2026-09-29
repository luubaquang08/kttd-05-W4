import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    page_title = driver.title
    print(f"Tiêu đề trang: {page_title}")
    assert page_title == "Web form", "Tiêu đề trang không đúng!"

    wait = WebDriverWait(driver, timeout=10)
    text_box = wait.until(EC.presence_of_element_located((By.NAME, "my-text")))
    submit_button = driver.find_element(By.CSS_SELECTOR, "button")

    text_box.send_keys("Selenium Automation")
    submit_button.click()

    message_element = wait.until(EC.visibility_of_element_located((By.ID, "message")))
    result_text = message_element.text
    print(f"Kết quả nhận được: {result_text}")
    assert result_text == "Received!", "Form chưa được gửi thành công!"

    print("Test passed thành công!")

finally:
    driver.quit()
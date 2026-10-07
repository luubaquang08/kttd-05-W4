import pytest
from selenium import webdriver

def test_open_google():  # Bắt buộc phải có chữ test_ ở đầu tên hàm
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()
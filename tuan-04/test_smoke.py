import pytest
from selenium import webdriver

def test_smoke():
    # 1. Khởi tạo và mở trình duyệt Google Chrome
    driver = webdriver.Chrome()
    
    # 2. Điều hướng trình duyệt truy cập đến trang web bài tập
    driver.get("https://the-internet.herokuapp.com/")
    
    # 3. Lấy tiêu đề thực tế của trang web và so sánh với tiêu đề mong đợi "The Internet"
    # Lệnh assert sẽ kiểm tra điều kiện: Nếu đúng thì PASS, nếu sai thì báo lỗi FAIL
    assert driver.title == "The Internet"
    
    # 4. Tắt trình duyệt và dọn dẹp tài nguyên sau khi kiểm thử xong
    driver.quit()
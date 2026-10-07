# Ghi chú tuần 04

## Thành viên: Hồ Tùng Bách - A48138

### 1. Điều đã học được trong tuần
* Nắm được cách thiết lập và viết test case cơ bản với **Selenium** và **pytest** trong Python để tự động mở trình duyệt, điều hướng URL và kiểm tra tiêu đề trang web (`assert`).
* Hiểu được quy ước đặt tên của pytest (hàm test phải có tiền tố `test_`) và vòng đời kiểm thử tự động (mở trình duyệt -> tương tác/kiểm tra -> giải phóng tài nguyên với `driver.quit()`).
* Thành thạo hơn các thao tác Git cơ bản khi làm việc nhóm: quản lý branch, staging (`git add`), commit có ý nghĩa và đẩy nhánh lên GitHub (`git push -u origin <branch>`).

---

### 2. Trả lời câu hỏi phần đọc / lý thuyết
* **Câu hỏi 1: Vì sao cần phải gọi `driver.quit()` trong khối `finally` hoặc fixture teardown?**
  * *Trả lời:* Để đảm bảo dù test case có chạy thành công (`PASSED`) hay gặp lỗi văng Exception (`FAILED`), tiến trình trình duyệt Chrome chạy ngầm vẫn luôn được đóng giải phóng RAM và CPU cho hệ thống.
* **Câu hỏi 2: Sự khác nhau giữa `assert` trong test case và lệnh `print` thông thường là gì?**
  * *Trả lời:* `print` chỉ in thông tin ra màn hình console để quan sát, không quyết định kết quả test. Còn `assert` là điều kiện kiểm tra logic, nếu sai sẽ ném ra `AssertionError` để pytest đánh dấu test case là thất bại (`FAILED`).

---

### 3. Nhật ký sử dụng AI (AI Prompting Log)
* **Đã hỏi AI điều gì:**
  1. Hỏi nguyên nhân tại sao chạy `pytest` thì Chrome bật lên rồi tắt ngay lập tức và báo `no tests ran`.
  2. Nhờ sửa code mẫu Selenium sang chuẩn cấu trúc test function của pytest.
  3. Hỏi lý do tại sao đã tạo branch và commit ở máy local nhưng trên giao diện GitHub không thấy nhánh hiển thị.
* **Câu trả lời của AI có đúng không:**
  * Câu trả lời rất chính xác và trúng vấn đề:
    * Chỉ ra đúng lỗi do viết code tuần tự ở module level thay vì đặt trong hàm `def test_*()`.
    * Giải thích đúng việc nhánh mới chỉ nằm ở local và hướng dẫn dùng lệnh `git push -u origin <branch>` để đẩy lên remote.
* **Bản thân hiểu thêm được gì:**
  * Hiểu cơ chế hoạt động của `pytest` tự động thu thập test (test discovery) dựa trên naming convention (`test_*.py` và `def test_*()`).
  * Phân biệt được sự tách biệt giữa Git Local (kho lưu trên máy cá nhân) và Git Remote (kho lưu trữ trên GitHub).
# Ghi Chú Học Tập - Tuần 04

## 1. Thu hoạch cá nhân

### Thành viên 1: [Họ và tên sinh viên 1] (Vai trò: Driver)
* **Điều đã học:** Biết cách thao tác cài đặt các thư viện kiểm thử như `selenium` và `pytest` trên máy tính. Hiểu cách chạy kịch bản kiểm thử tự động trực tiếp bằng dòng lệnh trong Terminal của VS Code.
* **Bài học kinh nghiệm:** Cần cẩn thận khi lưu file (`Ctrl + S`) và tạo đúng cấu trúc đường dẫn thư mục `tuan-04/...` để `pytest` có thể tìm thấy bài test.

### Thành viên 2: [Họ và tên sinh viên 2] (Vai trò: Navigator)
* **Điều đã học:** Hiểu được luồng hoạt động của Automation Testing: Selenium đóng vai trò là robot giả lập thao tác người dùng trên trình duyệt Chrome, còn Pytest đóng vai trò kiểm tra tính đúng đắn (`assert`) và tổng hợp báo cáo kết quả.
* **Bài học kinh nghiệm:** Luôn kiểm tra kỹ quy tắc đặt tên hàm (`test_...`) và phân biệt rõ lỗi cú pháp hệ thống (như thiếu `pip`) với lỗi kịch bản test không khớp (`AssertionError`).

---

## 2. Trả lời câu hỏi phần đọc

* **Câu hỏi:** Mục đích chính của việc viết kịch bản kiểm thử tự động (Automation Test) so với kiểm thử thủ công (Manual Test) trong dự án phần mềm là gì?
* **Trả lời:** Kiểm thử tự động giúp tiết kiệm thời gian và công sức khi phải lặp đi lặp lại các bài test nhiều lần (đặc biệt là Regression Testing - kiểm thử hồi quy). Nó giúp phát hiện lỗi nhanh chóng ngay khi có sự thay đổi trong source code mà không cần con người phải ngồi click tay từng chức năng.

---

## 3. Nhật ký sử dụng AI trợ giúp

* **Nội dung đã hỏi AI:**
  1. Cách xử lý lỗi `The system cannot find the path specified` và lỗi thiếu `pip` (`No module named pip`) khi khởi tạo môi trường Python.
  2. Cách viết kịch bản Selenium cơ bản để mở trang `the-internet` và kiểm tra tiêu đề.
  3. Ý nghĩa của các thông báo `collected 0 items` và `1 failed` khi chạy `pytest`.
* **Đánh giá câu trả lời của AI:**
  * Câu trả lời chính xác, giúp phát hiện đúng nguyên nhân máy đang dùng bản Python cắt giảm của MSYS2 nên thiếu `pip`.
  * AI đã đưa ra từng bước khắc phục trực quan theo đúng vai trò Driver & Navigator.
* **Điều hiểu thêm được:** 
  * Hiểu nguyên lý hoạt động của `assert`: so sánh giá trị thực tế lấy từ web (`driver.title`) với giá trị mong đợi.
  * Biết cách đọc thông báo lỗi của Pytest để tìm ra điểm khác biệt giữa dữ liệu thực tế và dữ liệu mong đợi khi bài test bị thất bại.
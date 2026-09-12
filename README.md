# 🛒 Long Chau Pharma Web Scraping Pipeline

Dự án Demo tự động hóa quy trình thu thập và xử lý dữ liệu sản phẩm từ hệ thống **Nhà thuốc Long Châu**.

## 🎯 Mục tiêu dự án
* **Chuyên mục cào dữ liệu:** [Thực phẩm chức năng hỗ trợ thần kinh não](https://nhathuoclongchau.com.vn/thuc-pham-chuc-nang/than-kinh-nao) - Nhà thuốc Long Châu.
* **Công nghệ sử dụng:** Python, Playwright (Cào dữ liệu động & tương tác tự động), Crawl4AI (Lọc sạch nội dung sang Markdown), và Regex (Bóc tách dữ liệu cấu trúc).

---

## 🔄 Quy trình Pipeline & Chi tiết các file

Hệ thống được chia thành 3 bước độc lập tương ứng với 3 file script chính trong thư mục `Demo/`:

### 1️⃣ Bước 1: Thu thập dữ liệu thô (`Step1.py`)
* **Vai trò:** Đóng vai trò là con bot cào động (Scraper).
* **Cách hoạt động:** Sử dụng thư viện **Playwright** để bật trình duyệt, tự động cuộn xuống cuối trang và liên tục nhấn nút *"Xem thêm"* cho đến khi toàn bộ sản phẩm của chuyên mục được tải hết lên giao diện.
* **Đầu ra:** Lưu toàn bộ mã nguồn trang thành file thô **`longchau.html`**.

### 2️⃣ Bước 2: Làm sạch và chuẩn hóa (`Step2.py`)
* **Vai trò:** Đóng vai trò là bộ lọc thông minh (Parser).
* **Cách hoạt động:** Đọc file `longchau.html` cục bộ bằng **Crawl4AI**, tự động loại bỏ các thành phần rác không cần thiết như Header, Footer, Menu, quảng cáo.
* **Đầu ra:** Chuyển đổi và lưu nội dung thành file Markdown tinh gọn **`longchau_clean.md`**.

### 3️⃣ Bước 3: Trích xuất cấu trúc và xuất file (`Step3.py`)
* **Vai trò:** Xử lý dữ liệu và kết xuất (Data Extractor).
* **Cách hoạt động:** Đọc file Markdown sạch, ứng dụng biểu thức chính quy (**Regex**) và thuật toán logic để bóc tách rõ ràng các trường thông tin: *Loại sản phẩm, Tên sản phẩm, Giá bán, Quy cách đóng gói*.
* **Đầu ra:** Xuất dữ liệu hoàn chỉnh ra file bảng tính chuẩn **`longchau_products.csv`** sẵn sàng phục vụ cho việc phân tích.

---

## 📊 Kết quả đầu ra (`Demo/longchau_products.csv`)
Dữ liệu cuối cùng được tổng hợp trực quan dưới dạng bảng `.csv` giúp dễ dàng tra cứu, thống kê hoặc phục vụ cho các ứng dụng phân tích dữ liệu và AI/RAG.

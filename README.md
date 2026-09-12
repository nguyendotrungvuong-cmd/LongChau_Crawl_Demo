# 🛒 Long Chau Pharma Web Scraping Pipeline

Dự án Demo tự động hóa quy trình thu thập và xử lý dữ liệu sản phẩm từ hệ thống **Nhà thuốc Long Châu**.

## 🎯 Mục tiêu dự án
* **Chuyên mục cào dữ liệu:** [Thực phẩm chức năng hỗ trợ thần kinh não](https://nhathuoclongchau.com.vn/thuc-pham-chuc-nang/than-kinh-nao) - Nhà thuốc Long Châu.
* **Công nghệ sử dụng:** Python, Playwright (Cào động & tương tác click "Xem thêm"), Crawl4AI (Lọc sạch nội dung sang Markdown), và Regex (Bóc tách dữ liệu có cấu trúc).

## 🚀 Cấu trúc mã nguồn (`Demo/`)
* `Step1.py`: Bot 1 dùng Playwright để mở trình duyệt, tự động cuộn trang và nhấn nút "Xem thêm" để tải toàn bộ danh sách sản phẩm.
* `Step2.py`: Bot 2 dùng Crawl4AI để phân tích và lọc bỏ các thành phần rác, xuất ra file Markdown tinh gọn.
* `Step3.py`: Bot 3 dùng thuật toán bóc tách dữ liệu để phân loại sản phẩm, giá bán, quy cách đóng gói và xuất ra file chuẩn `longchau_products.csv`.

## 📊 Kết quả đầu ra
Dữ liệu cuối cùng được tổng hợp trực quan dưới dạng bảng tính `.csv` sẵn sàng để phục vụ cho việc thống kê, phân tích hoặc tích hợp vào các hệ thống AI/RAG.

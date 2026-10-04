## Cách sử dụng

### 1. Clone repository

    git clone https://github.com/xiaoxigua0503/xsmb_api_project.git
    cd xsmb_api_project

### 2. Tạo virtual environment (Linux)

    python3 -m venv venv
    source venv/bin/activate

### 3. Cài đặt dependencies

    pip install -r requirements.txt

### 4. Cấu hình API Key

Thêm API Key của XosoAPI vào file cấu hình của project.

### 5. Chạy chương trình

    python main.py

Có thể chỉ định số lượng trang và số bản ghi mỗi trang:

    python main.py --pages 10 --limit 20

### 6. Kết quả

Sau khi chạy, chương trình sẽ lấy dữ liệu XSMB từ API, lọc dữ liệu Miền Bắc, lấy kết quả của 7 ngày gần nhất và xuất ra file CSV.
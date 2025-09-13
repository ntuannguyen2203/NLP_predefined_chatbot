# ☕ CoffeeShop Chatbot (FastAPI + Keyword Cases)

Chatbot mẫu viết bằng **FastAPI** với logic trả lời dựa trên **keyword/case**.  
Dự án này demo cho một quán cà phê nhỏ, nhưng có thể mở rộng cho nhiều lĩnh vực khác.

---

## 🚀 Tính năng
- Giao diện web chat đơn giản (HTML + CSS + JS).
- Trả lời dựa trên **keyword** (`equals`, `contains`, `regex`, `default`).
- 10 case CoffeeShop có sẵn:
  1. Chào hỏi khách
  2. Xem menu
  3. Hỏi giờ mở cửa
  4. Xem địa chỉ
  5. Xin mật khẩu Wi-Fi
  6. Đặt bàn
  7. Order đồ uống
  8. Xem khuyến mãi
  9. Feedback / đánh giá
  10. Thanh toán

---

## 📂 Cấu trúc project
```
chatbot-fastapi/
├─ main.py              # Backend FastAPI (API + logic chatbot)
├─ templates/
│  └─ index.html        # Giao diện web chat
├─ static/
│  └─ style.css         # CSS cho giao diện
├─ requirements.txt     # Thư viện cần cài
└─ README.md            # Tài liệu hướng dẫn
```

---

## 🔧 Cài đặt

1. Clone project và tạo virtual environment:
   ```bash
   git clone https://github.com/ntuannguyen2203/NLP_predefined_chatbot.git
   cd chatbot-fastapi
   python -m venv .venv
   ```

2. Kích hoạt môi trường:
   - **Linux/macOS**:
     ```bash
     source .venv/bin/activate
     ```
   - **Windows**:
     ```bash
     .venv\Scripts\activate
     ```

3. Cài dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Chạy server FastAPI:
   ```bash
   uvicorn main:app --reload --port 8000
   ```

5. Mở trình duyệt tại:
   ```
   http://127.0.0.1:8000/
   ```

---

## 💬 Hướng dẫn chat

### 1. Chào hỏi
```
chào
hello
hi
```
👉 Bot: *"Chào mừng bạn đến với CoffeeShop! ☕ Bạn muốn uống gì hôm nay?"*

### 2. Xem menu
```
menu
thực đơn
```
👉 Bot trả về danh sách đồ uống và giá.

### 3. Giờ mở cửa
```
giờ mở cửa
open time
mấy giờ mở
```
👉 Bot: *"Quán mở từ 7:00 sáng đến 10:00 tối mỗi ngày."*

### 4. Địa chỉ
```
địa chỉ
ở đâu
location
```
👉 Bot: *"CoffeeShop ở số 123 Nguyễn Văn A, Quận 1, TP.HCM."*

### 5. Wi-Fi
```
wifi
mật khẩu wifi
wifi password
```
👉 Bot gửi SSID + password.

### 6. Đặt bàn
```
đặt bàn
reservation
booking
```
👉 Bot hỏi số người & thời gian.

### 7. Order đồ uống
```
mua latte
order espresso
cho mình 1 trà sữa
```
👉 Bot xác nhận order.

### 8. Khuyến mãi
```
khuyến mãi
giảm giá
ưu đãi
promotion
```
👉 Bot báo ưu đãi hôm nay.

### 9. Feedback
```
góp ý
feedback
phàn nàn
đánh giá
```
👉 Bot cảm ơn & ghi nhận góp ý.

### 10. Thanh toán
```
thanh toán
payment
trả tiền
```
👉 Bot: *"Quán nhận tiền mặt, thẻ và ví điện tử (Momo, ZaloPay)."*

---

## 🛠️ Mở rộng
- Thêm case mới vào biến `CASES` trong `main.py`.
- Tách `CASES` ra file JSON/YAML để dễ cấu hình.
- Dùng **WebSocket** để chat realtime thay vì API POST.
- Tích hợp **NLP/AI model** (spaCy, transformers) để tăng độ hiểu ngữ nghĩa.
- Thêm **database** để lưu order, lịch đặt bàn.

---

## 📸 Demo giao diện
Giao diện mặc định có khung chat, khung nhập tin nhắn, và nút gửi.  
Bạn có thể tùy chỉnh CSS trong `static/style.css` để đổi màu, font, hoặc thêm dark mode.

---

## 📜 License
MIT License.

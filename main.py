from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import re
from typing import List, Dict, Any

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# ----- Cấu hình các case / keyword / response -----
# Mỗi case gồm: type (equals|contains|startswith|regex), keywords (list), response (str or func)
CASES = [
    # 1. Chào hỏi khách
    {
        "type": "contains",
        "keywords": ["xin chào", "chào", "hello", "hi"],
        "response": "Chào mừng bạn đến với CoffeeShop! ☕ Bạn muốn uống gì hôm nay?"
    },
    # 2. Hỏi menu
    {
        "type": "contains",
        "keywords": ["menu", "thực đơn"],
        "response": "Menu hôm nay: Espresso (40k), Latte (45k), Cappuccino (50k), Cold Brew (55k), Trà sữa (35k)."
    },
    # 3. Giờ mở cửa
    {
        "type": "contains",
        "keywords": ["giờ mở cửa", "open time", "mấy giờ mở"],
        "response": "Quán mở từ 7:00 sáng đến 10:00 tối mỗi ngày."
    },
    # 4. Địa chỉ
    {
        "type": "contains",
        "keywords": ["địa chỉ", "ở đâu", "location"],
        "response": "CoffeeShop ở số 123 Nguyễn Văn A, Quận 1, TP.HCM."
    },
    # 5. Wifi
    {
        "type": "contains",
        "keywords": ["wifi", "mật khẩu wifi", "wifi password"],
        "response": "Wi-Fi: CoffeeLovers — Password: 12345678"
    },
    # 6. Đặt bàn
    {
        "type": "contains",
        "keywords": ["đặt bàn", "reservation", "booking"],
        "response": "Bạn muốn đặt bàn cho mấy người và lúc mấy giờ?"
    },
    # 7. Order cà phê
    {
        "type": "contains",
        "keywords": ["mua", "order", "gọi", "cho mình"],
        "response": "Bạn muốn order loại đồ uống nào? (ví dụ: Latte, Espresso, Trà sữa)"
    },
    # 8. Giảm giá / khuyến mãi
    {
        "type": "contains",
        "keywords": ["khuyến mãi", "giảm giá", "promotion", "ưu đãi"],
        "response": "Hôm nay có ưu đãi: Mua 2 Latte tặng 1 bánh ngọt 🎉"
    },
    # 9. Feedback
    {
        "type": "contains",
        "keywords": ["góp ý", "feedback", "phàn nàn", "đánh giá"],
        "response": "Cảm ơn bạn đã góp ý! Bạn vui lòng để lại đánh giá chi tiết, chúng tôi sẽ ghi nhận."
    },
    # 10. Thanh toán
    {
        "type": "contains",
        "keywords": ["thanh toán", "payment", "trả tiền"],
        "response": "Quán nhận tiền mặt, thẻ và ví điện tử (Momo, ZaloPay)."
    },

    # fallback
    {
        "type": "default",
        "response": "Xin lỗi, mình chưa hiểu. Bạn có thể thử hỏi: 'menu', 'giờ mở cửa', 'wifi', 'đặt bàn'."
    }
]


# ----- Hàm xử lý keyword matching -----
def match_cases(msg: str) -> str:
    msg_lower = msg.lower().strip()
    for case in CASES:
        ctype = case.get("type", "contains")
        if ctype == "default":
            # xử lý ở cuối nếu ko khớp case nào
            continue
        if ctype == "equals":
            for kw in case.get("keywords", []):
                if msg_lower == kw.lower():
                    resp = case["response"]
                    return resp(msg_lower) if callable(resp) else resp
        elif ctype == "contains":
            for kw in case.get("keywords", []):
                if kw.lower() in msg_lower:
                    resp = case["response"]
                    return resp(msg_lower) if callable(resp) else resp
        elif ctype == "startswith":
            for kw in case.get("keywords", []):
                if msg_lower.startswith(kw.lower()):
                    resp = case["response"]
                    return resp(msg_lower) if callable(resp) else resp
        elif ctype == "regex":
            for pat in case.get("keywords", []):
                m = re.search(pat, msg_lower)
                if m:
                    resp = case["response"]
                    return resp(m) if callable(resp) else resp
        else:
            # unknown type -> skip
            continue

    # nếu không khớp case nào, trả default
    for case in CASES:
        if case.get("type") == "default":
            resp = case["response"]
            return resp if not callable(resp) else resp(msg_lower)
    return "Mình chưa có câu trả lời cho câu đó."

# ----- Routes -----
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat_endpoint(payload: Dict[str, Any]):
    # payload expected: {"message": "..." }
    message = str(payload.get("message", "")).strip()
    if not message:
        return JSONResponse({"error": "empty message"}, status_code=400)
    answer = match_cases(message)
    return {"reply": answer, "original": message}

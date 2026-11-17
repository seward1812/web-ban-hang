# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

# Sử dụng đường dẫn import có tiền tố backend để Python nhận diện chính xác gói module
from backend.services.shipping import create_shipping_order
from backend.services.wms_erp import sync_to_wms_and_erp

app = FastAPI(title="Shopee Clone Enterprise API", version="1.0")

# Bật CORS để Frontend gọi API không bị chặn
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Struct dữ liệu đơn hàng nhận từ Frontend
class CartItem(BaseModel):
    id: int
    name: str
    price: int
    quantity: int

class CheckoutRequest(BaseModel):
    customer_name: str
    phone: str
    address: str
    items: List[CartItem]
    total_amount: int

@app.get("/")
def read_root():
    return {"status": "Online", "system": "Shopee Clone Enterprise Backend"}

@app.post("/api/checkout")
def checkout(order: CheckoutRequest):
    order_id = 1001  # Giả lập ID đơn tăng tự động
    
    # 1. Gọi Shipping API
    ship_info = create_shipping_order(order_id, order.address, order.customer_name)
    
    # 2. Đồng bộ Kho WMS & Kế toán ERP
    erp_info = sync_to_wms_and_erp({
        "order_id": order_id,
        "total_amount": order.total_amount + ship_info["shipping_fee"]
    })
    
    return {
        "success": True,
        "message": "Đặt hàng thành công!",
        "data": {
            "order_id": order_id,
            "grand_total": order.total_amount + ship_info["shipping_fee"],
            "shipping": ship_info,
            "erp_wms": erp_info
        }
    }
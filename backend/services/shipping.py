# backend/services/shipping.py

def calculate_shipping_fee(address: str) -> int:
    """Tính phí vận chuyển tự động dựa trên địa chỉ"""
    if "Hà Nội" in address or "TP.HCM" in address or "Hồ Chí Minh" in address:
        return 22000
    return 35000

def create_shipping_order(order_id: int, address: str, customer_name: str):
    """Gửi yêu cầu tạo vận đơn sang GHN / GHTK API"""
    fee = calculate_shipping_fee(address)
    return {
        "shipping_unit": "Giao Hàng Nhanh (GHN)",
        "tracking_code": f"GHN{order_id}VN",
        "shipping_fee": fee,
        "status": "Ready_To_Pick"
    }
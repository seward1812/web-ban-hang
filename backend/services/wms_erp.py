# backend/services/wms_erp.py

def sync_to_wms_and_erp(order_data: dict):
    """Trừ tồn kho WMS và xuất hóa đơn ERP"""
    print(f"[WMS]: Trừ tồn kho cho đơn hàng {order_data['order_id']}")
    print(f"[ERP]: Ghi nhận doanh thu {order_data['total_amount']}đ vào sổ sách")
    return {
        "wms_status": "Stock_Deducted",
        "erp_invoice": f"INV-2026-{order_data['order_id']}"
    }
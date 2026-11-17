// Quản lý trạng thái giỏ hàng
let cart = [];

/**
 * Thêm sản phẩm vào giỏ hàng
 * @param {number} id - ID sản phẩm
 * @param {string} name - Tên sản phẩm
 * @param {number} price - Giá tiền sản phẩm
 */
function addToCart(id, name, price) {
    const existing = cart.find(item => item.id === id);
    if (existing) {
        existing.quantity += 1;
    } else {
        cart.push({ id, name, price, quantity: 1 });
    }
    updateCartCount();
    alert(`Đã thêm "${name}" vào Giỏ hàng!`);
}

/**
 * Cập nhật số lượng sản phẩm trên Icon Giỏ hàng (Header)
 */
function updateCartCount() {
    const total = cart.reduce((sum, item) => sum + item.quantity, 0);
    const cartCountElement = document.getElementById('cartCount');
    if (cartCountElement) {
        cartCountElement.textContent = total;
    }
}

/**
 * Hiển thị chi tiết giỏ hàng và đặt hàng
 */
function toggleCart() {
    if (cart.length === 0) {
        alert("Giỏ hàng của bạn đang trống!");
        return;
    }

    let msg = "=== GIỎ HÀNG SHOPEE ===\n\n";
    let total = 0;
    
    cart.forEach((item, index) => {
        const itemTotal = item.price * item.quantity;
        total += itemTotal;
        msg += `${index + 1}. ${item.name} x${item.quantity} = ₫${itemTotal.toLocaleString('vi-VN')}\n`;
    });
    
    msg += `\nTổng thanh toán: ₫${total.toLocaleString('vi-VN')}`;
    
    if (confirm(msg + "\n\nBấm OK để gửi đơn hàng tới Python API (ERP/WMS/Shipping API)")) {
        checkoutOrder(total);
    }
}

/**
 * Xử lý đặt hàng (Chuẩn bị dữ liệu để kết nối Backend Python)
 */
function checkoutOrder(totalAmount) {
    const orderPayload = {
        customer_id: "GUEST_123",
        items: cart,
        total_amount: totalAmount,
        created_at: new Date().toISOString()
    };
    
    console.log("Đang gửi đơn hàng tới Python FastAPI:", orderPayload);
    alert("Đã gửi đơn hàng thành công! Đang xử lý giao hàng tự động qua GHN/GHTK.");
    
    cart = [];
    updateCartCount();
}

/**
 * Xử lý tìm kiếm sản phẩm trên thanh Header
 */
function handleSearch() {
    const queryInput = document.getElementById('searchInput');
    const query = queryInput ? queryInput.value.trim() : '';
    if (query) {
        alert(`Tìm kiếm Shopee: "${query}"`);
    } else {
        alert("Vui lòng nhập từ khóa tìm kiếm!");
    }
}

// Khởi tạo khi DOM sẵn sàng
document.addEventListener('DOMContentLoaded', () => {
    console.log("Shopee Clone JS đã tải hoàn tất!");
});
import pytest
from shopping_cart import ShoppingCart, InvalidQuantityError, OutOfStockError


@pytest.fixture
def empty_cart():
    """Tạo giỏ hàng của user thường không có sản phẩm."""
    return ShoppingCart(user_id="user_normal_01", is_vip=False)

@pytest.fixture
def vip_cart():
    """Tạo giỏ hàng của khách VIP."""
    return ShoppingCart(user_id="user_vip_01", is_vip=True)

@pytest.fixture
def cart_with_items(empty_cart):
    """Giỏ hàng mẫu đã có sẵn một vài sản phẩm."""
    empty_cart.add_item("Bàn phím cơ", 500_000, 1)
    empty_cart.add_item("Chuột không dây", 250_000, 2)
    return empty_cart



def test_add_new_item_successfully(empty_cart):
    empty_cart.add_item("Tai nghe", 300_000, 1)
    assert "Tai nghe" in empty_cart.items
    assert empty_cart.items["Tai nghe"]["qty"] == 1
    assert empty_cart.get_subtotal() == 300_000

def test_add_existing_item_accumulates_quantity(cart_with_items):
    cart_with_items.add_item("Bàn phím cơ", 500_000, 2)
    assert cart_with_items.items["Bàn phím cơ"]["qty"] == 3

def test_remove_partial_quantity(cart_with_items):
    cart_with_items.remove_item("Chuột không dây", 1)
    assert cart_with_items.items["Chuột không dây"]["qty"] == 1

def test_remove_all_or_excess_quantity_deletes_item(cart_with_items):
    cart_with_items.remove_item("Chuột không dây", 5)
    assert "Chuột không dây" not in cart_with_items.items



def test_add_item_invalid_quantity_raises_error(empty_cart):
    with pytest.raises(InvalidQuantityError, match="Số lượng phải lớn hơn 0"):
        empty_cart.add_item("Màn hình", 2_000_000, qty=-1)

def test_add_item_negative_price_raises_error(empty_cart):
    with pytest.raises(ValueError, match="Giá tiền không hợp lệ"):
        empty_cart.add_item("Lót chuột", -10_000, qty=1)

def test_remove_nonexistent_item_raises_error(empty_cart):
    with pytest.raises(KeyError):
        empty_cart.remove_item("Sản phẩm ma", 1)


@pytest.mark.parametrize(
    "subtotal_amount, is_vip, expected_discount_percent",
    [
        (500_000, False, 0.0),
        (1_000_000, False, 0.10),
        (500_000, True, 0.05), 
        (1_200_000, True, 0.15),
    ]
)
def test_discount_tiers(subtotal_amount, is_vip, expected_discount_percent):
    cart = ShoppingCart(user_id="user_test", is_vip=is_vip)
    cart.add_item("Sản phẩm tùy biến", subtotal_amount, 1)
    
    assert cart.calculate_discount() == expected_discount_percent
    assert cart.get_total_price() == subtotal_amount * (1 - expected_discount_percent)
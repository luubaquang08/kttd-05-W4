class OutOfStockError(Exception):
    pass


class InvalidQuantityError(Exception):
    pass


class ShoppingCart:
    def __init__(self, user_id: str, is_vip: bool = False):
        self.user_id = user_id
        self.is_vip = is_vip
        self.items = {}

    def add_item(self, item_name: str, price: float, qty: int = 1):
        if qty <= 0:
            raise InvalidQuantityError("Số lượng phải lớn hơn 0")
        if price < 0:
            raise ValueError("Giá tiền không hợp lệ")

        if item_name in self.items:
            self.items[item_name]["qty"] += qty
        else:
            self.items[item_name] = {"price": price, "qty": qty}

    def remove_item(self, item_name: str, qty: int = 1):
        if item_name not in self.items:
            raise KeyError(f"Sản phẩm {item_name} không có trong giỏ hàng")
        if qty <= 0:
            raise InvalidQuantityError("Số lượng cần xóa phải lớn hơn 0")

        if qty >= self.items[item_name]["qty"]:
            del self.items[item_name]
        else:
            self.items[item_name]["qty"] -= qty

    def get_subtotal(self) -> float:
        return sum(data["price"] * data["qty"] for data in self.items.values())

    def calculate_discount(self) -> float:
        subtotal = self.get_subtotal()
        discount = 0.0
        if subtotal >= 1_000_000:
            discount += 0.10
        if self.is_vip:
            discount += 0.05

        return min(discount, 0.20)

    def get_total_price(self) -> float:
        subtotal = self.get_subtotal()
        discount = self.calculate_discount()
        return subtotal * (1 - discount)
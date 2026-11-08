import magazine.utils as utils


class Order:
    def __init__(self, order_id: int, price: float, quantity: int) -> None:
        self.order_id = order_id
        self.price = price
        self.quantity = quantity

    def total(self) -> float:
        return self.price * self.quantity

    def __str__(self) -> str:
        return (f"Zamówienie {self.order_id}: {self.quantity} szt. x "
                f"{utils.format_price(self.price)} = "
                f"{utils.format_price(self.total())}")


if __name__ == "__main__":
    order = Order(order_id=1, price=19.9, quantity=2)
    print(order)

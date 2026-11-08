import magazine.utils as utils


class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"{self.name} - {utils.format_price(self.price)}"


if __name__ == "__main__":
    print(Product("Kawa", 19.9))

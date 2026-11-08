from oop.property import Property


class Flat(Property):
    def __init__(
        self, area: float, rooms: int, price: float, address: str, floor: int
    ) -> None:
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self) -> str:
        return (
            f"Flat: {self.address}, {self.area} m2, "
            f"{self.rooms} rooms, floor: {self.floor}, price: {self.price} PLN"
        )

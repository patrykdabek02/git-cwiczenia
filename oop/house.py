from oop.property import Property


class House(Property):
    def __init__(
        self, area: float, rooms: int, price: float, address: str, plot: int
    ) -> None:
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self) -> str:
        return (
            f"House: {self.address}, {self.area} m2, "
            f"{self.rooms} rooms, plot: {self.plot} m2, "
            f"price: {self.price} PLN"
        )

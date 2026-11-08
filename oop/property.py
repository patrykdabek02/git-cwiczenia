class Property:
    def __init__(
        self, area: float, rooms: int, price: float, address: str
    ) -> None:
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self) -> str:
        return (
            f"Property: {self.address}, {self.area} m2, "
            f"{self.rooms} rooms, price: {self.price} PLN"
        )

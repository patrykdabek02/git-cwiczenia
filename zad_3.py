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


house1 = House(120, 5, 500000, "ulica", 300)
flat1 = Flat(60, 3, 300000, "ulica", 2)


print(house1)
print(flat1)

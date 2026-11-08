from oop.book import Book
from oop.employee import Employee
from oop.student import Student


class Order:
    def __init__(
        self,
        employee: Employee,
        student: Student,
        books: list[Book],
        order_date: str,
    ) -> None:
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self) -> str:
        books = "\n".join(f"  - {book}" for book in self.books)
        return (
            f"Zamówienie z {self.order_date}\n"
            f"Pracownik: {self.employee}\n"
            f"Student: {self.student}\n"
            f"Książki:\n{books}"
        )

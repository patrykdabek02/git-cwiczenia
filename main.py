from oop.book import Book
from oop.employee import Employee
from oop.flat import Flat
from oop.house import House
from oop.library import Library
from oop.order import Order
from oop.student import Student


def run_students() -> None:
    print("=== zad_1: Student ===")
    anna = Student("Anna", [60, 70, 80])
    tom = Student("Tom", [40, 50, 60])
    print(anna.is_passed())
    print(tom.is_passed())


def run_library() -> None:
    print("=== zad_2: Biblioteka ===")
    warsaw_library = Library(
        "Warsaw", "Main Street", "00-001", "9:00-17:00", "111111111"
    )
    cracow_library = Library(
        "Cracow", "Second Street", "30-002", "10:00-18:00", "222222222"
    )

    book1 = Book(warsaw_library, "2020-01-01", "Author", "A", 200)
    book2 = Book(cracow_library, "2021-02-02", "Author", "B", 300)
    book3 = Book(warsaw_library, "2022-03-03", "Author", "C", 400)
    book4 = Book(cracow_library, "2023-04-04", "Author", "D", 500)

    employee1 = Employee(
        "John", "Doe", "2020-01-01", "1990-01-01",
        "Warsaw", "Main Street", "00-001", "123456789",
    )
    employee2 = Employee(
        "Jane", "Smith", "2021-02-02", "1991-02-02",
        "Cracow", "Second Street", "30-002", "987654321",
    )

    student1 = Student("Anna", [60, 70, 80])
    student2 = Student("Tom", [40, 50, 60])

    order1 = Order(employee1, student1, [book1, book2], "2024-06-01")
    order2 = Order(employee2, student2, [book3, book4], "2024-06-02")

    print(order1)
    print()
    print(order2)


def run_properties() -> None:
    print("=== zad_3: Nieruchomości ===")
    house1 = House(120, 5, 500000, "ulica", 300)
    flat1 = Flat(60, 3, 300000, "ulica", 2)
    print(house1)
    print(flat1)


if __name__ == "__main__":
    run_students()
    print()
    run_library()
    print()
    run_properties()

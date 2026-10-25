class Library:
    def __init__(self, city: str, street: str, zip_code: str,
                 open_hours: str, phone: str) -> None:
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self) -> str:
        return (f"Biblioteka: {self.street}, {self.zip_code} {self.city}, "
                f"godz. {self.open_hours}, tel. {self.phone}")


class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date: str,
                 birth_date: str, city: str, street: str, zip_code: str,
                 phone: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self) -> str:
        return (f"{self.first_name} {self.last_name} "
                f"(zatrudniony od {self.hire_date}, tel. {self.phone})")


class Student:
    def __init__(self, name: str, marks: list[int]) -> None:
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        return sum(self.marks) / len(self.marks) > 50

    def __str__(self) -> str:
        return f"{self.name} (oceny: {self.marks})"


class Book:
    def __init__(self, library: Library, publication_date: str,
                 author_name: str, author_surname: str,
                 number_of_pages: int) -> None:
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self) -> str:
        return (f"{self.author_name} {self.author_surname}, "
                f"{self.number_of_pages} str., wyd. {self.publication_date} | "
                f"{self.library}")


class Order:
    def __init__(self, employee: Employee, student: Student,
                 books: list[Book], order_date: str) -> None:
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self) -> str:
        books = "\n".join(f"  - {book}" for book in self.books)
        return (f"Zamówienie z {self.order_date}\n"
                f"Pracownik: {self.employee}\n"
                f"Student: {self.student}\n"
                f"Książki:\n{books}")


warsaw_library = Library("Warsaw", "Main Street", "00-001", "9:00-17:00", "111111111")
cracow_library = Library("Cracow", "Second Street", "30-002", "10:00-18:00", "222222222")

book1 = Book(warsaw_library, "2020-01-01", "Author", "A", 200)
book2 = Book(cracow_library, "2021-02-02", "Author", "B", 300)
book3 = Book(warsaw_library, "2022-03-03", "Author", "C", 400)
book4 = Book(cracow_library, "2023-04-04", "Author", "D", 500)
book5 = Book(warsaw_library, "2024-05-05", "Author", "E", 600)

employee1 = Employee("John", "Doe", "2020-01-01", "1990-01-01", "Warsaw", "Main Street", "00-001", "123456789")
employee2 = Employee("Jane", "Smith", "2021-02-02", "1991-02-02", "Cracow", "Second Street", "30-002", "987654321")
employee3 = Employee("Alice", "Johnson", "2022-03-03", "1992-03-03", "Warsaw", "Main Street", "00-001", "456789123")

student1 = Student("Anna", [60, 70, 80])
student2 = Student("Tom", [40, 50, 60])
student3 = Student("Mike", [90, 80, 70])

order1 = Order(employee1, student1, [book1, book2], "2024-06-01")
order2 = Order(employee2, student2, [book3, book4], "2024-06-02")

print(order1)
print()
print(order2)
#pol english pol polsih pierdolish

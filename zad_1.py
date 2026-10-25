class Student:
    def __init__(self, name: str, marks: list[int]) -> None:
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        return sum(self.marks) / len(self.marks) > 50


anna = Student("Anna", [60, 70, 80])
tom = Student("Tom", [40, 50, 60])
print(anna.is_passed())
print(tom.is_passed())

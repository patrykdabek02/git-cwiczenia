class Student:
    def __init__(self, name: str, marks: list[int]) -> None:
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        return sum(self.marks) / len(self.marks) > 50

    def __str__(self) -> str:
        return f"{self.name} (oceny: {self.marks})"

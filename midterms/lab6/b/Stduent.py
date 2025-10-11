class Student:
    def __init__(self, id_number: int, name: str, course: str):
        self.id_number = id_number
        self.name = name
        self.course = course

    def __str__(self) -> str:
        return f"{self.id_number} - {self.name} - {self.course}"

    def validate_info(self) -> None:
        if not self.name.replace(" ", "").isalpha():
            print("Student information is not valid.")
            return
        if len(str(self.id_number)) != 9:
            print("Student information is not valid.")
            return
        print("Student information is valid.")

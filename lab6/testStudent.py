from Stduent import Student

def main():
    print("Action: Invoking __str__() method with the following Student information:")
    s1 = Student(123456789, "John Doe", "Computer Science")
    print(f"ID: {s1.id_number}")
    print(f"Name: {s1.name}")
    print(f"Course: {s1.course}")
    print("\nOutput:")
    print(s1)
    print()

    print("Action: Invoking __str__() method with the following Student information:")
    s2 = Student(12345, "Jane Doe", "Mathematics")
    print(f"ID: {s2.id_number}")
    print(f"Name: {s2.name}")
    print(f"Course: {s2.course}")
    print("\nOutput:")
    print(s2)
    print()

    print("Action: Invoking validate_info() method with the following Student information:")
    s3 = Student(987654321, "Alice123", "Physics")
    print(f"ID: {s3.id_number}")
    print(f"Name: {s3.name}")
    print(f"Course: {s3.course}")
    print("\nOutput:")
    s3.validate_info()

if __name__ == "__main__":
    main()

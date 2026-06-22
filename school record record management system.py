# school_record_system.py

class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


class SchoolRecordSystem:
    def __init__(self):
        self.records = {}

    def add_student(self, student):
        if student.student_id in self.records:
            print("Student ID already exists!")
        else:
            self.records[student.student_id] = student
            print("Student added successfully.")

    def view_students(self):
        if not self.records:
            print("No student records found.")
        else:
            for student in self.records.values():
                print(student)

    def update_student(self, student_id, name=None, age=None, grade=None):
        if student_id in self.records:
            student = self.records[student_id]
            if name:
                student.name = name
            if age:
                student.age = age
            if grade:
                student.grade = grade
            print("Student record updated successfully.")
        else:
            print("Student not found.")

    def delete_student(self, student_id):
        if student_id in self.records:
            del self.records[student_id]
            print("Student record deleted successfully.")
        else:
            print("Student not found.")


def main():
    system = SchoolRecordSystem()

    while True:
        print("\n--- School Record System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            grade = input("Enter Grade: ")
            student = Student(student_id, name, age, grade)
            system.add_student(student)

        elif choice == "2":
            system.view_students()

        elif choice == "3":
            student_id = input("Enter Student ID to update: ")
            name = input("Enter new Name (leave blank to skip): ")
            age = input("Enter new Age (leave blank to skip): ")
            grade = input("Enter new Grade (leave blank to skip): ")
            system.update_student(student_id, name or None, age or None, grade or None)

        elif choice == "4":
            student_id = input("Enter Student ID to delete: ")
            system.delete_student(student_id)

        elif choice == "5":
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

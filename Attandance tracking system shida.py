import csv
import datetime

# File to store attendance
ATTENDANCE_FILE = "attendance.csv"

# Initialize CSV file if not exists
def initialize_file():
    try:
        with open(ATTENDANCE_FILE, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Date", "Status"])
    except FileExistsError:
        pass

# Mark attendance
def mark_attendance(name, status="Present"):
    date = datetime.date.today().strftime("%Y-%m-%d")
    with open(ATTENDANCE_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, date, status])
    print(f"Attendance marked for {name} on {date} as {status}")

# View attendance records
def view_attendance():
    with open(ATTENDANCE_FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Menu-driven system
def main():
    initialize_file()
    while True:
        print("\n--- Attendance Tracking System ---")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            status = input("Enter status (Present/Absent): ").capitalize()
            mark_attendance(name, status)
        elif choice == "2":
            view_attendance()
        elif choice == "3":
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

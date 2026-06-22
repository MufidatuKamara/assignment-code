import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

student_records = []

def calculate_grade(test_score, exam_score):
    """
    Function 1: Processes scores and applies decision structures.
    Calculates final mark based on weight: 40% Continuous Assessment, 60% Exam.
    """
    final_mark = (test_score * 0.4) + (exam_score * 0.6)

    # Decision structures for West African / Sierra Leone grading standards
    if final_mark >= 70:
        grade = "A (Excellent)"
        status = "Pass"
    elif final_mark >= 60:
        grade = "B (Very Good)"
        status = "Pass"
    elif final_mark >= 50:
        grade = "C (Good)"
        status = "Pass"
    elif final_mark >= 40:
        grade = "D (Credit)"
        status = "Pass"
    else:
        grade = "F (Fail)"
        status = "Fail"

    return round(final_mark, 2), grade, status


def add_student():
    """
    Function 2: Handles Input Module, validates data, and updates UI.
    """
    # Retrieve inputs
    name = entry_name.get().strip()
    student_id = entry_id.get().strip()
    test_raw = entry_test.get().strip()
    exam_raw = entry_exam.get().strip()

    # Advanced Quality Input Validation
    if not name or not student_id or not test_raw or not exam_raw:
        messagebox.showerror("Input Error", "All fields are mandatory!")
        return

    try:
        test_score = float(test_raw)
        exam_score = float(exam_raw)

        if not (0 <= test_score <= 100) or not (0 <= exam_score <= 100):
            messagebox.showerror("Range Error", "Scores must be between 0 and 100.")
            return
    except ValueError:
        messagebox.showerror("Data Type Error", "Scores must be numeric values.")
        return

    # Process inputs using Function 1
    final_mark, grade, status = calculate_grade(test_score, exam_score)

    # Append structured record to global list
    record = {
        "id": student_id,
        "name": name,
        "final_mark": final_mark,
        "grade": grade,
        "status": status
    }
    student_records.append(record)

    # Output single record results dynamically to visual table (Treeview)
    table.insert("", "end", values=(student_id, name, final_mark, grade, status))

    # Trigger system analytics updating routine
    update_class_analytics()

    # Clear fields for next data handling entry
    clear_input_fields()


def update_class_analytics():
    """
    Function 3: Processing & Output Module for collective statistics using iteration (loops).
    """
    if not student_records:
        lbl_avg_val.config(text="0.00%")
        lbl_highest_val.config(text="0.00")
        return

    total_marks = 0
    highest_mark = 0

    # Iteration through records to perform logical calculations
    for student in student_records:
        current_mark = student["final_mark"]
        total_marks += current_mark
        if current_mark > highest_mark:
            highest_mark = current_mark

    class_average = total_marks / len(student_records)

    # Display formatted output to user-friendly components
    lbl_avg_val.config(text=f"{round(class_average, 2)}%")
    lbl_highest_val.config(text=f"{round(highest_mark, 2)}%")


def clear_input_fields():
    """
    Helper Function: Clears entry boxes safely.
    """
    entry_name.delete(0, tk.END)
    entry_id.delete(0, tk.END)
    entry_test.delete(0, tk.END)
    entry_exam.delete(0, tk.END)


def reset_system():
    """
    Helper Function: Wipes out active cache and visual items.
    """
    global student_records
    student_records = []
    for item in table.get_children():
        table.delete(item)
    update_class_analytics()
    clear_input_fields()


# ==========================================
# GUI ARCHITECTURE MODULE
# ==========================================
root = tk.Tk()
root.title("Sierra Leone Student Academic Portal (SDG 4)")
root.geometry("750x600")
root.configure(bg="#f4f6f9")

# Header Section
header_frame = tk.Frame(root, bg="#1a365d", padx=10)
header_frame.pack(fill="x")
lbl_title = tk.Label(header_frame, text="SIERRA LEONE ACADEMIC PORTAL", font=("Tahoma", 14, "bold"), fg="white",
                     bg="#1a365d")
lbl_title.pack()
lbl_subtitle = tk.Label(header_frame, text="Modular GUI Solutions • Aligned with SDG 4", font=("Tahoma", 9, "italic"),
                        fg="#cbd5e1", bg="#1a365d")
lbl_subtitle.pack()

# Input Module Panel
input_frame = tk.LabelFrame(root, text=" Student Data Entry Module ", font=("Tahoma", 10, "bold"), bg="#f4f6f9",
                            padx=15, pady=10)
input_frame.pack(fill="x", padx=15, pady=10)

tk.Label(input_frame, text="Student Name:", font=("Tahoma", 10), bg="#f4f6f9").grid(row=0, column=0, sticky="w", pady=5)
entry_name = tk.Entry(input_frame, font=("Tahoma", 10))
entry_name.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

tk.Label(input_frame, text="Student ID Number:", font=("Tahoma", 10), bg="#f4f6f9").grid(row=0, column=2, sticky="w",
                                                                                         pady=5)
entry_id = tk.Entry(input_frame, font=("Tahoma", 10))
entry_id.grid(row=0, column=3, padx=10, pady=5, sticky="ew")

tk.Label(input_frame, text="Continuous Assessment (Max 100):", font=("Tahoma", 10), bg="#f4f6f9").grid(row=1, column=0,
                                                                                                       sticky="w",
                                                                                                       pady=5)
entry_test = tk.Entry(input_frame, font=("Tahoma", 10))
entry_test.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

tk.Label(input_frame, text="Final Examination (Max 100):", font=("Tahoma", 10), bg="#f4f6f9").grid(row=1, column=2,
                                                                                                   sticky="w", pady=5)
entry_exam = tk.Entry(input_frame, font=("Tahoma", 10))
entry_exam.grid(row=1, column=3, padx=10, pady=5, sticky="ew")

# Interactive Control Buttons Panel
btn_frame = tk.Frame(root, bg="#f4f6f9")
btn_frame.pack(fill="x", padx=15, pady=5)

btn_add = tk.Button(btn_frame, text="Process & Add Record", command=add_student, bg="#2b6cb0", fg="white",
                    font=("Tahoma", 9, "bold"), padx=10)
btn_add.pack(side="left", padx=5)

btn_clear = tk.Button(btn_frame, text="Clear Entries", command=clear_input_fields, bg="#718096", fg="white",
                      font=("Tahoma", 9), padx=10)
btn_clear.pack(side="left", padx=5)

btn_reset = tk.Button(btn_frame, text="Reset System", command=reset_system, bg="#e53e3e", fg="white",
                      font=("Tahoma", 9), padx=10)
btn_reset.pack(side="left", padx=5)

btn_exit = tk.Button(btn_frame, text="Exit", command=root.quit, bg="#2d3748", fg="white", font=("Tahoma", 9), padx=10)
btn_exit.pack(side="right", padx=5)

# Output Module View (Table Layout)
output_frame = tk.LabelFrame(root, text=" Registered Database Records ", font=("Tahoma", 10, "bold"), bg="#f4f6f9",
                             padx=10, pady=10)
output_frame.pack(fill="both", expand=True, padx=15, pady=10)

columns = ("id", "name", "final", "grade", "status")
table = ttk.Treeview(output_frame, columns=columns, show="headings", height=8)
table.heading("id", text="Student ID")
table.heading("name", text="Full Name")
table.heading("final", text="Weighted Mark")
table.heading("grade", text="Letter Grade")
table.heading("status", text="Standing Status")

table.column("id", width=100, anchor="center")
table.column("name", width=200, anchor="w")
table.column("final", width=110, anchor="center")
table.column("grade", width=140, anchor="center")
table.column("status", width=110, anchor="center")
table.pack(fill="both", expand=True)

# Processing Dashboard Metrics Display Panel
analytics_frame = tk.Frame(root, bg="#e2e8f0", padx=10)
analytics_frame.pack(fill="x", side="bottom")

lbl_avg_title = tk.Label(analytics_frame, text="Overall Class Average Score: ", font=("Tahoma", 10, "bold"),
                         bg="#e2e8f0", fg="#2d3748")
lbl_avg_title.pack(side="left", padx=5)
lbl_avg_val = tk.Label(analytics_frame, text="0.00%", font=("Tahoma", 10, "bold"), bg="#e2e8f0", fg="#2b6cb0")
lbl_avg_val.pack(side="left", padx=5)

lbl_highest_val = tk.Label(analytics_frame, text="0.00%", font=("Tahoma", 10, "bold"), bg="#e2e8f0", fg="#2f855a")
lbl_highest_val.pack(side="right", padx=5)
lbl_highest_title = tk.Label(analytics_frame, text="Highest Class Score: ", font=("Tahoma", 10, "bold"), bg="#e2e8f0",
                             fg="#2d3748")
lbl_highest_title.pack(side="right", padx=5)

# Run Loop Initialization Execution Frame
root.mainloop()
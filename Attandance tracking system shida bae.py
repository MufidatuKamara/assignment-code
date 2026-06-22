import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText


# ==========================
# STUDENT DATA
# ==========================

student_info = {
    "name": "Your Name",
    "university": "Limkokwing University",
    "enrollment": "2025",
    "email": "your_email@gmail.com"
}

modules = [
    ("Principle of Programming", "Mr Elijah Fulla"),
    ("Introduction to Database", "Mr Amed Jelil Conteh"),
    ("Introduction to Data Communication", "Mr Mustapha Kamara"),
    ("Computerized Mathematics", "Mr Amadu Kamara"),
    ("Principle of Software Engineering", "Mr Hassan Mansaray"),
    ("Introduction to Multimedia", "Mr Abubakarr Tappia Sesay")
]


# ==========================
# EMAIL FUNCTION
# ==========================

def send_email_notification():

    sender_email = "yourgmail@gmail.com"
    app_password = "your_app_password"

    receiver_email = student_info["email"]

    subject = "Student Academic Portal Notification"

    body = f"""
Hello {student_info['name']},

Welcome to the Student Academic Portal.

University: {student_info['university']}
Enrollment Year: {student_info['enrollment']}

Your modules have been successfully loaded.

Regards,
Academic Administration
"""

    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = receiver_email

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()

        messagebox.showinfo(
            "Email Sent",
            f"Notification sent to {receiver_email}"
        )

    except Exception as e:
        messagebox.showerror(
            "Email Error",
            str(e)
        )


# ==========================
# PORTAL WINDOW
# ==========================

def open_portal():

    portal = tk.Toplevel()
    portal.title("Student Academic Portal")
    portal.geometry("700x500")
    portal.configure(bg="lightblue")

    title = tk.Label(
        portal,
        text="STUDENT ACADEMIC PORTAL",
        font=("Arial", 18, "bold"),
        bg="lightblue"
    )
    title.pack(pady=10)

    info_frame = tk.Frame(portal, bg="white")
    info_frame.pack(fill="x", padx=20, pady=10)

    tk.Label(
        info_frame,
        text=f"Student Name: {student_info['name']}",
        font=("Arial", 12),
        bg="white"
    ).pack(anchor="w")

    tk.Label(
        info_frame,
        text=f"University: {student_info['university']}",
        font=("Arial", 12),
        bg="white"
    ).pack(anchor="w")

    tk.Label(
        info_frame,
        text=f"Enrollment: {student_info['enrollment']}",
        font=("Arial", 12),
        bg="white"
    ).pack(anchor="w")

    tk.Label(
        info_frame,
        text=f"Email: {student_info['email']}",
        font=("Arial", 12),
        bg="white"
    ).pack(anchor="w")

    module_frame = tk.LabelFrame(
        portal,
        text="Registered Modules",
        font=("Arial", 12, "bold")
    )
    module_frame.pack(fill="both", expand=True, padx=20, pady=10)

    for module, lecturer in modules:
        tk.Label(
            module_frame,
            text=f"{module}  --->  {lecturer}",
            font=("Arial", 11)
        ).pack(anchor="w", padx=10, pady=3)

    notify_btn = tk.Button(
        portal,
        text="Send Email Notification",
        bg="green",
        fg="white",
        font=("Arial", 11, "bold"),
        command=send_email_notification
    )
    notify_btn.pack(pady=10)


# ==========================
# LOGIN FUNCTION
# ==========================

def login():

    username = username_entry.get()
    password = password_entry.get()

    if username == "student" and password == "12345":
        messagebox.showinfo(
            "Login Successful",
            "Welcome to the Student Academic Portal"
        )
        open_portal()
    else:
        messagebox.showerror(
            "Login Failed",
            "Invalid Username or Password"
        )


# ==========================
# MAIN WINDOW
# ==========================

root = tk.Tk()
root.title("Login System")
root.geometry("400x300")
root.configure(bg="skyblue")

title_label = tk.Label(
    root,
    text="Student Login",
    font=("Arial", 18, "bold"),
    bg="skyblue"
)
title_label.pack(pady=20)

tk.Label(
    root,
    text="Username",
    bg="skyblue",
    font=("Arial", 12)
).pack()

username_entry = tk.Entry(root, width=30)
username_entry.pack(pady=5)

tk.Label(
    root,
    text="Password",
    bg="skyblue",
    font=("Arial", 12)
).pack()

password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

login_button = tk.Button(
    root,
    text="Login",
    bg="blue",
    fg="white",
    font=("Arial", 12, "bold"),
    command=login
)
login_button.pack(pady=20)

root.mainloop()
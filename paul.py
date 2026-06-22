import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText


class LimkokwingPortalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Limkokwing Student Portal")
        self.root.geometry("600x600")
        self.root.configure(bg="#f0f4f8")

        # 1. System Data - Updated with your details
        self.student_info = {
            "name": "Jenneh Musa",
            "university": "Limkokwing University",
            "course": "Diploma in Information Technology",
            "enrollment": "2025",
            "email": "jennehmusa@icloud.com"
        }

        self.modules = [
            ("Principle of Programming", "Mr. Elijah Fulla"),
            ("Introduction to Database", "Mr. Amed Jelil Conteh"),
            ("Introduction to Data Communication", "Mr. Mustapha Kamara"),
            ("Computerized Mathematics", "Mr. Amadu Kamara"),
            ("Principle of Software Engineering", "Mr. Hassan Mansaray"),
            ("Introduction to Multimedia", "Mr. Abubakarr Tappia Sesay")
        ]

        self.build_gui()

    def build_gui(self):
        # Header
        header = tk.Label(self.root, text="STUDENT ACADEMIC PORTAL", font=("Arial", 16, "bold"), bg="#f0f4f8",
                          fg="#1e3a8a")
        header.pack(pady=15)

        # Student Information Section
        info_frame = tk.LabelFrame(self.root, text="Student Details", font=("Arial", 11, "bold"), bg="white", padx=15,
                                   pady=10)
        info_frame.pack(fill="x", padx=20, pady=10)

        tk.Label(info_frame, text=f"Student Name: {self.student_info['name']}", bg="white", font=("Arial", 10)).pack(
            anchor="w")
        tk.Label(info_frame, text=f"University: {self.student_info['university']}", bg="white",
                 font=("Arial", 10)).pack(anchor="w")
        tk.Label(info_frame, text=f"Course: {self.student_info['course']}", bg="white", font=("Arial", 10)).pack(
            anchor="w")
        tk.Label(info_frame, text=f"Enrollment: {self.student_info['enrollment']}", bg="white",
                 font=("Arial", 10)).pack(anchor="w")
        tk.Label(info_frame, text=f"Email: {self.student_info['email']}", bg="white", font=("Arial", 10)).pack(
            anchor="w")

        # Modules Section
        module_frame = tk.LabelFrame(self.root, text="Registered Modules", font=("Arial", 11, "bold"), bg="white",
                                     padx=15, pady=10)
        module_frame.pack(fill="both", expand=True, padx=20, pady=10)

        for mod, lec in self.modules:
            tk.Label(module_frame, text=f"• {mod} - {lec}", bg="white", font=("Arial", 10)).pack(anchor="w", pady=2)

        # Email Notification Section
        email_frame = tk.Frame(self.root, bg="#f0f4f8")
        email_frame.pack(fill="x", padx=20, pady=15)

        tk.Label(email_frame, text="Notification Email:", bg="#f0f4f8", font=("Arial", 10, "bold")).pack(side="left")

        # Pre-fill the entry box with the student's iCloud email
        self.email_entry = tk.Entry(email_frame, width=30, font=("Arial", 10))
        self.email_entry.insert(0, self.student_info['email'])
        self.email_entry.pack(side="left", padx=10)

        notify_btn = tk.Button(email_frame, text="Send to Phone", bg="#2563eb", fg="white", font=("Arial", 10, "bold"),
                               command=self.send_notification)
        notify_btn.pack(side="right")

    def send_notification(self):
        receiver_email = self.email_entry.get().strip()

        if not receiver_email:
            messagebox.showwarning("Input Error", "Please enter a valid email address.")
            return

        # ⚠️ IMPORTANT: To actually send emails via Python, you need an SMTP server.
        # If using Gmail to send the notification out, put the sender details below:
        sender_email = "your_sender_email@gmail.com"
        app_password = "your_16_digit_app_password"

        subject = "Limkokwing Academic Portal - Modules Loaded"
        body = f"Hello {self.student_info['name']},\n\nWelcome to {self.student_info['university']}!\nCourse: {self.student_info['course']}\nEnrollment Year: {self.student_info['enrollment']}\n\nYour registered modules are:\n"

        for mod, lec in self.modules:
            body += f"- {mod} (Lecturer: {lec})\n"

        body += "\nBest regards,\nAcademic Administration"

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

            messagebox.showinfo("Success", f"Notification successfully sent to your phone via {receiver_email}!")
        except Exception as e:
            messagebox.showerror("Email Failed",
                                 f"Could not send email.\nEnsure you have configured the sender_email and app_password in the code.\n\nError: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = LimkokwingPortalApp(root)
    root.mainloop()
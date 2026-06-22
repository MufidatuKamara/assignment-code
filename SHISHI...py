import tkinter as tk
from tkinter import ttk, messagebox
import time


class Patient:
    def __init__(self, patient_id, name, reason, p_type, is_urgent):
        self.patient_id = patient_id
        self.name = name
        self.reason = reason
        self.p_type = p_type  # "Walk-in" or "Appointment"
        self.is_urgent = is_urgent
        self.status = "Waiting"
        self.time_added = time.strftime("%H:%M:%S")

    def __str__(self):
        urgency = "[URGENT] " if self.is_urgent else ""
        return f"{urgency}{self.name} ({self.p_type}) - {self.reason}"


class ClinicSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HealthSync Clinic - Advanced Queue & Records")
        self.root.geometry("850x600")
        self.root.configure(bg="#f8fafc")

        # System Data
        self.queue = []
        self.active_patient = None
        self.records = []  # Secure patient history
        self.patient_counter = 1000

        self.build_gui()

    def build_gui(self):
        # Header
        header = tk.Label(self.root, text="CLINIC MANAGEMENT SYSTEM", font=("Arial", 16, "bold"), bg="#f8fafc",
                          fg="#0f172a")
        header.pack(pady=10)

        # Tabbed Layout (Notebook)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=20, pady=10)

        self.tab_queue = tk.Frame(self.notebook, bg="#f8fafc")
        self.tab_records = tk.Frame(self.notebook, bg="#f8fafc")

        self.notebook.add(self.tab_queue, text="Live Queue Management")
        self.notebook.add(self.tab_records, text="Secure Patient Records")

        self.build_queue_tab()
        self.build_records_tab()

    def build_queue_tab(self):
        # --- Left Side: Registration & Serving ---
        left_frame = tk.Frame(self.tab_queue, bg="#f8fafc")
        left_frame.pack(side="left", fill="y", padx=10, pady=10)

        # Registration
        reg_frame = tk.LabelFrame(left_frame, text="Quick Registration", font=("Arial", 11, "bold"), bg="white",
                                  padx=15, pady=10)
        reg_frame.pack(fill="x", pady=(0, 15))

        tk.Label(reg_frame, text="Patient Name:", bg="white").pack(anchor="w")
        self.name_entry = tk.Entry(reg_frame, width=30)
        self.name_entry.pack(pady=(0, 10))

        tk.Label(reg_frame, text="Reason/Condition:", bg="white").pack(anchor="w")
        self.reason_entry = tk.Entry(reg_frame, width=30)
        self.reason_entry.pack(pady=(0, 10))

        tk.Label(reg_frame, text="Visit Type:", bg="white").pack(anchor="w")
        self.type_var = tk.StringVar(value="Walk-in")
        tk.Radiobutton(reg_frame, text="Walk-in", variable=self.type_var, value="Walk-in", bg="white").pack(anchor="w")
        tk.Radiobutton(reg_frame, text="Appointment", variable=self.type_var, value="Appointment", bg="white").pack(
            anchor="w")

        self.urgent_var = tk.BooleanVar()
        tk.Checkbutton(reg_frame, text="Urgent / Emergency", variable=self.urgent_var, bg="white", fg="red",
                       font=("Arial", 9, "bold")).pack(anchor="w", pady=10)

        tk.Button(reg_frame, text="Register & Add", bg="#0f172a", fg="white", font=("Arial", 10, "bold"),
                  command=self.register_patient).pack(fill="x")

        # Active Consultation
        serving_frame = tk.LabelFrame(left_frame, text="Currently Serving", font=("Arial", 11, "bold"), bg="#eff6ff",
                                      fg="#1e3a8a", padx=15, pady=10)
        serving_frame.pack(fill="both", expand=True)

        self.serving_label = tk.Label(serving_frame, text="Doctor is available.", bg="#eff6ff", font=("Arial", 11),
                                      fg="#64748b", wraplength=180)
        self.serving_label.pack(expand=True, pady=10)

        tk.Button(serving_frame, text="Finish & Save Record", bg="#16a34a", fg="white", font=("Arial", 10, "bold"),
                  command=self.finish_consultation).pack(fill="x")

        # --- Right Side: Queue List ---
        right_frame = tk.LabelFrame(self.tab_queue, text="Waitlist & Status", font=("Arial", 11, "bold"), bg="white",
                                    padx=10, pady=10)
        right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Treeview to show columns (Name, Est Wait, Type)
        columns = ("Name", "Type", "Est Wait Time")
        self.tree_queue = ttk.Treeview(right_frame, columns=columns, show="headings", height=15)
        self.tree_queue.heading("Name", text="Patient Name")
        self.tree_queue.heading("Type", text="Visit Type")
        self.tree_queue.heading("Est Wait Time", text="Est Wait Time")

        self.tree_queue.column("Name", width=180)
        self.tree_queue.column("Type", width=100)
        self.tree_queue.column("Est Wait Time", width=100)
        self.tree_queue.pack(fill="both", expand=True, pady=5)

        # Buttons
        btn_frame = tk.Frame(right_frame, bg="white")
        btn_frame.pack(fill="x", pady=5)

        tk.Button(btn_frame, text="Notify (SMS)", bg="#f59e0b", fg="white", font=("Arial", 10, "bold"),
                  command=self.notify_patient).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Call to Office", bg="#2563eb", fg="white", font=("Arial", 10, "bold"),
                  command=self.call_patient).pack(side="right", padx=5)

    def build_records_tab(self):
        frame = tk.Frame(self.tab_records, bg="white", padx=20, pady=20)
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="Secure Patient History", font=("Arial", 14, "bold"), bg="white").pack(anchor="w",
                                                                                                    pady=(0, 10))

        columns = ("ID", "Name", "Reason", "Type", "Status")
        self.tree_records = ttk.Treeview(frame, columns=columns, show="headings")
        for col in columns:
            self.tree_records.heading(col, text=col)
            self.tree_records.column(col, width=120)

        self.tree_records.pack(fill="both", expand=True)

    def register_patient(self):
        name = self.name_entry.get().strip()
        reason = self.reason_entry.get().strip()
        p_type = self.type_var.get()
        is_urgent = self.urgent_var.get()

        if not name:
            messagebox.showwarning("Error", "Patient name is required.")
            return

        self.patient_counter += 1
        new_patient = Patient(f"PT{self.patient_counter}", name, reason, p_type, is_urgent)

        if is_urgent:
            self.queue.insert(0, new_patient)
        else:
            self.queue.append(new_patient)

        self.refresh_queue()

        # Reset form
        self.name_entry.delete(0, tk.END)
        self.reason_entry.delete(0, tk.END)
        self.type_var.set("Walk-in")
        self.urgent_var.set(False)

    def notify_patient(self):
        selected = self.tree_queue.selection()
        if not selected:
            messagebox.showinfo("Select", "Please select a patient from the waitlist to notify.")
            return

        item = self.tree_queue.item(selected[0])
        name = item['values'][0]
        messagebox.showinfo("SMS Sent",
                            f"Notification sent to {name}:\n\n'Please proceed to the waiting area. It's almost your turn to see the doctor!'")

    def call_patient(self):
        if not self.queue:
            messagebox.showinfo("Queue Empty", "No patients are waiting.")
            return

        if self.active_patient is not None:
            messagebox.showwarning("Doctor Busy", "Please complete the current consultation first.")
            return

        # Simple FIFO with priority already sorted
        self.active_patient = self.queue.pop(0)
        self.active_patient.status = "In Consultation"

        self.serving_label.config(
            text=f"{self.active_patient.name}\n({self.active_patient.p_type})\n\nReason: {self.active_patient.reason}",
            fg="#0f172a", font=("Arial", 12, "bold")
        )
        self.refresh_queue()

    def finish_consultation(self):
        if self.active_patient is None:
            return

        self.active_patient.status = "Done"
        # Save to records
        self.records.insert(0, self.active_patient)

        # Update Records Table
        self.tree_records.insert("", "end", values=(
            self.active_patient.patient_id,
            self.active_patient.name,
            self.active_patient.reason,
            self.active_patient.p_type,
            self.active_patient.status
        ))

        self.active_patient = None
        self.serving_label.config(text="Doctor is available.", fg="#64748b", font=("Arial", 11, "normal"))
        messagebox.showinfo("Success", "Consultation completed. Record saved securely.")
        self.refresh_queue()

    def refresh_queue(self):
        # Clear tree
        for row in self.tree_queue.get_children():
            self.tree_queue.delete(row)

        # Repopulate
        for idx, p in enumerate(self.queue):
            # Calculate est wait time (e.g. 15 mins per person ahead, plus active patient)
            base_wait = 15
            multiplier = idx + (1 if self.active_patient else 0)
            est_wait = f"~{multiplier * base_wait} mins"

            name_display = f"[URGENT] {p.name}" if p.is_urgent else p.name

            self.tree_queue.insert("", "end", values=(name_display, p.p_type, est_wait))


if __name__ == "__main__":
    root = tk.Tk()
    app = ClinicSystemApp(root)
    root.mainloop()
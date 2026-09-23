import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt

subjects = ["Python", "Data Structures", "Web Development", "Mathematics", "Database"]
marks = []
attendance = []

def calculate():
    try:
        name = name_entry.get()

        if name == "":
            messagebox.showerror("Error", "Enter student name")
            return

        marks.clear()
        attendance.clear()

        for i in range(5):
            m = float(mark_entries[i].get())
            a = float(att_entries[i].get())

            if m < 0 or m > 100 or a < 0 or a > 100:
                raise ValueError

            marks.append(m)
            attendance.append(a)

        grades = []
        points = []

        for m in marks:
            if m >= 90:
                grade, point = "A+", 10
            elif m >= 80:
                grade, point = "A", 9
            elif m >= 70:
                grade, point = "B+", 8
            elif m >= 60:
                grade, point = "B", 7
            elif m >= 50:
                grade, point = "C", 6
            elif m >= 40:
                grade, point = "D", 5
            else:
                grade, point = "F", 0

            grades.append(grade)
            points.append(point)

        total = sum(marks)
        percentage = total / 5
        gpa = sum(points) / 5
        cgpa = gpa

        result.delete("1.0", tk.END)
        result.insert(tk.END, f"Student: {name}\n")
        result.insert(tk.END, "-" * 40 + "\n")

        for i in range(5):
            result.insert(
                tk.END,
                f"{subjects[i]:20} {marks[i]:5.1f}  "
                f"{grades[i]:3}  Attendance: {attendance[i]:.1f}%\n"
            )

        result.insert(tk.END, "-" * 40 + "\n")
        result.insert(tk.END, f"Total Marks : {total:.1f}/500\n")
        result.insert(tk.END, f"Percentage  : {percentage:.2f}%\n")
        result.insert(tk.END, f"GPA         : {gpa:.2f}\n")
        result.insert(tk.END, f"CGPA        : {cgpa:.2f}\n")

    except ValueError:
        messagebox.showerror("Error", "Enter valid marks and attendance")

def show_chart():
    if not marks:
        messagebox.showerror("Error", "Calculate result first")
        return

    plt.figure(figsize=(8, 5))
    plt.bar(subjects, marks)
    plt.title("Subject-wise Academic Performance")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.ylim(0, 100)
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.show()

def show_attendance():
    if not attendance:
        messagebox.showerror("Error", "Calculate result first")
        return

    plt.figure(figsize=(8, 5))
    plt.bar(subjects, attendance)
    plt.title("Subject-wise Attendance")
    plt.xlabel("Subjects")
    plt.ylabel("Attendance (%)")
    plt.ylim(0, 100)
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.show()

root = tk.Tk()
root.title("Intelligent Academic Performance Tracker")
root.geometry("850x650")

title = tk.Label(
    root,
    text="Intelligent Academic Performance Tracker",
    font=("Arial", 20, "bold")
)
title.pack(pady=15)

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Student Name:", font=("Arial", 12)).grid(
    row=0, column=0, padx=10, pady=8
)

name_entry = tk.Entry(frame, width=25)
name_entry.grid(row=0, column=1, padx=10)

tk.Label(frame, text="Subject", font=("Arial", 12, "bold")).grid(
    row=1, column=0, padx=20
)

tk.Label(frame, text="Marks", font=("Arial", 12, "bold")).grid(
    row=1, column=1
)

tk.Label(frame, text="Attendance %", font=("Arial", 12, "bold")).grid(
    row=1, column=2
)

mark_entries = []
att_entries = []

for i, subject in enumerate(subjects):
    tk.Label(frame, text=subject).grid(row=i+2, column=0, pady=5)

    m = tk.Entry(frame, width=12)
    m.grid(row=i+2, column=1)
    mark_entries.append(m)

    a = tk.Entry(frame, width=12)
    a.grid(row=i+2, column=2)
    att_entries.append(a)

button_frame = tk.Frame(root)
button_frame.pack(pady=15)

tk.Button(
    button_frame,
    text="Calculate Result",
    command=calculate,
    width=18
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="Performance Chart",
    command=show_chart,
    width=18
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="Attendance Chart",
    command=show_attendance,
    width=18
).grid(row=0, column=2, padx=5)

result = tk.Text(root, width=85, height=15, font=("Courier New", 11))
result.pack(pady=10)

root.mainloop()
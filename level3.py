import matplotlib.pyplot as plt

name = input("Enter student name: ").strip()
semester = input("Enter semester: ").strip()

if not name or not semester:
    print("Name and semester cannot be empty.")
    exit()

subjects = ["Python", "DS", "Web", "Math"]
credits = [4, 4, 3, 4]
marks = []
attendance = []
points = []

for subject in subjects:
    while True:
        try:
            m = float(input("Enter marks in " + subject + " (0-100): "))
            if 0 <= m <= 100:
                break
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            a = float(input("Enter attendance in " + subject + " (0-100): "))
            if 0 <= a <= 100:
                break
            print("Attendance must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

    marks.append(m)
    attendance.append(a)
    points.append(min(m // 10, 10))

total = sum(marks)
percentage = total / len(subjects)
gpa = sum(points[i] * credits[i] for i in range(4)) / sum(credits)
cgpa = gpa
avg_attendance = sum(attendance) / len(subjects)

print("\n===== ACADEMIC PERFORMANCE REPORT =====")
print("Student Name:", name)
print("Semester:", semester)
print("Total Marks:", total, "/400")
print("Percentage:", round(percentage, 2), "%")
print("GPA:", round(gpa, 2), "/10")
print("Estimated CGPA:", round(cgpa, 2), "/10")
print("Average Attendance:", round(avg_attendance, 2), "%")

print("\nSubject Details:")

for i in range(4):
    if marks[i] >= 90:
        grade = "A+"
    elif marks[i] >= 80:
        grade = "A"
    elif marks[i] >= 70:
        grade = "B"
    elif marks[i] >= 60:
        grade = "C"
    elif marks[i] >= 40:
        grade = "D"
    else:
        grade = "Fail"

    status = "Eligible" if attendance[i] >= 75 else "Low Attendance"

    print(subjects[i], "| Marks:", marks[i],
          "| Grade:", grade,
          "| Attendance:", attendance[i], "%",
          "|", status)

print("\nPerformance Summary:")

if percentage >= 75:
    print("Excellent academic performance!")
elif percentage >= 60:
    print("Good performance. Keep improving!")
elif percentage >= 40:
    print("Average performance. More practice is needed.")
else:
    print("Needs improvement.")

fig, ax = plt.subplots(1, 2, figsize=(10, 4))

ax[0].bar(subjects, marks)
ax[0].set_title("Subject-wise Marks")
ax[0].set_ylabel("Marks")
ax[0].set_ylim(0, 100)

ax[1].bar(subjects, attendance)
ax[1].axhline(75, linestyle="--", label="75% Attendance")
ax[1].set_title("Subject-wise Attendance")
ax[1].set_ylabel("Attendance (%)")
ax[1].set_ylim(0, 100)
ax[1].legend()

plt.suptitle("Academic Performance Dashboard - " + name)
plt.tight_layout()
plt.show()
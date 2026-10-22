import matplotlib.pyplot as plt

name = input("Enter student name: ")
subjects = ["Python", "DS", "Web", "Math"]
marks = []
attendance = []
credits = [4, 4, 3, 4]
points = []

for subject in subjects:
    m = float(input("Enter marks in " + subject + ": "))
    a = float(input("Enter attendance in " + subject + " (%): "))

    if not 0 <= m <= 100 or not 0 <= a <= 100:
        print("Invalid input. Enter values between 0 and 100.")
        exit()

    marks.append(m)
    attendance.append(a)

    p = min(m // 10, 10)
    points.append(p)

total = sum(marks)
percentage = total / len(subjects)
gpa = sum(points[i] * credits[i] for i in range(4)) / sum(credits)

print("\n--- Academic Performance Report ---")
print("Student:", name)
print("Total Marks:", total, "/400")
print("Percentage:", round(percentage, 2), "%")
print("GPA:", round(gpa, 2), "/10")

print("\nSubject-wise Report:")

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

    status = "Good" if attendance[i] >= 75 else "Low"

    print(subjects[i], "- Marks:", marks[i],
          "Grade:", grade, "Attendance:", attendance[i], "%", status)

plt.figure(figsize=(8, 4))
plt.bar(subjects, marks)
plt.title("Subject-wise Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 4))
plt.bar(subjects, attendance)
plt.title("Subject-wise Attendance")
plt.xlabel("Subjects")
plt.ylabel("Attendance (%)")
plt.ylim(0, 100)
plt.tight_layout()
plt.show()

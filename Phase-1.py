import matplotlib.pyplot as plt

name = input("Enter student name: ")
subjects = ["Python", "DS", "Web", "Math"]
marks = []
attendance = []

for subject in subjects:
    m = float(input("Enter marks in " + subject + " (out of 100): "))
    a = float(input("Enter attendance in " + subject + " (%): "))
    if m < 0 or m > 100 or a < 0 or a > 100:
        print("Invalid input. Enter values between 0 and 100.")
        exit()
    marks.append(m)
    attendance.append(a)

total = sum(marks)
percentage = total / len(subjects)

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "Fail"

print("\n--- Student Report ---")
print("Name:", name)
print("Total Marks:", total, "/400")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Average Attendance:", round(sum(attendance) / len(subjects), 2), "%")

plt.bar(subjects, marks)
plt.title("Academic Performance")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.show()

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

st.set_page_config(page_title="Academic Performance Tracker", page_icon="📊", layout="wide")
st.title("🎓 Intelligent Academic Performance Tracker & Visualizer")
st.write("Analyze marks, grades, GPA and attendance.")

st.sidebar.header("Student Information")
name = st.sidebar.text_input("Student Name")
roll = st.sidebar.text_input("Roll Number")
department = st.sidebar.selectbox("Department", ["CSE", "CSE (AI & ML)", "IT", "ENTC", "Mechanical", "Civil", "Other"])
semester = st.sidebar.selectbox("Semester", [f"Semester {i}" for i in range(1, 9)])

st.subheader("📚 Enter Subject Details")
default_subjects = ["Python", "Data Structures", "Web Development", "Mathematics"]
subjects = []

for i, subject in enumerate(default_subjects):
    with st.expander(subject, expanded=True):
        c1, c2, c3 = st.columns(3)
        with c1:
            mark = st.number_input(f"{subject} Marks (out of 100)", 0, 100, 0, key=f"marks_{i}")
        with c2:
            attendance = st.number_input(f"{subject} Attendance (%)", 0, 100, 75, key=f"attendance_{i}")
        with c3:
            credits = st.number_input(f"{subject} Credits", 1, 10, 4, key=f"credits_{i}")
        subjects.append({"Subject": subject, "Marks": mark, "Attendance": attendance, "Credits": credits})

def get_grade(mark):
    if mark >= 90: return "A+"
    if mark >= 80: return "A"
    if mark >= 70: return "B"
    if mark >= 60: return "C"
    if mark >= 50: return "D"
    if mark >= 40: return "E"
    return "F"

def get_grade_point(mark):
    if mark >= 90: return 10
    if mark >= 80: return 9
    if mark >= 70: return 8
    if mark >= 60: return 7
    if mark >= 50: return 6
    if mark >= 40: return 5
    return 0

if st.button("📊 Analyze Academic Performance", type="primary"):
    if not name.strip() or not roll.strip():
        st.error("Please enter the student name and roll number.")
    else:
        df = pd.DataFrame(subjects)
        df["Grade"] = df["Marks"].apply(get_grade)
        df["Grade Point"] = df["Marks"].apply(get_grade_point)
        df["Attendance Status"] = df["Attendance"].apply(lambda x: "Eligible" if x >= 75 else "Shortage")

        total_marks = int(df["Marks"].sum())
        maximum_marks = len(df) * 100
        percentage = total_marks / maximum_marks * 100
        gpa = (df["Grade Point"] * df["Credits"]).sum() / df["Credits"].sum()
        average_attendance = df["Attendance"].mean()

        if percentage >= 90: overall_grade = "A+"
        elif percentage >= 80: overall_grade = "A"
        elif percentage >= 70: overall_grade = "B"
        elif percentage >= 60: overall_grade = "C"
        elif percentage >= 50: overall_grade = "D"
        elif percentage >= 40: overall_grade = "E"
        else: overall_grade = "F"

        st.success(f"Analysis completed for {name}!")
        st.subheader("📌 Student Summary")
        st.write(f"**Name:** {name}  |  **Roll Number:** {roll}")
        st.write(f"**Department:** {department}  |  **Semester:** {semester}")

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total Marks", f"{total_marks}/{maximum_marks}")
        c2.metric("Percentage", f"{percentage:.2f}%")
        c3.metric("GPA", f"{gpa:.2f}/10")
        c4.metric("Avg. Attendance", f"{average_attendance:.2f}%")
        st.metric("Overall Grade", overall_grade)

        st.subheader("📋 Subject-wise Performance")
        st.dataframe(df, use_container_width=True, hide_index=True)

        st.subheader("📊 Marks Comparison")
        fig, ax = plt.subplots()
        ax.bar(df["Subject"], df["Marks"])
        ax.set_ylim(0, 100)
        ax.set_ylabel("Marks")
        ax.set_title("Subject-wise Marks")
        plt.xticks(rotation=20, ha="right")
        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

        st.subheader("📈 Attendance Analysis")
        fig, ax = plt.subplots()
        ax.bar(df["Subject"], df["Attendance"])
        ax.axhline(y=75, linestyle="--", label="Minimum Attendance (75%)")
        ax.set_ylim(0, 100)
        ax.set_ylabel("Attendance (%)")
        ax.set_title("Subject-wise Attendance")
        ax.legend()
        plt.xticks(rotation=20, ha="right")
        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

        st.subheader("🎯 Academic Insights")
        st.write(f"**Highest-scoring subject:** {df.loc[df['Marks'].idxmax(), 'Subject']}")
        st.write(f"**Subject needing improvement:** {df.loc[df['Marks'].idxmin(), 'Subject']}")
        shortage = df[df["Attendance"] < 75]
        if shortage.empty:
            st.success("Attendance is at least 75% in every subject.")
        else:
            st.warning("Attendance is below 75% in: " + ", ".join(shortage["Subject"].tolist()))

        st.subheader("⬇️ Download Academic Report")
        report = BytesIO()
        with pd.ExcelWriter(report, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="Academic Report")
            summary = pd.DataFrame({
                "Detail": ["Student Name", "Roll Number", "Department", "Semester", "Total Marks", "Percentage", "Overall Grade", "GPA", "Average Attendance"],
                "Value": [name, roll, department, semester, f"{total_marks}/{maximum_marks}", f"{percentage:.2f}%", overall_grade, f"{gpa:.2f}", f"{average_attendance:.2f}%"]
            })
            summary.to_excel(writer, index=False, sheet_name="Student Summary")
        st.download_button("Download Excel Report", data=report.getvalue(), file_name=f"{roll}_academic_report.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

st.divider()
st.caption("Intelligent Academic Performance Tracker & Visualizer | Phase 3")

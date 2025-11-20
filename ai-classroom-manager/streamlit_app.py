import streamlit as st
from features import (
    generate_timetable,
    generate_lesson_plan,
    generate_test,
    generate_parent_message,
    generate_behavior_note,          # ✅ correct name
    generate_emergency_lesson_plan,  # ✅ correct name
    generate_progress_heatmap,
)

# Basic page config
st.set_page_config(page_title="AI Classroom Manager", layout="wide")

st.title("📘 AI Classroom Manager Agent")
st.write("Your personal teaching assistant — powered by OpenRouter / OpenAI (same brain as your CLI & Flask app).")

# Sidebar menu
menu = st.sidebar.radio(
    "Choose a Feature",
    [
        "Generate Timetable",
        "Generate Lesson Plan",
        "Generate Test / Worksheet",
        "Parent Message",
        "Behaviour Note",
        "Emergency Plan",
        "Progress Heatmap",
    ],
)

# -------------------------------------------------
# 1. Timetable
# -------------------------------------------------
if menu == "Generate Timetable":
    st.header("📅 Generate Timetable")

    classes_str = st.text_input(
        "Classes (comma-separated)",
        "Class 6-A, Class 6-B, Class 7-A",
    )
    periods = st.number_input(
        "Periods per day",
        min_value=1,
        max_value=12,
        value=6,
    )
    days_str = st.text_input(
        "Days (comma-separated)",
        "Monday, Tuesday, Wednesday, Thursday, Friday",
    )

    if st.button("Generate Timetable"):
        classes = [c.strip() for c in classes_str.split(",") if c.strip()]
        days = [d.strip() for d in days_str.split(",") if d.strip()]

        if not classes or not days:
            st.error("Please enter at least one class and one day.")
        else:
            result = generate_timetable(classes, periods, days)
            st.success(result)

# -------------------------------------------------
# 2. Lesson Plan
# -------------------------------------------------
elif menu == "Generate Lesson Plan":
    st.header("📚 Generate Lesson Plan")

    col1, col2 = st.columns(2)
    with col1:
        grade = st.text_input("Grade", "3")
        subject = st.text_input("Subject", "English")
    with col2:
        topic = st.text_input("Topic", "Eid")
        duration = st.number_input(
            "Duration (minutes)",
            min_value=5,
            max_value=200,
            value=45,
        )

    if st.button("Generate Lesson Plan"):
        result = generate_lesson_plan(grade, subject, topic, duration)
        st.success(result)

# -------------------------------------------------
# 3. Test / Worksheet
# -------------------------------------------------
elif menu == "Generate Test / Worksheet":
    st.header("📝 Generate Test / Worksheet")

    col1, col2 = st.columns(2)
    with col1:
        grade = st.text_input("Grade", "7")
        subject = st.text_input("Subject", "Science")
        topic = st.text_input("Topic", "Photosynthesis")
    with col2:
        question_type = st.selectbox(
            "Question Type",
            ["MCQ", "short", "long"],
            index=0,
        )
        count = st.number_input(
            "Number of Questions",
            min_value=1,
            max_value=50,
            value=5,
        )

    if st.button("Generate Test"):
        result = generate_test(
            topic=topic,
            question_type=question_type,
            count=int(count),
            grade=grade,
            subject=subject,
        )
        st.success(result)

# -------------------------------------------------
# 4. Parent Message
# -------------------------------------------------
elif menu == "Parent Message":
    st.header("👨‍👩‍👧 Parent Message")

    student_name = st.text_input("Student Name", "Ali Ahmed")
    issue_type = st.text_input("Issue / reason", "Homework not completed regularly")
    tone = st.selectbox(
        "Tone",
        ["polite", "firm but kind", "appreciative"],
        index=0,
    )

    if st.button("Generate Parent Message"):
        result = generate_parent_message(
            student_name=student_name,
            issue_type=issue_type,
            tone=tone,
        )
        st.success(result)

# -------------------------------------------------
# 5. Behaviour Note
# -------------------------------------------------
elif menu == "Behaviour Note":
    st.header("🧠 Behaviour / Observation Note")

    student_name = st.text_input("Student Name", "Sara")
    behaviour_issue = st.text_input(
        "Behaviour / Incident",
        "Talking in class and disturbing others",
    )
    positives = st.text_input(
        "Positives (optional)",
        "Participates actively, helps classmates",
    )

    if st.button("Generate Behaviour Note"):
        result = generate_behavior_note(
            student_name=student_name,
            behavior_issue=behaviour_issue,
            positives=positives,
        )
        st.success(result)

# -------------------------------------------------
# 6. Emergency Lesson Plan
# -------------------------------------------------
elif menu == "Emergency Plan":
    st.header("🚨 20-Minute Emergency Lesson Plan")

    col1, col2, col3 = st.columns(3)
    with col1:
        grade = st.text_input("Grade", "8")
    with col2:
        subject = st.text_input("Subject", "Maths")
    with col3:
        topic = st.text_input("Topic", "Fractions Revision")

    if st.button("Generate Emergency Lesson Plan"):
        result = generate_emergency_lesson_plan(
            grade=grade,
            subject=subject,
            topic=topic,
        )
        st.success(result)

# -------------------------------------------------
# 7. Progress Heatmap
# -------------------------------------------------
elif menu == "Progress Heatmap":
    st.header("📊 Progress Heatmap")

    class_name = st.text_input("Class name", "Class 7-B")
    subjects_str = st.text_input(
        "Subjects (comma-separated)",
        "Maths, English, Science",
    )
    percentages_str = st.text_input(
        "Percentages (comma-separated, same order)",
        "75, 88, 92",
    )

    if st.button("Generate Heatmap"):
        subjects = [s.strip() for s in subjects_str.split(",") if s.strip()]
        try:
            percentages = [int(p.strip()) for p in percentages_str.split(",") if p.strip()]
        except ValueError:
            st.error("Please enter valid integer percentages (e.g., 75, 88, 92).")
            st.stop()

        if len(subjects) != len(percentages):
            st.error("Number of subjects and percentages must match.")
        elif not subjects:
            st.error("Please enter at least one subject and percentage.")
        else:
            result = generate_progress_heatmap(
                subjects=subjects,
                percentages=percentages,
                class_name=class_name,
            )
            st.success(result)

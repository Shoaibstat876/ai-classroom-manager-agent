from flask import Flask, render_template, request
from features import (
    generate_timetable,
    generate_lesson_plan,
    generate_test,
    generate_parent_message,
    generate_behavior_note,
    generate_emergency_lesson_plan,
    generate_progress_heatmap,
)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result_title = None
    result_text = None
    active_tab = "timetable"  # default

    if request.method == "POST":
        action = request.form.get("action", "timetable")
        active_tab = action

        if action == "timetable":
            classes_raw = request.form.get("classes", "")
            periods = int(request.form.get("periods_per_day", "6") or 6)
            days_raw = request.form.get("days", "Monday,Tuesday,Wednesday,Thursday,Friday")

            classes = [c.strip() for c in classes_raw.split(",") if c.strip()]
            days = [d.strip() for d in days_raw.split(",") if d.strip()]

            result_text = generate_timetable(classes, periods, days)
            result_title = "Generated Timetable"

        elif action == "lesson_plan":
            grade = request.form.get("grade", "")
            subject = request.form.get("subject", "")
            topic = request.form.get("topic", "")
            duration = int(request.form.get("duration", "40") or 40)

            result_text = generate_lesson_plan(grade, subject, topic, duration)
            result_title = "Generated Lesson Plan"

        elif action == "test":
            grade = request.form.get("grade_test", "")
            subject = request.form.get("subject_test", "")
            topic = request.form.get("topic_test", "")
            qtype = request.form.get("question_type", "MCQ")
            count = int(request.form.get("count", "5") or 5)

            result_text = generate_test(topic, qtype, count, grade, subject)
            result_title = "Generated Test / Worksheet"

        elif action == "parent_message":
            student = request.form.get("student_name_msg", "")
            issue = request.form.get("issue_msg", "")
            tone = request.form.get("tone_msg", "polite")

            result_text = generate_parent_message(student, issue, tone)
            result_title = "Generated Parent Message"

        elif action == "behaviour":
            student = request.form.get("student_name_beh", "")
            issue = request.form.get("issue_beh", "")
            positives = request.form.get("positives_beh", "")

            result_text = generate_behavior_note(student, issue, positives)
            result_title = "Generated Behaviour / Observation Note"

        elif action == "emergency":
            grade = request.form.get("grade_em", "")
            subject = request.form.get("subject_em", "")
            topic = request.form.get("topic_em", "")

            result_text = generate_emergency_lesson_plan(grade, subject, topic)
            result_title = "Generated Emergency Lesson Plan"

        elif action == "heatmap":
            class_name = request.form.get("class_name_heat", "")
            subjects_raw = request.form.get("subjects_heat", "")
            subjects = [s.strip() for s in subjects_raw.split(",") if s.strip()]

            percentages = []
            for subject in subjects:
                key = f"pct_{subject}"
                value = request.form.get(key, "0") or "0"
                try:
                    percentages.append(int(value))
                except ValueError:
                    percentages.append(0)

            result_text = generate_progress_heatmap(subjects, percentages, class_name)
            result_title = "Generated Progress Heatmap"

    return render_template(
        "index.html",
        result_title=result_title,
        result_text=result_text,
        active_tab=active_tab,
    )


if __name__ == "__main__":
    app.run(debug=True)




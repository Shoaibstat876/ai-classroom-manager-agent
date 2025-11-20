from typing import List
from config import client, DEFAULT_MODEL


def _chat_completion(system_prompt: str, user_prompt: str) -> str:
    """
    Internal helper that sends a chat completion request
    and returns the plain text content.
    Works both with OpenRouter and OpenAI configs.
    """
    response = client.chat.completions.create(
        model=DEFAULT_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response.choices[0].message.content


# 1. Timetable Generator
def generate_timetable(
    classes: List[str],
    periods_per_day: int,
    days: List[str],
) -> str:
    system_prompt = (
        "You are a helpful school timetable generator for a Pakistani school. "
        "Avoid subject clashes for teachers and generate clean, readable tables."
    )
    user_prompt = (
        "Generate a weekly timetable.\n"
        f"Classes: {', '.join(classes)}\n"
        f"Days: {', '.join(days)}\n"
        f"Periods per day: {periods_per_day}\n\n"
        "Format it as simple text tables, one table per class."
    )
    return _chat_completion(system_prompt, user_prompt)


# 2. Lesson Plan
def generate_lesson_plan(
    grade: str,
    subject: str,
    topic: str,
    duration_minutes: int,
) -> str:
    system_prompt = (
        "You are an expert lesson plan designer following Bloom's Taxonomy. "
        "You design practical lesson plans for Pakistani classrooms."
    )
    user_prompt = (
        f"Create a lesson plan for Grade {grade}, Subject: {subject}, Topic: {topic}.\n"
        f"Duration: {duration_minutes} minutes.\n"
        "Include: Objectives, Materials, Warm-up, Main Activity, Assessment, Homework.\n"
        "Write it in clear bullet points."
    )
    return _chat_completion(system_prompt, user_prompt)


# 3. Test Generator
def generate_test(
    topic: str,
    question_type: str,
    count: int,
    grade: str,
    subject: str,
) -> str:
    system_prompt = (
        "You are an assessment generator for school exams. "
        "You create clear, age-appropriate questions suitable for Pakistani students."
    )
    user_prompt = (
        f"Generate {count} {question_type} questions for Grade {grade}, "
        f"Subject: {subject}, Topic: {topic}.\n"
        "If MCQ, include 4 options (A–D) and mark the correct answer clearly."
    )
    return _chat_completion(system_prompt, user_prompt)


# 4. Parent Message
def generate_parent_message(
    student_name: str,
    issue_type: str,
    tone: str,
) -> str:
    system_prompt = (
        "You are a polite school teacher writing SMS-style messages to parents. "
        "Tone must be respectful, short, and professional."
    )
    user_prompt = (
        f"Write a short SMS for the parents of {student_name} about: {issue_type}.\n"
        f"Tone: {tone}.\n"
        "Message should be 2–3 lines."
    )
    return _chat_completion(system_prompt, user_prompt)


# 5. Behaviour Note
def generate_behavior_note(
    student_name: str,
    behavior_issue: str,
    positives: str = "",
) -> str:
    system_prompt = (
        "You are a teacher writing formal behaviour/observation notes for school records."
    )
    user_prompt = (
        f"Create an observation note for student {student_name}.\n"
        f"Issue: {behavior_issue}.\n"
        f"Positives: {positives or 'none mentioned'}.\n"
        "Include: Summary, Behaviour Details, Teacher Recommendation."
    )
    return _chat_completion(system_prompt, user_prompt)


# 6. Emergency Lesson Plan
def generate_emergency_lesson_plan(
    grade: str,
    subject: str,
    topic: str,
) -> str:
    system_prompt = (
        "You are a teacher support AI that creates quick emergency lesson plans."
    )
    user_prompt = (
        f"Create a 20-minute emergency lesson plan for Grade {grade}, "
        f"Subject: {subject}, Topic: {topic}.\n"
        "Include: Quick objective, 1 main activity, 1 exit question."
    )
    return _chat_completion(system_prompt, user_prompt)


# 7. Progress Heatmap
def generate_progress_heatmap(
    subjects: List[str],
    percentages: List[int],
    class_name: str,
) -> str:
    system_prompt = "You create text-based progress heatmaps."

    bars = []
    for subject, pct in zip(subjects, percentages):
        filled = pct // 10
        empty = 10 - filled
        bar = "█" * filled + "▒" * empty
        bars.append(f"{subject}: {bar} ({pct}%)")

    user_prompt = (
        f"Class: {class_name}\n"
        "Progress data:\n"
        + "\n".join(bars)
        + "\nReturn a nicely formatted text heatmap and a short summary."
    )
    return _chat_completion(system_prompt, user_prompt)

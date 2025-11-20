from features import (
    generate_timetable,
    generate_lesson_plan,
    generate_test,
    generate_parent_message,
    generate_behavior_note,
    generate_emergency_lesson_plan,
    generate_progress_heatmap,
)


def menu():
    print("\n=== AI Classroom Manager Agent (CLI) ===")
    print("1. Generate Timetable")
    print("2. Generate Lesson Plan")
    print("3. Generate Test / Worksheet")
    print("4. Generate Parent Message")
    print("5. Generate Behaviour / Observation Note")
    print("6. Emergency 20-minute Lesson Plan")
    print("7. Progress Heatmap")
    print("0. Exit")


def handle_choice(choice: str):
    if choice == "1":
        classes = input("Enter classes (comma-separated): ").split(",")
        classes = [c.strip() for c in classes if c.strip()]
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        periods = int(input("Periods per day: "))
        result = generate_timetable(classes, periods, days)
        print("\n--- Timetable ---\n")
        print(result)

    elif choice == "2":
        grade = input("Grade: ")
        subject = input("Subject: ")
        topic = input("Topic: ")
        duration = int(input("Duration (min): "))
        result = generate_lesson_plan(grade, subject, topic, duration)
        print("\n--- Lesson Plan ---\n")
        print(result)

    elif choice == "3":
        grade = input("Grade: ")
        subject = input("Subject: ")
        topic = input("Topic: ")
        qtype = input("Type (MCQ/short/long): ")
        count = int(input("Count: "))
        result = generate_test(topic, qtype, count, grade, subject)
        print("\n--- Test ---\n")
        print(result)

    elif choice == "4":
        student = input("Student name: ")
        issue = input("Issue: ")
        tone = input("Tone (polite/firm but kind/appreciative): ")
        result = generate_parent_message(student, issue, tone)
        print("\n--- Parent Message ---\n")
        print(result)

    elif choice == "5":
        student = input("Student name: ")
        issue = input("Behaviour issue: ")
        positives = input("Positives (optional): ")
        result = generate_behavior_note(student, issue, positives)
        print("\n--- Behaviour Note ---\n")
        print(result)

    elif choice == "6":
        grade = input("Grade: ")
        subject = input("Subject: ")
        topic = input("Topic: ")
        result = generate_emergency_lesson_plan(grade, subject, topic)
        print("\n--- Emergency Lesson Plan ---\n")
        print(result)

    elif choice == "7":
        class_name = input("Class name: ")
        subjects = [s.strip() for s in input("Subjects (comma-separated): ").split(",")]
        percentages = [int(input(f"{s} %: ")) for s in subjects]
        result = generate_progress_heatmap(subjects, percentages, class_name)
        print("\n--- Progress Heatmap ---\n")
        print(result)

    else:
        print("Invalid choice.")


def main():
    while True:
        menu()
        choice = input("Choose option: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        handle_choice(choice)


if __name__ == "__main__":
    main()

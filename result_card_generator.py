"""Generate a formatted result card for one student."""


def get_valid_marks(subject):
    # Ask repeatedly until the entered subject marks are an integer from 0 to 100.
    while True:
        try:
            marks = int(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= marks <= 100:
                return marks
            print("Invalid marks. Enter a value between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def calculate_percentage(total, max_total):
    # Calculate the percentage from obtained and maximum marks.
    if max_total <= 0:
        return 0.0
    return (total / max_total) * 100


def get_grade(percentage):
    # Convert the percentage into the required letter grade.
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    return "Fail"


def format_name(name):
    # Remove extra spaces and capitalize each part of the student's name.
    return name.strip().title()


def get_valid_roll_number():
    # Accept a roll number only when it contains digits and nothing else.
    while True:
        roll_number = input("Enter roll number (digits only): ").strip()
        if roll_number.isdigit():
            return roll_number
        print("Invalid roll number. Use digits only (for example, 1025).")


def main():
    # Collect student details, calculate the result, and print the result card.
    print("=== Student Result Card Generator ===")
    while True:
        raw_name = input("Enter student name: ")
        student_name = format_name(raw_name)
        if student_name:
            break
        print("Name cannot be empty.")

    roll_number = get_valid_roll_number()
    subjects = ["English", "Mathematics", "Computer", "Physics", "Urdu"]
    subject_marks = {}

    for subject in subjects:
        subject_marks[subject] = get_valid_marks(subject)

    total = sum(subject_marks.values())
    max_total = len(subjects) * 100
    percentage = calculate_percentage(total, max_total)
    grade = get_grade(percentage)

    # A student must score at least 40 in every subject to pass.
    passed = all(mark >= 40 for mark in subject_marks.values())
    status = "Pass" if passed else "Fail"
    final_grade = grade if passed else "Fail"

    print("\n" + "=" * 42)
    print("             STUDENT RESULT CARD")
    print("=" * 42)
    print(f"Student Name : {student_name}")
    print(f"Roll Number  : {roll_number}")
    print("-" * 42)
    print(f"{'Subject':<22}{'Marks':>10}")
    print("-" * 42)
    for subject, marks in subject_marks.items():
        print(f"{subject:<22}{marks:>10}")
    print("-" * 42)
    print(f"{'Total Obtained':<22}{total:>10} / {max_total}")
    print(f"{'Percentage':<22}{percentage:>9.2f}%")
    print(f"{'Letter Grade':<22}{final_grade:>10}")
    print(f"{'Final Status':<22}{status:>10}")
    print("=" * 42)


if __name__ == "__main__":
    main()

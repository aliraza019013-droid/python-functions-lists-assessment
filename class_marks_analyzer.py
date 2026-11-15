"""Analyze marks for a class of students."""


def get_valid_integer(prompt, minimum=1):
    # Keep asking until the user enters an integer at least as large as minimum.
    while True:
        try:
            value = int(input(prompt))
            if value >= minimum:
                return value
            print(f"Please enter a number greater than or equal to {minimum}.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_valid_mark(student_name):
    # Ask repeatedly until a student's mark is a whole number from 0 to 100.
    while True:
        try:
            mark = int(input(f"Enter marks for {student_name} (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("Invalid marks. Enter a value between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def display_extreme_students(student_names, student_marks, target_mark):
    # Display every student whose marks match the selected highest or lowest mark.
    achievers = [
        name for name, mark in zip(student_names, student_marks)
        if mark == target_mark
    ]
    print(", ".join(achievers))


def main():
    # Collect class data and display a summary of student performance.
    print("=== Class Marks Analyzer ===")
    number_of_students = get_valid_integer("How many students are in the class? ")

    student_names = []
    student_marks = []

    for index in range(number_of_students):
        print(f"\nStudent {index + 1}")
        while True:
            name = input("Enter student name: ").strip()
            if name:
                student_names.append(name.title())
                break
            print("Name cannot be empty.")
        student_marks.append(get_valid_mark(student_names[-1]))

    class_average = sum(student_marks) / len(student_marks)
    highest_marks = max(student_marks)
    lowest_marks = min(student_marks)
    passing_students = sum(1 for mark in student_marks if mark >= 50)
    failing_students = len(student_marks) - passing_students

    above_average_students = [
        f"{name} ({mark})"
        for name, mark in zip(student_names, student_marks)
        if mark > class_average
    ]
    descending_marks = sorted(student_marks, reverse=True)

    print("\n========== CLASS PERFORMANCE REPORT ==========")
    print(f"Number of students : {len(student_names)}")
    print(f"Class average      : {class_average:.2f}")
    print(f"Highest marks      : {highest_marks}")
    print("Student(s) with highest marks: ", end="")
    display_extreme_students(student_names, student_marks, highest_marks)
    print(f"Lowest marks       : {lowest_marks}")
    print("Student(s) with lowest marks: ", end="")
    display_extreme_students(student_names, student_marks, lowest_marks)
    print(f"Passing students   : {passing_students}")
    print(f"Failing students   : {failing_students}")

    print("Students above class average:")
    if above_average_students:
        for student in above_average_students:
            print(f"- {student}")
    else:
        print("- None")

    print(f"Marks (highest to lowest): {descending_marks}")
    print("=" * 48)


if __name__ == "__main__":
    main()

"""Class Marks Analyzer.

Collects each student's name and marks in two parallel lists, then reports
the class average, highest and lowest marks (with tied students), pass/fail
counts, students above average and the marks sorted high to low.
"""

MIN_STUDENTS = 1
MIN_MARK, MAX_MARK = 0, 100
PASS_MARK = 40
LABEL_WIDTH = 19            # width used to align the report labels


def get_valid_integer(prompt, minimum):
    """Ask for a whole number that is at least `minimum`."""
    while True:
        text = input(prompt).strip()
        try:
            if "_" in text:                 # int() would accept "1_0"; reject it
                raise ValueError
            value = int(text)
        except ValueError:
            print("Error: Please enter a whole number.")
            continue
        if value >= minimum:
            return value
        print(f"Error: Value must be at least {minimum}.")


def get_valid_student_name():
    """Ask for a non-empty student name."""
    while True:
        name = input("Name: ").strip()
        if name:
            return name
        print("Error: Name cannot be empty. Please try again.")


def get_valid_mark(student_name):
    """Ask for a whole number from MIN_MARK to MAX_MARK for one student."""
    while True:
        text = input("Marks: ").strip()
        try:
            if "_" in text:
                raise ValueError
            mark = int(text)
        except ValueError:
            print(f"Error: Marks for {student_name} must be a whole number.")
            continue
        if MIN_MARK <= mark <= MAX_MARK:
            return mark
        print(f"Error: Marks for {student_name} must be between {MIN_MARK} and {MAX_MARK}.")


def display_extreme_students(label, mark, student_names, student_marks):
    """Show the highest/lowest mark and every student tied on it."""
    holders = [name for name, m in zip(student_names, student_marks) if m == mark]
    print(f"{label.capitalize() + ' marks':<{LABEL_WIDTH}}: {mark}")
    print(f"Student(s) with {label} marks: {', '.join(holders)}")


def display_above_average(student_names, student_marks, average):
    """List every student whose marks are above the class average."""
    above = [(n, m) for n, m in zip(student_names, student_marks) if m > average]
    print("Students above class average:")
    if not above:
        print("- None")
    for name, mark in above:
        print(f"- {name} ({mark})")


def main():
    print("=== Class Marks Analyzer ===")
    student_names = []
    student_marks = []
    try:
        count = get_valid_integer("How many students are in the class? ", MIN_STUDENTS)
        for number in range(1, count + 1):
            print(f"\nStudent {number}")
            name = get_valid_student_name()
            mark = get_valid_mark(name)
            student_names.append(name)
            student_marks.append(mark)
    except EOFError:
        print("\nError: Input ended before all values were entered.")
        return

    average = sum(student_marks) / len(student_marks)
    highest = max(student_marks)
    lowest = min(student_marks)
    passing = len([m for m in student_marks if m >= PASS_MARK])
    failing = len(student_marks) - passing
    ranked_marks = sorted(student_marks, reverse=True)

    print("\n--- Class Analysis ---")
    print(f"{'Number of students':<{LABEL_WIDTH}}: {len(student_marks)}")
    print(f"{'Class average':<{LABEL_WIDTH}}: {average:.2f}")
    display_extreme_students("highest", highest, student_names, student_marks)
    display_extreme_students("lowest", lowest, student_names, student_marks)
    print(f"{'Passing students':<{LABEL_WIDTH}}: {passing}")
    print(f"{'Failing students':<{LABEL_WIDTH}}: {failing}")
    display_above_average(student_names, student_marks, average)
    print(f"Marks (highest to lowest): {ranked_marks}")


if __name__ == "__main__":
    main()

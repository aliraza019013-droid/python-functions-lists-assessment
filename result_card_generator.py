"""Student Result Card Generator.

Reads one student's name, roll number and marks in five subjects, then
prints a result card with total, percentage, grade and final status.
A student fails if ANY subject mark is below the pass mark.
"""

# ---- Constants (no magic numbers) ----
SUBJECTS = ["English", "Mathematics", "Computer", "Physics", "Urdu"]
MIN_MARK, MAX_MARK = 0, 100
PASS_MARK = 40                      # every subject must reach this mark
MAX_TOTAL = len(SUBJECTS) * MAX_MARK
GRADE_SCALE = [(90, "A+"), (80, "A"), (70, "B"), (60, "C"), (50, "D")]
PASS, FAIL = "Pass", "Fail"
CARD_WIDTH = 34


def format_name(name):
    """Remove outer spaces and capitalise each word."""
    return name.strip().title()


def get_valid_name():
    """Ask for a name until it is not empty; return the cleaned name."""
    while True:
        name = format_name(input("Student name: "))
        if name:
            return name
        print("Error: Name cannot be empty. Please try again.")


def get_valid_roll_number():
    """Ask for a roll number until it contains digits only."""
    while True:
        roll_number = input("Roll number: ").strip()
        if roll_number.isdigit() and roll_number.isascii():
            return roll_number
        print("Error: Roll number must contain digits only (no letters, spaces or symbols).")


def get_valid_marks(subject):
    """Ask for a whole number from MIN_MARK to MAX_MARK for one subject."""
    while True:
        text = input(f"{subject}: ").strip()
        try:
            if "_" in text:                 # int() would accept "1_0"; reject it
                raise ValueError
            marks = int(text)
        except ValueError:
            print(f"Error: Marks for {subject} must be a whole number.")
            continue
        if MIN_MARK <= marks <= MAX_MARK:
            return marks
        print(f"Error: Marks for {subject} must be between {MIN_MARK} and {MAX_MARK}.")


def calculate_percentage(total, max_total):
    """Return the overall percentage."""
    return total * 100 / max_total


def get_grade(percentage):
    """Return the letter grade for a percentage using GRADE_SCALE."""
    for minimum, grade in GRADE_SCALE:
        if percentage >= minimum:
            return grade
    return FAIL


def get_final_result(marks, percentage):
    """Return (grade, status). Any mark below PASS_MARK means Fail."""
    if not all(mark >= PASS_MARK for mark in marks):
        return FAIL, FAIL
    grade = get_grade(percentage)
    status = FAIL if grade == FAIL else PASS
    return grade, status


def display_result_card(name, roll_number, marks, total, percentage, grade, status):
    """Print the formatted result card."""
    line = "-" * CARD_WIDTH
    print("\n" + "=" * CARD_WIDTH)
    print("RESULT CARD".center(CARD_WIDTH).rstrip())
    print("=" * CARD_WIDTH)
    print(f"Student Name : {name}")
    print(f"Roll Number  : {roll_number}")
    print(line)
    for subject, mark in zip(SUBJECTS, marks):
        print(f"{subject:<12} : {mark}")
    failed = [f"{s} ({m})" for s, m in zip(SUBJECTS, marks) if m < PASS_MARK]
    if failed:
        print(f"{'Failed In':<12} : {', '.join(failed)}")
    print(line)
    print(f"Total Obtained: {total} / {MAX_TOTAL}")
    print(f"Percentage   : {percentage:.2f}%")
    print(f"Letter Grade : {grade}")
    print(f"Final Status : {status}")
    print("=" * CARD_WIDTH)


def main():
    print("=== Student Result Card Generator ===")
    try:
        name = get_valid_name()
        roll_number = get_valid_roll_number()
        marks = [get_valid_marks(subject) for subject in SUBJECTS]
    except EOFError:
        print("\nError: Input ended before all values were entered.")
        return
    total = sum(marks)
    percentage = calculate_percentage(total, MAX_TOTAL)
    grade, status = get_final_result(marks, percentage)
    display_result_card(name, roll_number, marks, total, percentage, grade, status)


if __name__ == "__main__":
    main()

# Python Functions and Lists Assessment

## Project Overview

This project contains two separate Python programs for practicing functions, string manipulation, lists, loops, validation, and basic class-result analysis.

## 1. Student Result Card Generator

File: `result_card_generator.py`

This program asks for one student's name, roll number, and marks in five subjects. It validates the roll number and marks, calculates the total and percentage, assigns a grade, and prints a formatted result card.

**Important result rule:** A student receives a final status of `Fail` if any subject mark is below 40, even if the overall percentage is high.

### Functions and concepts

- `get_valid_marks(subject)`: validates that marks are a whole number from 0 to 100.
- `calculate_percentage(total, max_total)`: calculates the overall percentage.
- `get_grade(percentage)`: returns the grade based on the given grading scale.
- `format_name(name)`: uses `strip()` and `title()` to clean the student's name.
- `get_valid_roll_number()`: uses `isdigit()` to accept digits only.
- `main()`: coordinates input, calculations, and result-card display.
- F-strings format the result card, and `all()` checks whether every subject mark is at least 40.

### Grading scale

| Percentage | Grade |
|---|---|
| 90 and above | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| Below 50 | Fail |

## 2. Class Marks Analyzer

File: `class_marks_analyzer.py`

This program collects each student's name and marks, then reports the class average, highest and lowest marks, students achieving those marks, pass/fail counts, students above average, and marks sorted from highest to lowest.

### Functions and concepts

- `get_valid_integer(prompt, minimum)`: validates the number of students.
- `get_valid_mark(student_name)`: validates marks from 0 to 100.
- `display_extreme_students(...)`: displays all students tied at the highest or lowest mark.
- `main()`: collects the class data and displays the analysis.
- `student_names` and `student_marks` are separate lists. `.append()` adds each entry.
- `len()`, `sum()`, `max()`, `min()`, and `sorted()` are used for analysis.
- Loops collect data and display above-average students.
- List comprehensions select students above average and students matching an extreme mark.

## Requirements

- Python 3.8 or later
- No external packages are required.

## How to Run

Open a terminal in the project folder.

Run the result card program:

```bash
python result_card_generator.py
```

Run the class marks analyzer:

```bash
python class_marks_analyzer.py
```

On some systems, use `python3` instead of `python`.

## Sample Input and Output

### Student Result Card Generator

Sample input:

```text
Student name:   aLI raza
Roll number: 1025
English: 85
Mathematics: 92
Computer: 88
Physics: 79
Urdu: 90
```

Sample result summary:

```text
Student Name : Ali Raza
Roll Number  : 1025
Total Obtained: 434 / 500
Percentage   : 86.80%
Letter Grade : A
Final Status : Pass
```

If any one subject is below 40, the final status and displayed letter grade are `Fail`.

### Class Marks Analyzer

Sample input:

```text
How many students are in the class? 4

Student 1
Name: Ayesha
Marks: 90

Student 2
Name: Bilal
Marks: 75

Student 3
Name: Hina
Marks: 90

Student 4
Name: Usman
Marks: 35
```

Sample output summary:

```text
Number of students : 4
Class average      : 72.50
Highest marks      : 90
Student(s) with highest marks: Ayesha, Hina
Lowest marks       : 35
Student(s) with lowest marks: Usman
Passing students   : 3
Failing students   : 1
Students above class average:
- Ayesha (90)
- Bilal (75)
- Hina (90)
Marks (highest to lowest): [90, 90, 75, 35]
```

## Input Validation

Both programs catch `ValueError` when a whole number is expected but the input cannot be converted to an integer. They also check numeric ranges and repeat the prompt when a value is outside the allowed range. The result-card program checks roll numbers with `isdigit()` so letters and symbols are rejected.

## Project Structure

```text
python-functions-lists-assessment/
├── result_card_generator.py
├── class_marks_analyzer.py
└── README.md
```

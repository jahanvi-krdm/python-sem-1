def calculate_sgpa(total_points, total_credit):
    assert total_credit > 0
    if total_credit > 0:
        return total_points / total_credit

sem = [] 
total_points = 0
total_credit = 0

grade_points = {
    "A+": 10, "A": 10, "A-": 9,
    "B+": 8, "B": 8, "B-": 7,
    "C+": 6, "C": 6, "C-": 5,
    "D": 4, "F": 2
}

while True:
    semester_input = input("Enter Course No., Credits, Grade (or press Enter to finish): ")
    if not semester_input:
        break  
    course_no, credits_str, grade = [item.strip() for item in semester_input.split(',')]
    if len([course_no, credits_str, grade]) != 3 or not credits_str.isdigit() or int(credits_str) not in [1, 2, 4]:
        print("Invalid input. Please enter in the format: Course No., Credits (1, 2, or 4), Grade.")
        continue
    credits = int(credits_str)
    if course_no.isupper() and course_no[-1].isdigit() and course_no.replace(" ", "").isalnum() and grade in grade_points:
        total_credit += credits
        total_points += credits * grade_points[grade]
    else:
        print(f"Invalid input for Course No. '{course_no}' or Grade '{grade}'.")


sgpa = calculate_sgpa(total_points, total_credit)

if sgpa:
    print(f"SGPA: {sgpa:.2f}")
else:
    print("No valid courses entered.")

def test_calculate_sgpa():
    assert calculate_sgpa(30, 3) == 10.0, "Test failed: SGPA should be 10.0"
    assert calculate_sgpa(45, 5) == 9.0, "Test failed: SGPA should be 9.0"
    assert calculate_sgpa(10,10) == 1.0, "test failed : sgpa should be 1.0"
test_calculate_sgpa()
    




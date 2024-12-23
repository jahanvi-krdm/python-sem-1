def assign_grade(total_marks, cutoffs):
    if total_marks >= cutoffs[0]:
        return 'A'
    elif total_marks >= cutoffs[1]:
        return 'B'
    elif total_marks >= cutoffs[2]:
        return 'C'
    elif total_marks >= cutoffs[3]:
        return 'D'
    else:
        return 'F'

def create_course():
    name = input("Course name: ")
    creds = int(input("Course credits: "))
    assessments = [
        (assessment_name := input("Assessment name: "), int(input(f"Weight for {assessment_name}: ")))
        for _ in range(int(input("Number of assessments: ")))
    ]
    cutoffs = [int(input(f"Grade cutoff for {grade}: ")) for grade in "ABCDF"]
    return {"name": name, "creds": creds, "assessments": assessments, "cutoffs": sorted(cutoffs, reverse=True), "students": {}}

def upload_marks(course, file):
    with open(file, 'r') as f:
        for line in f:
            data = line.strip().split(',')
            if len(data) != len(course["assessments"]) + 1:
                print(f"Skipping invalid line: {line.strip()}")
                continue

            roll_no = data[0]
            if not roll_no.isalnum():
                print(f"Invalid roll number: {roll_no}. Skipping.")
                continue

            marks = {course["assessments"][i][0]: float(data[i + 1]) for i in range(len(course["assessments"]))}
            total_marks = sum(marks[a[0]] * a[1] / 100 for a in course["assessments"])

            if total_marks > 100:
                print(f"Invalid total marks for {roll_no}. Skipping.")
                continue

            course["students"][roll_no] = {"marks": marks, "total": total_marks, "grade": assign_grade(total_marks, course["cutoffs"])}

def generate_summary(course):
    summary = f"Course: {course['name']} | Credits: {course['creds']}\n"
    summary += "Assessments:\n" + "".join(f"  {a[0]} - {a[1]}%\n" for a in course["assessments"])
    summary += "Grading Policy:\n" + "".join(f"  {grade}: {course['cutoffs'][i]}%\n" for i, grade in enumerate("ABCDF"))
    
    grading_summary = {grade: sum(1 for s in course["students"].values() if s["grade"] == grade) for grade in "ABCDF"}
    summary += "Grading Summary:\n" + "".join(f"  {grade}: {count}\n" for grade, count in grading_summary.items())
    
    return summary

def view_grades(course):
    for roll_no, student in course["students"].items():
        print(f"{roll_no}: {student['total']} marks - {student['grade']} grade")

def search_student(course, roll_no):
    student = course["students"].get(roll_no)
    if student:
        print(f"{roll_no}: Marks: {student['marks']} Total: {student['total']} Grade: {student['grade']}")
    else:
        print("Student not found.")

while True:
    course = create_course()
    file = input("Enter student marks file: ")
    upload_marks(course, file)

    print("\n1 > Generate Summary\n2 > View Grades\n3 > Save Grades\n4 > Search Student\nPress Enter to quit")
    
    choice = input("Enter your choice: ").strip()

    if choice == '1':
        print(generate_summary(course))
    elif choice == '2':
        view_grades(course)
    elif choice == '3':
        file = input("Enter filename to save grades: ")
        with open(file, 'w') as f:
            for roll_no, student in course["students"].items():
                f.write(f"{roll_no}, {student['total']}, {student['grade']}\n")
    elif choice == '4':
        roll_no = input("Enter roll number to search: ")
        search_student(course, roll_no)
    elif choice == '':
        break
    else:
        print("Invalid option. Please try again.")

def test_generate_summary():
    course_data = {
        "name": "Python 101",
        "creds": 3,
        "students": {
            "1": {"marks": {"Quiz": 10, "Assignment": 20}, "total": 30, "grade": "A"},
            "2": {"marks": {"Quiz": 15, "Assignment": 15}, "total": 30, "grade": "A"},
            "3": {"marks": {"Quiz": 5, "Assignment": 10}, "total": 15, "grade": "B"},
        }
    }
    assert generate_summary(course_data) == {
        "Course Name": "Python 101",
        "Credits": 3,
        "Grading Summary": {'A': 2, 'B': 1, 'C': 0, 'D': 0, 'F': 0}
    }
    assert generate_summary({"name": "Python 101", "creds": 3, "students": {}}) == {
        "Course Name": "Python 101",
        "Credits": 3,
        "Grading Summary": {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    }

test_generate_summary()


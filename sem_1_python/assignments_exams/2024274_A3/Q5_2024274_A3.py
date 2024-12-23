def get_grade(marks, cutoffs):
    grades = "ABCDF"
    for i in range(len(cutoffs)):
        if marks >= cutoffs[i]:
            return grades[i]
    return "F"

def create_course():
    name = input("Course name: ")
    creds = int(input("Course credits: "))
    
    assessments = []
    num_assessments = int(input("Number of assessments: "))
    for _ in range(num_assessments):
        a_name = input("Assessment name: ")
        a_weight = int(input(f"Weight for {a_name}: "))
        assessments.append((a_name, a_weight))

    policy = []
    for grade in "ABCDF":
        policy.append(int(input(f"Grade cutoff for {grade}: ")))

    cutoffs = sorted(policy, reverse=True)
    return {"name": name, "creds": creds, "assessments": assessments, "policy": policy, "cutoffs": cutoffs, "students": {}}

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

            marks = {}
            valid_data = True
            for i in range(len(course["assessments"])):
                try:
                    marks[course["assessments"][i][0]] = float(data[i + 1])
                except ValueError:
                    print(f"Invalid marks for {roll_no} in {course['assessments'][i][0]}. Skipping.")
                    valid_data = False
                    break

            if not valid_data:
                continue

            total_marks = 0
            total_weight = 0
            for i in range(len(course["assessments"])):
                weight = course["assessments"][i][1] / 100  
                total_marks += marks[course["assessments"][i][0]] * weight
                total_weight += weight

            if total_weight != 1:
                print("Error: The sum of assessment weights is not equal to 100%.")
                return

            grade = get_grade(total_marks, course["cutoffs"])
            course["students"][roll_no] = {"marks": marks, "total": total_marks, "grade": grade}

def generate_summary(course):
    summary = f"Course: {course['name']} | Credits: {course['creds']}\n"
    summary += "Assessments:\n"
    for a in course["assessments"]:
        summary += f"  {a[0]} - {a[1]}%\n"
    summary += "Grading Policy:\n"
    grades = "ABCDF"
    for i in range(len(course["policy"])):
        summary += f"  {grades[i]}: {course['policy'][i]}%\n"
    
    grading_summary = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for s in course["students"].values():
        grading_summary[s["grade"]] += 1
    
    summary += "Grading Summary:\n"
    for grade, count in grading_summary.items():
        summary += f"  {grade}: {count}\n"
    
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

        
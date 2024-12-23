class Student:
    def __init__(self, roll_no):
        self.roll_no = roll_no
        self.marks = {}
        self.total_marks = 0
        self.grade = 'F'

    def calculate_total(self, assessments):
        total_weighted_marks = 0
        for assessment, weight in assessments:
            total_weighted_marks += self.marks[assessment] * weight / 100
        self.total_marks = total_weighted_marks

    def assign_grade(self, grade_cutoffs):
        for grade, min_marks in grade_cutoffs:
            if self.total_marks >= min_marks:
                self.grade = grade
                return
        self.grade = 'F'


class Course:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits
        self.assessments = []
        self.grade_cutoffs = []
        self.students = {}

    def add_assessments(self, assessments):
        self.assessments = assessments

    def add_grade_cutoffs(self, cutoffs):
        self.grade_cutoffs = sorted(cutoffs, key=lambda x: -x[1])  

    def add_student(self, roll_no, marks):
        student = Student(roll_no)
        student.marks = marks
        student.calculate_total(self.assessments)
        student.assign_grade(self.grade_cutoffs)
        self.students[roll_no] = student

    def generate_summary(self):
        summary = {
            "Course Name": self.name,
            "Credits": self.credits,
            "Grading Summary": {grade: 0 for grade, _ in self.grade_cutoffs}
        }
        summary["Grading Summary"]['F'] = 0
        for student in self.students.values():
            summary["Grading Summary"][student.grade] += 1
        return summary

    def show_grades(self):
        for student in self.students.values():
            print(f"{student.roll_no}: {student.total_marks:.2f} marks - Grade: {student.grade}")

    def save_grades(self, filename):
        with open(filename, 'w') as file:
            for student in self.students.values():
                file.write(f"{student.roll_no}, {student.total_marks:.2f}, {student.grade}\n")


def create_course():
    name = input("Course name: ")
    credits = int(input("Course credits: "))
    course = Course(name, credits)
    
    num_assessments = int(input("How many assessments? "))
    assessments = []
    for _ in range(num_assessments):
        assessment_name = input("Assessment name: ")
        weight = int(input(f"Weight for {assessment_name}: "))
        assessments.append((assessment_name, weight))
    course.add_assessments(assessments)

    num_grades = int(input("How many grades do you want to define? "))
    grade_cutoffs = []
    for _ in range(num_grades):
        grade = input("Grade letter: ")
        min_marks = int(input(f"Minimum marks for {grade}: "))
        grade_cutoffs.append((grade, min_marks))
    course.add_grade_cutoffs(grade_cutoffs)

    return course


def upload_marks(course, file):
    with open(file, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            roll_no = data[0]
            marks = {course.assessments[i][0]: float(data[i + 1]) for i in range(len(course.assessments))}
            course.add_student(roll_no, marks)


course = create_course()
file_path = input("Enter the path for student data file: ")
upload_marks(course, file_path)

while True:
    print("\n1 > Generate Summary\n2 > View Grades\n3 > Save Grades\n4 > Search Student\nPress Enter to quit")
    choice = input("Choice: ").strip()

    if choice == '1':
        summary = course.generate_summary()
        for key, value in summary.items():
            print(f"{key}: {value}")
    elif choice == '2':
        course.show_grades()
    elif choice == '3':
        file_name = input("Enter the filename to save grades: ")
        course.save_grades(file_name)
    elif choice == '4':
        roll_no = input("Enter roll number to search: ")
        student = course.students.get(roll_no)
        if student:
            print(f"{student.roll_no}: Marks: {student.marks} Total: {student.total_marks:.2f} Grade: {student.grade}")
        else:
            print("Student not found.")
    elif choice == '':
        break
    else:
        print("Invalid choice. Try again.")
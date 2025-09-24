#Step 1: Student Class
class Student:
    def __init__(self, student_id, student_name, email, grades=None, courses=None):
        # Tuple → (id, name) for student basic info (immutable)
        self.id_name = (student_id, student_name)

        # String → email of student
        self.email = email

        # Dictionary → grades, default empty if not given
        self.grades = grades or {}

        # Set → courses enrolled, default empty if not given
        self.courses = courses or set()

    def __str__(self):
        # Return formatted string when printing student info
        return (f"ID: {self.id_name[0]}, Name: {self.id_name[1]}, "
                f"Email: {self.email}, "
                f"Courses: {', '.join(self.courses) if self.courses else 'None'}, "
                f"Grades: {self.grades if self.grades else 'None'}, "
                f"GPA: {self.calculate_gpa():.2f}")

    #Challenge 1: Calculate GPA
    def calculate_gpa(self):
        if not self.grades:  # No grades yet
            return 0.0

        total_points = 0
        for score in self.grades.values():
            # Convert score into GPA scale
            if score >= 90:
                total_points += 4.0
            elif score >= 80:
                total_points += 3.0
            elif score >= 70:
                total_points += 2.0
            elif score >= 60:
                total_points += 1.0
            else:
                total_points += 0.0

        # Average GPA = total points / number of subjects
        return total_points / len(self.grades)

#Step 2: StudentRecords Class
class StudentRecords:
    def __init__(self):
        # List → holds multiple Student objects
        self.students = []

    #Step 3: Add Student
    def add_student(self, student_id, student_name, email, grades=None, courses=None):
        self.students.append(Student(student_id, student_name, email, grades, courses))
        return "Student added successfully"

    #Step 4: Update Student
    def update_student(self, student_id, email=None, grades=None, courses=None):
        for student in self.students:
            if student.id_name[0] == student_id:
                if email:
                    student.email = email
                if grades:
                    student.grades.update(grades)  # merge dictionary
                if courses:
                    student.courses.update(courses)  # add into set
                return "Student updated successfully"
        return "Student not found"

    #Step 5: Delete Student
    def delete_student(self, student_id):
        for student in self.students:
            if student.id_name[0] == student_id:
                self.students.remove(student)
                return "Student deleted successfully"
        return "Student not found"

    #Step 6: Enroll in Course
    def enroll_course(self, student_id, course):
        for student in self.students:
            if student.id_name[0] == student_id:
                student.courses.add(course)
                return f"{student.id_name[1]} enrolled in {course}"
        return "Student not found"

    #Step 7: Search Student by ID
    def search_student(self, student_id):
        for student in self.students:
            if student.id_name[0] == student_id:
                return str(student)
        return "Student not found"

    #Challenge 2: Search by Name (Partial Match)
    def search_by_name(self, name):
        results = []
        for student in self.students:
            if name.lower() in student.id_name[1].lower():  # case-insensitive search
                results.append(str(student))
        return results if results else ["No students found"]

#Testing the Program
if __name__ == "__main__":
    records = StudentRecords()

    # Add students
    print(records.add_student(1, "Lanz", "lanz@mail.com", {"Math": 92, "Physical": 87}, {"Math"}))
    print(records.add_student(2, "Ronan", "Ron@mail.com", {"Comp. Sci.": 74}, {"Comp. Sci."}))
    print(records.add_student(3, "Cortez", "cort@mail.com", {"IT": 59}, {"It"}))

    # Search student by ID
    print(records.search_student(1))  # Lanz with GPA
    print(records.search_student(2))  # Ronan with GPA

    # Update Bob’s info
    print(records.update_student(2, grades={"Comp. Sci.": 85}, courses={"Comp. Sci."}))
    print(records.search_student(2))  # GPA updated

    # Enroll Alice in English
    print(records.enroll_course(1, "IT"))
    print(records.search_student(1))

    # Delete Charlie
    print(records.delete_student(3))
    print(records.search_student(3))

    # Partial name search
    print("Search results for 'lanz':")
    for s in records.search_by_name("lanz"):
        print(s)
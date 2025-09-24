class Student:
    def __init__(self, student_id, student_name, email, grades=None, courses=None):
        """
        A Student object stores all details for one student.
        
        Attributes:
            id_name (tuple): (student_id, student_name) → immutable student info
            email (str): Student email
            grades (dict): {subject: score}, e.g., {"Math": 95, "English": 88}
            courses (set): Unique enrolled courses, e.g., {"Math", "Science"}
        """
        self.id_name = (student_id, student_name)  # Tuple for ID + Name
        self.email = email                        # String
        self.grades = grades or {}                # Dictionary (default empty)
        self.courses = courses or set()           # Set (default empty)

    def __str__(self):
        """
        Returns a clean, formatted string when printing a student.
        Useful for displaying search results.
        """
        return (f"ID: {self.id_name[0]}, Name: {self.id_name[1]}, "
                f"Email: {self.email}, "
                f"Courses: {', '.join(self.courses) if self.courses else 'None'}, "
                f"Grades: {self.grades if self.grades else 'None'}")

    #Challenge Feature 1: GPA Calculation
    def calculate_gpa(self):
        """
        Converts numeric scores into GPA values and computes average.
        Scale used:
            A = 90–100 → 4.0
            B = 80–89  → 3.0
            C = 70–79  → 2.0
            D = 60–69  → 1.0
            F = <60    → 0.0
        """
        if not self.grades:  # If no grades, GPA = 0
            return 0.0
        
        # Helper function to convert score → GPA
        def score_to_gpa(score):
            if score >= 90: return 4.0
            elif score >= 80: return 3.0
            elif score >= 70: return 2.0
            elif score >= 60: return 1.0
            else: return 0.0

        # Convert all grades into GPA and take average
        gpa_values = [score_to_gpa(score) for score in self.grades.values()]
        return round(sum(gpa_values) / len(gpa_values), 2)


#Step 2: Define the StudentRecords Class
class StudentRecords:
    def __init__(self):
        """
        StudentRecords manages multiple Student objects.
        Uses a LIST to hold Student objects.
        """
        self.students = []

    #Step 3: Add Student
    def add_student(self, student_id, student_name, email, grades=None, courses=None):
        """
        Creates a new Student object and stores it in the list.
        """
        self.students.append(Student(student_id, student_name, email, grades, courses))
        return "Student added successfully"

    #Step 4: Update Student
    def update_student(self, student_id, email=None, grades=None, courses=None):
        """
        Finds student by ID and updates only provided fields.
        """
        for student in self.students:
            if student.id_name[0] == student_id:
                if email:   # Update email if given
                    student.email = email
                if grades:  # Merge new grades into existing ones
                    student.grades.update(grades)
                if courses: # Add new courses into set (avoids duplicates automatically)
                    student.courses.update(courses)
                return "Student updated successfully"
        return "Student not found"

    #Step 5: Delete Student
    def delete_student(self, student_id):
        """
        Removes a student from the list by matching ID.
        """
        for student in self.students:
            if student.id_name[0] == student_id:
                self.students.remove(student)
                return "Student deleted successfully"
        return "Student not found"

    #Step 6: Enroll in a Course
    def enroll_course(self, student_id, course):
        """
        Enrolls a student into a course.
        Using a set ensures no duplicates.
        """
        for student in self.students:
            if student.id_name[0] == student_id:
                student.courses.add(course)
                return f"{student.id_name[1]} enrolled in {course}"
        return "Student not found"

    #Step 7: Search by ID
    def search_student(self, student_id):
        """
        Finds a student by ID and returns their info.
        """
        for student in self.students:
            if student.id_name[0] == student_id:
                return str(student)
        return "Student not found"

    #Challenge Feature 2: Search by Name
    def search_by_name(self, name):
        """
        Performs case-insensitive search by partial name.
        Example: 'ali' matches 'Alice Johnson'
        """
        matches = [str(s) for s in self.students if name.lower() in s.id_name[1].lower()]
        return matches if matches else "No matches found"

#Testing the system
if __name__ == "__main__":
    # Create a StudentRecords object
    records = StudentRecords()

    # Step 3: Add Students
    print(records.add_student(1, "Lanz Ronan Cortez", "lanz@gmail.com",
                              {"Math": 94, "Comp. Sci.": 91}, {"Math"}))
    print(records.add_student(2, "Lance Cortez", "lance@gmail.com"))

    # Step 7: Search Student by ID
    print("\n-- Search by ID --")
    print(records.search_student(1))  # Lanz

    # Step 4: Update Student
    print("\n-- Update Student --")
    print(records.update_student(2, grades={"IT": 75}, courses={"IT"}))

    # Step 6: Enroll in Course
    print("\n-- Enroll Course --")
    print(records.enroll_course(1, "IT"))

    # Challenge 2: Search by Name
    print("\n-- Search by Partial Name --")
    print(records.search_by_name("lanz"))

    # Challenge 1: GPA Calculation
    print("\n-- GPA Calculation --")
    student = records.students[0]  # Lanz
    print(f"{student.id_name[1]}'s GPA: {student.calculate_gpa()}")

    # Step 5: Delete Student
    print("\n-- Delete Student --")
    print(records.delete_student(2))
    print(records.search_student(2))  # Should say not found

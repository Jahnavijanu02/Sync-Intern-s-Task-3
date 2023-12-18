class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.attendance = set()
class AttendanceSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name):
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)

    def mark_attendance(self, student_id, date):
        if student_id in self.students:
            self.students[student_id].attendance.add(date)
            return f"Attendance marked for {self.students[student_id].name} on {date}."
        else:
            return "Student not found."

    def get_attendance(self, student_id):
        if student_id in self.students:
            return self.students[student_id].attendance
        else:
            return "Student not found."

# Function to get user input
def get_user_input(prompt):
    return input(prompt).strip()


# Example usage with user input
attendance_system = AttendanceSystem()

# Add students
num_students = int(get_user_input("Enter the number of students: "))
for _ in range(num_students):
    student_id = get_user_input("Enter student ID: ")
    name = get_user_input("Enter student name: ")
    attendance_system.add_student(student_id, name)

# Mark attendance
num_attendance = int(get_user_input("Enter the number of attendance records to mark: "))
for _ in range(num_attendance):
    student_id = get_user_input("Enter student ID for attendance: ")
    date = get_user_input("Enter date (YYYY-MM-DD): ")
    print(attendance_system.mark_attendance(student_id, date))

# Display attendance
student_id_to_check = get_user_input("Enter student ID to check attendance: ")
print("Attendance for", student_id_to_check + ":", attendance_system.get_attendance(student_id_to_check))

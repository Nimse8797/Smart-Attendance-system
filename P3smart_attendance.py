import datetime

class Student:
    def __init__ (self,roll_no,name):
        self.roll_no = roll_no
        self.name = name

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

class Classroom:
    def __init__(self, class_name):
        self.class_name = class_name
        self.students = [] #list
        self.attendance_record = {} #dictionary

    def add_student(self, student):
        self.students.append(student)

    def mark_attendance(self, present_roll_no, date=None):
        if date is None:
           date = datetime.date.today().isoformat()
        self.attendance_record[date] = present_roll_no
        print(f"Attendance marked for {date}")

    def generate_monthly_report(self):
        print(f"\nAttendance report for {self.class_name} is:")
        student_attendance={s.roll_no:0 for s in self.students} #initialise students attendance
        
        for date, present_list in self.attendance_record.items():
            for roll in present_list:
                if roll in student_attendance:
                   student_attendance[roll] += 1

        for student in self.students:
            days_present = student_attendance[student.roll_no]
            print(f"{student.name} ({student.roll_no}): {days_present} days present")

if __name__ == "__main__":
    teacher = Teacher("SSP", "Physics")
    classroom = Classroom("11-A")

    # Add Students
    classroom.add_student(Student(1, "Vaishnavi"))
    classroom.add_student(Student(2, "Nandini"))
    classroom.add_student(Student(3, "Rohan"))

    # Mark Attendance (simulate)
    classroom.mark_attendance([1, 3],"2025-04-21")  # Day 1: Vaishnavi and Rohan present
    classroom.mark_attendance([2, 3],"2025-04-22")  # Day 2: Nandini and Rohan present

    # Generate Report
    classroom.generate_monthly_report()


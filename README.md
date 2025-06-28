# 📘 Attendance Management System (Python OOP)

This is a simple Python project built using **Object-Oriented Programming (OOP)** concepts. It simulates an **attendance management system** for a classroom, allowing teachers to mark student attendance and generate monthly reports.

---

## 🚀 Features

- Add students to a classroom  
- Mark attendance for specific dates  
- Automatically uses today’s date if not provided  
- Generate monthly attendance reports showing how many days each student was present  
- Organized using OOP principles with `Student`, `Teacher`, and `Classroom` classes  

---

## 🧱 Class Structure

### `Student`
- **Attributes**: `roll_no`, `name`

### `Teacher`
- **Attributes**: `name`, `subject`

### `Classroom`
- **Attributes**:
  - `class_name`
  - `students`: list of `Student` objects
  - `attendance_record`: dictionary storing date-wise attendance
- **Methods**:
  - `add_student(student)`: Adds a student to the class
  - `mark_attendance(present_roll_no, date=None)`: Marks attendance for a given date (uses today's date if not given)
  - `generate_monthly_report()`: Displays total attendance for each student

---

## 🧪 Example Usage

```python
teacher = Teacher("SSP", "Physics")
classroom = Classroom("11-A")

# Add students
classroom.add_student(Student(1, "Vaishnavi"))
classroom.add_student(Student(2, "Nandini"))
classroom.add_student(Student(3, "Rohan"))

# Mark attendance on specific dates
classroom.mark_attendance([1, 3], "2025-04-21")
classroom.mark_attendance([2, 3], "2025-04-22")

# Generate attendance report
classroom.generate_monthly_report()
```

---

## ✅ Sample Output

```
Attendance marked for 2025-04-21
Attendance marked for 2025-04-22

Attendance report for 11-A is:
Vaishnavi (1): 1 days present
Nandini (2): 1 days present
Rohan (3): 2 days present
```

---

## 🖥️ How to Run

1. Save the code into a file, e.g., `attendance_system.py`  
2. Open your terminal or IDE  
3. Run the script using:

```bash
python attendance_system.py
```

---

## 📌 Future Improvements

- Add support for storing data in files or a database  
- GUI interface for marking and viewing attendance  
- CSV export of attendance reports  
- Option to edit or delete attendance records  

---

This is a great beginner project for learning classes, lists, dictionaries, and real-world OOP implementation in Python.

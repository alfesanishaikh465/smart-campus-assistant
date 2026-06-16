import sqlite3

conn = sqlite3.connect("campus.db")
cursor = conn.cursor()

# Sample Students
students = [
    ("Ahmed", "ahmed@gmail.com", "Computer Engineering", 8),
    ("Ali", "ali@gmail.com", "IT Engineering", 6),
    ("Sara", "sara@gmail.com", "Computer Engineering", 4)
]

cursor.executemany(
    "INSERT INTO students (name, email, department, semester) VALUES (?, ?, ?, ?)",
    students
)

# Sample Timetable
timetable = [
    ("Artificial Intelligence", "Dr. Khan", "Monday", "09:00", "10:00"),
    ("Machine Learning", "Dr. Patel", "Tuesday", "11:00", "12:00"),
    ("Database Systems", "Dr. Shah", "Wednesday", "10:00", "11:00")
]

cursor.executemany(
    "INSERT INTO timetable (subject, faculty, day, start_time, end_time) VALUES (?, ?, ?, ?, ?)",
    timetable
)

# Sample Assignments
assignments = [
    ("AI Project Report", "Artificial Intelligence", "2026-06-20"),
    ("ML Presentation", "Machine Learning", "2026-06-25")
]

cursor.executemany(
    "INSERT INTO assignments (title, subject, due_date) VALUES (?, ?, ?)",
    assignments
)

conn.commit()
conn.close()

print("Sample data inserted successfully!")
import sqlite3

conn = sqlite3.connect("campus.db")
cursor = conn.cursor()

# Students
print("\nStudents:")
cursor.execute("SELECT * FROM students")

for row in cursor.fetchall():
    print(row)

# Timetable
print("\nTimetable:")
cursor.execute("SELECT * FROM timetable")

for row in cursor.fetchall():
    print(row)

# Assignments
print("\nAssignments:")
cursor.execute("SELECT * FROM assignments")

for row in cursor.fetchall():
    print(row)

conn.close()
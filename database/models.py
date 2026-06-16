import sqlite3

conn = sqlite3.connect("campus.db")
cursor = conn.cursor()

# Students Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    department TEXT,
    semester INTEGER
)
""")

# Timetable Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS timetable (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT NOT NULL,
    faculty TEXT,
    day TEXT,
    start_time TEXT,
    end_time TEXT
)
""")

# Assignments Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS assignments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    subject TEXT,
    due_date TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully!")
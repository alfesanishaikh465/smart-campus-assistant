import sqlite3

def get_assignment_info():
    conn = sqlite3.connect("campus.db")
    cursor = conn.cursor()

    cursor.execute("SELECT title, due_date FROM assignments")
    assignments = cursor.fetchall()

    conn.close()

    if assignments:
        response = "Upcoming Assignments:\n"

        for title, due_date in assignments:
            response += f"- {title} (Due: {due_date})\n"

        return response

    return "No assignments found."


def get_timetable():
    conn = sqlite3.connect("campus.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT subject, faculty, day, start_time
        FROM timetable
    """)

    timetable = cursor.fetchall()

    conn.close()

    if timetable:
        response = "Class Timetable:\n"

        for subject, faculty, day, time in timetable:
            response += (
                f"- {subject} | "
                f"{faculty} | "
                f"{day} | "
                f"{time}\n"
            )

        return response

    return "No timetable data found."
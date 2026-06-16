from agents.faq_agent import (
    get_assignment_info,
    get_timetable
)

from agents.gemini_agent import ask_gemini

while True:
    print("\n===== Smart Campus Assistant =====")
    print("1. View Timetable")
    print("2. View Assignments")
    print("3. Ask Gemini")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print(get_timetable())

    elif choice == "2":
        print(get_assignment_info())

    elif choice == "3":
        question = input("Ask Gemini: ")
        print("\nGemini Answer:")
        print(ask_gemini(question))

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
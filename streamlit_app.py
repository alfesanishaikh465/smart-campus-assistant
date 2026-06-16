import streamlit as st
from agents.faq_agent import get_timetable, get_assignment_info
from agents.gemini_agent import ask_gemini

st.title("🎓 Smart Campus Assistant")

option = st.sidebar.selectbox(
    "Choose an option",
    ["View Timetable", "View Assignments", "Ask Gemini"]
)

if option == "View Timetable":
    st.subheader("📅 Timetable")
    st.write(get_timetable())

elif option == "View Assignments":
    st.subheader("📝 Assignments")
    st.write(get_assignment_info())

elif option == "Ask Gemini":
    st.subheader("🤖 Ask Gemini")
    question = st.text_input("Enter your question:")

    if st.button("Ask"):
        if question:
            answer = ask_gemini(question)
            st.success(answer)
        else:
            st.warning("Please enter a question.")
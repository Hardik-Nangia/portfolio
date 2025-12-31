import streamlit as st
from projects.file_organiser.organiser import run_app

st.set_page_config(page_title="My Portfolio", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio(
    "Go to",
    ["Home", "Skills", "Projects", "Contact"]
)

# HOME
if section == "Home":
    st.title("👋 Hi, I'm Hardik , a student") 
    st.write(
        "I am a student passionate about software development "
        "and problem-solving using Python and Java."
    )

# SKILLS
elif section == "Skills":
    st.header("🛠 Skills")
    col1, col2 = st.columns(2)
    with col1:
        st.write("- Python")
        st.write("- Java")
    with col2:
        st.write("- OOP")
        st.write("- Data Structures")

# PROJECTS
elif section == "Projects":
    st.header("📂 Projects")

    with st.expander("📁 File Organizer Tool"):
        st.write(
            "A production-level Python tool that automatically "
            "organizes files by extension."
        )
        run_app()

# CONTACT
elif section == "Contact":
    st.header("📫 Contact")
    st.write("📧 Email: your_email@example.com")
    st.write("🐙 GitHub: https://github.com/yourusername")

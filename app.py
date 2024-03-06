from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "My Resume.pdf"
profile_pic = current_dir / "assets" / "Maruf's Image.JPG"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Maruf Khan"
PAGE_ICON = ":wave:"
NAME = "Maruf Khan"
DESCRIPTION = """
Data Analyst Intern, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "mk7446683@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/contactmarukhan/",
    "GitHub": "https://github.com/",
    "Twitter": "https://twitter.com/MarufKh64948760",
}
PROJECTS = {
    "🏆 Prediction of Salary Based on Experience using Linear Regression": "https://github.com/Maruf-Ahmad-khan/Linear-Regression-Model-2",
    "🏆 House Price Prediction using Linear Regression": "https://github.com/Maruf-Ahmad-khan/Linear-Regression-Model-3",
    "🏆 Attendence System Using Computer Vision": "https://github.com/Maruf-Ahmad-khan/Attendence_System_Using_CV",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Data Analyst Intern extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Numpy, Streamlit, Flask), SQL
- 📊 Data Visulization: PowerBi, MS Excel, Plotly, Matplotlib, Seaborn
- 📚 Modeling: Logistic regression, linear regression, decition trees, Support Vector Machine
- 🗄️ Databases: Postgres,MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Analyst Intern | Upflairs Pvt Ltd **")
st.write("07/20222 - 09/2022 ")
st.write(
    """
- ► House Price Prediction
    Developed a machine learning model to predict the price of House based on Area.
- ► Developed a machine learning model to predict the placement of the students on
    the basis of their 10th, 12th and Last semester of engineering marks.
- ► Redesigned data model through iterations that improved predictions by 12%
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Data Analyst Intern| Upflairs Pvt Ltd**")
st.write("07/2023 - 10/2023")
st.write(
    """
- ► Movie Recommendation System 
    Developed a machine learning model that recommend the different movies.
- ► Book Recommendation System
    Developed a machine learning model that recommends the different books.

- ► Developed an attendance System using computer vision.
    Wat’s app Chat Analyzer
    Developed a model using machine learning to analyze the chat of any users on 
    Of Wat’sapp.    
""")


# --- JOB 3
st.write('\n')
st.write("🚧", "**Data Analyst Intern | Flipshope**")
st.write("02/2024 - Present")
st.write(
    """
- ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
- ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
- ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

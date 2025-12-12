import streamlit as st
from PIL import Image

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Sanjavi S | Portfolio", layout="wide")

# ---------------- CSS DESIGN ----------------
st.markdown("""
<style>
/* Smooth scrolling */
html { scroll-behavior: smooth; }

/* Background */
body { background: #f8f9fa; font-family: 'Arial', sans-serif; }

/* Navbar */
.navbar {
    display: flex;
    justify-content: center;
    gap: 40px;
    padding: 15px 20px;
    background: #ffffffcc;
    backdrop-filter: blur(10px);
    border-radius: 12px;
    margin-bottom: 40px;
    border: 1px solid #d4d4d4;
    position: sticky;
    top: 0;
    z-index: 100;
}
.navbar a {
    text-decoration: none;
    font-size: 18px;
    font-weight: 600;
    color: #333;
    transition: color 0.3s;
}
.navbar a:hover { color: #6c63ff; }

/* Section Titles */
.section-title {
    font-size: 32px;
    font-weight: 700;
    color: #6c63ff;
    margin-top: 50px;
    margin-bottom: 20px;
    text-align: center;
}

/* Contact Icons */
.contact-icons img {
    width: 40px;
    margin-right: 12px;
    cursor: pointer;
    transition: transform 0.3s ease;
}
.contact-icons img:hover { transform: scale(1.3); }

/* Gradient Resume Button */
.resume-btn {
    background: linear-gradient(90deg, #6c63ff, #9f7eff);
    color: white;
    padding: 10px 20px;
    border-radius: 12px;
    font-weight: 600;
    text-decoration: none;
}
.resume-btn:hover { opacity: 0.9; }
</style>
""", unsafe_allow_html=True)

# ---------------- NAVBAR ----------------
st.markdown("""
<div class="navbar">
<a href="#about">About</a>
<a href="#skills">Skills</a>
<a href="#projects">Projects</a>
<a href="#internships">Internships</a>
<a href="#education">Education</a>
<a href="#contact">Contact</a>
</div>
""", unsafe_allow_html=True)

# ---------------- HEADER / ABOUT ----------------
st.markdown("<div id='about'></div>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:
    img = Image.open("profile.jpg")  # put profile.jpg in same folder
    st.image(img, width=220)

with col2:
    st.title("Sanjavi S")
    st.write("Kurinjipadi, Cuddalore | CGPA: **8.9 / 10**")
    st.write("""
Highly skilled individual with strong programming skills, eager to contribute to dynamic team environments.  
Passionate about developing innovative solutions and leveraging technology to solve real-world problems.  
I love AI, web development, and real-world tech applications.
""")
    # Resume Button
    try:
        with open("resume.pdf", "rb") as f:
            st.download_button("📄 Download Resume", f, "Sanjavi_Resume.pdf", key="resume")
    except:
        st.warning("⚠️ Resume not found — upload `resume.pdf` in app folder")

    # Social Icons
    st.markdown("""
    <div class='contact-icons' style='margin-top:20px;'>
        <a href="https://www.linkedin.com/in/sanjavi-s-8b0496281" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png">
        </a>
        <a href="https://github.com/SANJU-SKETCH" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/733/733609.png">
        </a>
        <a href="mailto:sivakumarsanjavi2@gmail.com" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png">
        </a>
    </div>
    """, unsafe_allow_html=True)

# ---------------- SKILLS ----------------
st.markdown("<div id='skills' class='section-title'>Skills</div>", unsafe_allow_html=True)
cols = st.columns(3)
with cols[0]:
    st.markdown("**Programming:**\n- Python\n- Java\n- SQL\n- OOPS")
with cols[1]:
    st.markdown("**Web Tech:**\n- HTML\n- CSS\n- JavaScript\n- React")
with cols[2]:
    st.markdown("**Tools:**\n- Power BI\n- MySQL\n- Git\n- ML\n- Cloud")

# ---------------- PROJECTS ----------------
st.markdown("<div id='projects' class='section-title'>Projects</div>", unsafe_allow_html=True)

projects = [
    ("AI Recipe Maker", "Personalized meal suggestions using NLP.", "Python, SpaCy, NLP"),
    ("Mental Health Chatbot", "Emotion-aware chatbot using sentiment analysis.", "React, NLP, API"),
    ("Student Tracking App", "Displays student location on campus.", "Streamlit, Pandas"),
    ("Credit Card Fraud Detection", "ML model to detect fraud.", "Random Forest, XGBoost")
]

for title, desc, tech in projects:
    st.markdown(f"**{title}**\n{desc}\n_Tech Stack:_ {tech}\n\n")

# ---------------- INTERNSHIPS ----------------
st.markdown("<div id='internships' class='section-title'>Internships</div>", unsafe_allow_html=True)
internships = [
    ("Oasis Infobyte — Data Analytics with ML", "Jul 2024 – Aug 2024"),
    ("Ventures Pvt Ltd — Full Stack Developer", "Oct 2024 – Nov 2024")
]
for title, period in internships:
    st.write(f"**{title}**  |  {period}")

# ---------------- EDUCATION ----------------
st.markdown("<div id='education' class='section-title'>Education</div>", unsafe_allow_html=True)
st.write("""
**B.Tech — Information Technology**  
Dhanalakshmi Srinivasan Engineering College, Perambalur  
📅 2022 – 2026  |  CGPA: **8.9 / 10**
""")
st.write("""
**Higher Secondary Education**  
St. Paul Matric Higher Secondary School, Kurinjipadi  
📅 2020 – 2022  |  Percentage: **86%**
""")

# ---------------- CONTACT ----------------
st.markdown("<div id='contact' class='section-title'>Contact</div>", unsafe_allow_html=True)
st.write("📧 **Email:** sivakumarsanjavi2@gmail.com")
st.write("📱 **Phone:** 6374981585")
st.markdown("""
<div class='contact-icons'>
    <a href="https://www.linkedin.com/in/sanjavi-s-8b0496281" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png">
    </a>
    <a href="https://github.com/SANJU-SKETCH" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/733/733609.png">
    </a>
</div>
""", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""<hr><center>Made with ❤️ by <b>Sanjavi S</b></center>""", unsafe_allow_html=True)

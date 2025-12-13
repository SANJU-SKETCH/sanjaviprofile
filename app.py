import streamlit as st
from PIL import Image

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Sanjavi S | Portfolio", layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>
html { scroll-behavior: smooth; }

/* Navbar */
.navbar { display:flex; justify-content:center; gap:36px; padding:16px; background:#fff; border-radius:14px; margin-bottom:40px; border:1px solid #e5e7eb; position:sticky; top:0; z-index:100; }
.navbar a { text-decoration:none; font-size:17px; font-weight:700; color:#1f2937; }
.navbar a:hover { color:#4f46e5; }

/* Section title */
.section-title { font-size:36px; font-weight:900; color:#4f46e5; margin-top:80px; margin-bottom:35px; text-align:center; }

/* Profile image */
.profile-img img { border-radius:50%; border:5px solid #4f46e5; }

/* About text */
.about-text { 
    font-size:18px; 
    line-height:1.85; 
    color:#f5f5f5;  /* light color for dark background */
    font-weight:600; 
}

/* Skill card for each category */
.skill-card {
    background: #ffffff;       /* white background for clear visibility */
    padding: 15px 10px;
    border-radius: 14px;
    margin-bottom: 10px;
    font-weight: 700;
    text-align: center;
    color: #1f2937;
}

/* Pills for each skill */
.skill {
    background: #eef2ff;      /* light purple/blue */
    color: #3730a3;           /* dark text */
    padding: 6px 14px;
    border-radius: 20px;
    margin: 4px 4px 4px 0;    /* horizontal spacing */
    display: inline-block;    /* horizontal alignment */
    font-weight: 600;
    text-align: center;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.skill:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 10px rgba(79,70,229,0.2);
}

/* Line wrapper for pills */
.skill-line {
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-start;
}

/* Cards (Projects, Internships, Education, Contact) */
.card { background:#fff; border-radius:18px; padding:26px 30px; margin-bottom:28px; border:1px solid #e5e7eb; box-shadow:0 10px 25px rgba(0,0,0,0.08); color:#111827; }
.card:hover { transform:translateY(-6px); box-shadow:0 16px 34px rgba(79,70,229,0.18); transition:0.3s; }

/* Project text */
.project-title { font-size:22px; font-weight:800; color:#312e81; }
.project-desc { font-size:16px; color:#1f2937; line-height:1.6; }
.project-tech { font-size:14px; font-weight:700; color:#4f46e5; }

/* Contact box */
.contact-box { background:#fff; border-radius:18px; padding:26px 30px; border:1px solid #e5e7eb; margin-bottom:30px; color:#111827; }

/* Icons */
.contact-icons img { width:42px; margin:0 12px; transition:transform 0.3s ease; }
.contact-icons img:hover { transform:scale(1.25); }

/* Buttons */
.stDownloadButton>button, .hire-btn { background: linear-gradient(90deg,#4f46e5,#7c3aed); color:white; border-radius:14px; padding:12px 26px; font-weight:800; border:none; }
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

# ---------------- ABOUT ----------------
st.markdown("<div id='about'></div>", unsafe_allow_html=True)
col1, col2 = st.columns([1, 3])
with col1:
    try:
        img = Image.open("profile.jpg")
        st.image(img, width=220)
    except:
        st.warning("Upload profile.jpg in your folder")
with col2:
    st.markdown("## Sanjavi S")
    st.markdown("📍 Kurinjipadi, Cuddalore | 🎓 CGPA: **8.9 / 10**")
    st.markdown("""
    <div class="about-text">
    Aspiring <b>Data Analyst</b> with hands-on experience in Python, SQL, Power BI, and Excel.<br>
    Passionate about transforming raw data into meaningful insights and actively seeking real-time projects.<br>
    Quick learner, analytical, and motivated to work on real-world data-driven problems.
    </div>
    """, unsafe_allow_html=True)

# Resume + Hire Me
col1, col2 = st.columns(2)
with col1:
    try:
        with open("resume.pdf","rb") as f:
            st.download_button("📄 Download Resume", f)
    except:
        st.warning("Upload resume.pdf")
with col2:
    st.markdown("<a href='#contact'><button class='hire-btn'>💼 Hire Me</button></a>", unsafe_allow_html=True)

# Social Icons
st.markdown("""
<div class='contact-icons' style='margin-top:20px;'>
    <a href="https://www.linkedin.com/in/sanjavi-s-8b0496281" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png">
    </a>
    <a href="https://github.com/SANJU-SKETCH" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/733/733609.png">
    </a>
    <a href="mailto:sivakumarsanjavi2@gmail.com">
        <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png">
    </a>
</div>
""", unsafe_allow_html=True)

# ---------------- SKILLS ----------------
st.markdown("<div id='skills' class='section-title'>Skills</div>", unsafe_allow_html=True)

skills = {
    "Programming": ["Python","Java","SQL","OOPS"],
    "Web Tech": ["HTML","CSS","JavaScript","React"],
    "Tools": ["Power BI","MySQL","Git","ML","Cloud"]
}

# Three columns for each skill category
col1, col2, col3 = st.columns(3)
columns = [col1, col2, col3]

for i, (category, items) in enumerate(skills.items()):
    with columns[i]:
        st.markdown(f"<div class='skill-card'><b>{category}</b></div>", unsafe_allow_html=True)
        skill_html = "".join([f"<div class='skill'>{skill}</div>" for skill in items])
        st.markdown(f"<div class='skill-line'>{skill_html}</div>", unsafe_allow_html=True)

# ---------------- PROJECTS ----------------
st.markdown("<div id='projects' class='section-title'>Projects</div>", unsafe_allow_html=True)
projects = [
    ("AI Recipe Maker","Developed an AI-based Recipe Recommendation system using Python and SpaCy providing personalized meal suggestions.","Python, SpaCy, NLP"),
    ("Mental Health Chatbot","Designed an intelligent mental health chatbot understanding user emotions with sentiment analysis.","Python, NLP, Sentiment Analysis"),
    ("Student Tracking App","Monitors and visualizes student location data in a campus environment.","Streamlit, Python, Pandas"),
    ("Credit Card Fraud Detection","ML model to detect fraudulent credit card transactions analyzing transaction patterns.","Python, Random Forest, XGBoost"),
    ("Women Safety Companion","Offline system detecting harassment or abuse emergencies via Python.","Python, Offline Processing")
]
for t,d,tech in projects:
    st.markdown(f"""
    <div class="card">
        <div class="project-title">{t}</div>
        <div class="project-desc">{d}</div>
        <div class="project-tech">Tech Stack: {tech}</div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- INTERNSHIPS ----------------
st.markdown("<div id='internships' class='section-title'>Internships</div>", unsafe_allow_html=True)
internships = [
    ("Oasis Infobyte","Data Analytics with ML","Jul – Aug 2024"),
    ("Ventures Pvt Ltd","Full Stack Developer Intern","Oct – Nov 2024")
]
for t,role,period in internships:
    st.markdown(f"""
    <div class="card">
        <div class="project-title">{t}</div>
        <div class="project-desc">{role}</div>
        <div class="project-tech">{period}</div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- EDUCATION ----------------
st.markdown("<div id='education' class='section-title'>Education</div>", unsafe_allow_html=True)
educations = [
    ("B.Tech – Information Technology","Dhanalakshmi Srinivasan Engineering College","2022 – 2026 | CGPA: 8.9"),
    ("Higher Secondary Education","St. Paul Matric Higher Secondary School","2020 – 2022 | 86%")
]
for degree, inst, period in educations:
    st.markdown(f"""
    <div class="card">
        <div class="project-title">{degree}</div>
        <div class="project-desc">{inst}</div>
        <div class="project-tech">{period}</div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- CONTACT ----------------
st.markdown("<div id='contact' class='section-title'>Contact</div>", unsafe_allow_html=True)
st.markdown("""
<div class="contact-box">
    <p>📧 sivakumarsanjavi2@gmail.com</p>
    <p>📱 6374981585</p>
    <p>📍 Cuddalore, Tamil Nadu</p>
</div>
""", unsafe_allow_html=True)

with st.form("contact_form"):
    st.subheader("Send a Message")
    st.text_input("Your Name")
    st.text_input("Your Email")
    st.text_area("Message")
    st.form_submit_button("Send Message")

# ---------------- FOOTER ----------------
st.markdown("""
<hr>
<center><b>Turning data into insights, and ideas into real-world impact.</b></center>
""", unsafe_allow_html=True)

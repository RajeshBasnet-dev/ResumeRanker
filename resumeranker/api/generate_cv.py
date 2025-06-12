from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

def create_cv_pdf(filename='Rajesh_Basnet_CV.pdf'):
    doc = SimpleDocTemplate(filename, pagesize=A4,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=72)

    styles = getSampleStyleSheet()
    styleH = styles['Heading1']
    styleN = styles['Normal']

    content = []

    # Header
    content.append(Paragraph("<b>Rajesh Basnet</b>", styleH))
    content.append(Paragraph("Butwal, Nepal", styleN))
    content.append(Paragraph("Phone: 9749782458 | Email: basnetrajesh245@gmail.com", styleN))
    content.append(Paragraph("LinkedIn: https://www.linkedin.com/in/rajesh-basnet-360188340/", styleN))
    content.append(Paragraph("GitHub: https://github.com/RajeshBasnet-dev", styleN))
    content.append(Spacer(1, 12))

    # Objective
    content.append(Paragraph("<b>Objective</b>", styles['Heading2']))
    objective_text = ("Passionate and detail-oriented entry-level Python developer eager to contribute to software development projects. "
                      "Skilled in Python programming, data structures, and building backend applications with Django. "
                      "Seeking opportunities to apply my coding skills and grow as a developer.")
    content.append(Paragraph(objective_text, styleN))
    content.append(Spacer(1, 12))

    # Skills
    content.append(Paragraph("<b>Skills</b>", styles['Heading2']))
    skills_text = (
        "- Programming Languages: Python (Proficient)<br/>"
        "- Web Frameworks: Django, Flask (Basics)<br/>"
        "- Databases: PostgreSQL, SQLite<br/>"
        "- Tools: Git, REST APIs, Postman<br/>"
        "- Libraries: Requests, pandas (Basic), pdfplumber<br/>"
        "- Concepts: Object-Oriented Programming, Data Structures, Algorithms<br/>"
        "- Version Control: Git/GitHub<br/>"
        "- Operating Systems: Windows, Linux (Basic)<br/>"
        "- Soft Skills: Problem Solving, Teamwork, Time Management"
    )
    content.append(Paragraph(skills_text, styleN))
    content.append(Spacer(1, 12))

    # Projects
    content.append(Paragraph("<b>Projects</b>", styles['Heading2']))
    projects_text = (
        "<b>ResumeRanker</b> (Python, Django, REST API)<br/>"
        "- Built a web app to upload resumes and rank them against job descriptions using NLP and TF-IDF similarity scoring.<br/>"
        "- Implemented PDF text extraction and score calculation to assist HR in shortlisting candidates.<br/>"
        "- Designed REST APIs for job description and resume upload, ranking, and retrieval.<br/><br/>"
        "<b>GitHub Activity Tracker</b> (Python, API integration)<br/>"
        "- Developed a Python script to fetch and analyze GitHub user activity data for productivity tracking.<br/>"
        "- Visualized user commit patterns using simple charts.<br/><br/>"
        "<b>Blogger API</b> (Python, Django REST Framework)<br/>"
        "- Created a RESTful API for a blogging platform with CRUD functionality and user authentication."
    )
    content.append(Paragraph(projects_text, styleN))
    content.append(Spacer(1, 12))

    # Education
    content.append(Paragraph("<b>Education</b>", styles['Heading2']))
    education_text = (
        "<b>Bachelor of Business Management (BMS)</b><br/>"
        "Lumbini Banijya Campus, Nepal<br/>"
        "Expected Graduation: 2027 (4th Semester)<br/><br/>"
        "<b>+2 Science</b><br/>"
        "Kanti Secondary School, Nepal<br/>"
        "Graduated: 2022"
    )
    content.append(Paragraph(education_text, styleN))
    content.append(Spacer(1, 12))

    # Certifications
    content.append(Paragraph("<b>Certifications</b>", styles['Heading2']))
    cert_text = (
        "- Python Django Certificate<br/>"
        "- Completed several Python backend and API development courses"
    )
    content.append(Paragraph(cert_text, styleN))
    content.append(Spacer(1, 12))

    # Languages
    content.append(Paragraph("<b>Languages</b>", styles['Heading2']))
    lang_text = "- English – Fluent<br/>- Nepali – Native"
    content.append(Paragraph(lang_text, styleN))
    content.append(Spacer(1, 12))

    # Additional Information
    content.append(Paragraph("<b>Additional Information</b>", styles['Heading2']))
    add_info = (
        "- Strong willingness to learn new technologies and frameworks.<br/>"
        "- Ability to work independently and collaboratively in a team.<br/>"
        "- Detail-oriented with excellent problem-solving skills."
    )
    content.append(Paragraph(add_info, styleN))

    doc.build(content)
    print(f"CV generated successfully as '{filename}'")

if __name__ == "__main__":
    create_cv_pdf()

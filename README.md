# 🎓 EduPath AI

> AI-Powered Student Risk Analysis System

EduPath AI is a Proof of Concept (POC) web application that helps teachers identify academically at-risk students using attendance and academic performance data. The system also provides students with personalized recommendations to improve their performance.

---

## 🚀 Features

### Teacher
- Secure Login
- Dashboard with student statistics
- Add, Edit, and Delete students
- Search and filter students
- View individual student reports
- Risk distribution chart

### Student
- Secure Login
- Personal dashboard
- Academic summary
- Attendance overview
- AI-generated risk level
- Personalized recommendations

### AI Risk Analysis
Students are classified into:
- 🟢 Low Risk
- 🟡 Medium Risk
- 🔴 High Risk

The current POC uses a rule-based risk analysis engine based on:
- Attendance
- Subject marks
- Overall average

---

## 🛠 Tech Stack

- Python
- Flask
- SQLAlchemy
- SQLite
- Bootstrap 5
- Plotly

---

## 📂 Project Structure

```
EduPath-AI/
│
├── ai/
├── templates/
├── utils/
├── instance/
├── app.py
├── models.py
├── requirements.txt
└── README.md
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/lavanyat170108-cell/EduPath-AI.git
```

Move into the project folder:

```bash
cd EduPath-AI
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 🔑 Default Teacher Login

| Username | Password |
|----------|----------|
| teacher | teacher123 |

Student accounts can be created from the Teacher Dashboard.

---

## 📌 Current Status

✅ Proof of Concept (POC v1.0)

Implemented:
- Unified Login System
- Teacher Dashboard
- Student Dashboard
- Student Management (CRUD)
- AI Risk Analysis
- Search & Filtering
- Dashboard Analytics
- Responsive User Interface

---

## 🚀 Future Improvements

- Machine Learning-based Risk Prediction
- Student Progress Tracking
- AI Study Planner
- PDF Report Generation
- Multi-Teacher Support
- Department-wise Analytics
- Email Notifications

---

## 👩‍💻 Developer

**Lavanya Thiyagarajan**

Developed as part of an AI Internship Project.

Version: **POC v1.0**
---

Overall, your README is **well-suited for the POC stage**. As we move into the MVP, we'll enrich it with screenshots, diagrams, and a demo section to make it stand out even more.


## 📄 License

This project is developed for educational and learning purposes.

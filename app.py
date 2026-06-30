from utils.charts import create_risk_chart
from ai.risk_engine import analyze_student
from models import db, Student
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

TEACHER_USERNAME = "teacher"
TEACHER_PASSWORD = "teacher123"

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == TEACHER_USERNAME and password == TEACHER_PASSWORD:
            return redirect(url_for("teacher_dashboard"))

        return "Invalid Username or Password"

    return render_template("login.html")


@app.route("/teacher")
def teacher_dashboard():

    students = Student.query.all()

    total_students = len(students)

    high_risk = 0
    medium_risk = 0
    low_risk = 0

    total_attendance = 0
    total_average_marks = 0

    for student in students:

        report = analyze_student(student)

        if report["risk"] == "High":
            high_risk += 1
        elif report["risk"] == "Medium":
            medium_risk += 1
        else:
            low_risk += 1

        total_attendance += student.attendance

        average_marks = (
            student.math_marks +
            student.science_marks +
            student.english_marks
        ) / 3

        total_average_marks += average_marks

    if total_students > 0:
        avg_attendance = round(total_attendance / total_students, 2)
        avg_marks = round(total_average_marks / total_students, 2)
    else:
        avg_attendance = 0
        avg_marks = 0
    risk_chart = create_risk_chart(
        high_risk,
        medium_risk,
        low_risk
    )
    return render_template(
        "teacher_dashboard.html",
        total_students=total_students,
        high_risk=high_risk,
        medium_risk=medium_risk,
        low_risk=low_risk,
        avg_attendance=avg_attendance,
        avg_marks=avg_marks,
        
        risk_chart=risk_chart
    )
@app.route("/add-student", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":
 
        name = request.form["name"]
        department = request.form["department"]
        year = int(request.form["year"])

        attendance = float(request.form["attendance"])

        math_marks = int(request.form["math_marks"])
        science_marks = int(request.form["science_marks"])
        english_marks = int(request.form["english_marks"])

        assignments_completed = int(request.form["assignments_completed"])
        late_submissions = int(request.form["late_submissions"])
        student = Student(
            name=name,
            department=department,
            year=year,
            attendance=attendance,
            math_marks=math_marks,
            science_marks=science_marks,
            english_marks=english_marks,
            assignments_completed=assignments_completed,
            late_submissions=late_submissions
        )

        db.session.add(student)
        db.session.commit()

        return redirect(url_for("teacher_dashboard"))

    return render_template("add_student.html")
@app.route("/students")
def students():

    students = Student.query.all()

    student_reports = []

    for student in students:
        report = analyze_student(student)

        student_reports.append({
            "student": student,
            "report": report
        })

    return render_template(
        "students.html",
        student_reports=student_reports
    )

if __name__ == "__main__":
    app.run(debug=True)
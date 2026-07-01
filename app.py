from utils.charts import create_risk_chart
from ai.risk_engine import analyze_student
from models import db, Student
from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = "edupath-secret-key"


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

        role = request.form["role"]
        username = request.form["username"]
        password = request.form["password"]

        if role == "teacher":

            if username == TEACHER_USERNAME and password == TEACHER_PASSWORD:

                session.clear()
                session["teacher"] = True

                return redirect(url_for("teacher_dashboard"))

        elif role == "student":

            student = Student.query.filter_by(
                roll_number=username,
                password=password
            ).first()

            if student:

                session.clear()
                session["student_id"] = student.id

                return redirect(url_for("student_dashboard"))

        return "Invalid Login Credentials"

    return render_template("login.html")


@app.route("/teacher")
def teacher_dashboard():
    if "teacher" not in session:
        return redirect(url_for("login"))

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
    if "teacher" not in session:
        return redirect(url_for("login"))
 
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
            roll_number = request.form["roll_number"],
            password = request.form["password"],
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
    if "teacher" not in session:
        return redirect(url_for("login"))
   
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
@app.route("/edit-student/<int:id>", methods=["GET", "POST"])
def edit_student(id):
    if "teacher" not in session:
         return redirect(url_for("login"))
  
    student = Student.query.get_or_404(id)

    if request.method == "POST":

        student.name = request.form["name"]
        student.department = request.form["department"]
        student.year = int(request.form["year"])

        db.session.commit()

        return redirect(url_for("students"))

    return render_template(
        "edit_student.html",
        student=student
    )
@app.route("/delete-student/<int:id>")
def delete_student(id):

    if "teacher" not in session:
        return redirect(url_for("login"))

    student = Student.query.get_or_404(id)

    db.session.delete(student)
    db.session.commit()

    return redirect(url_for("students"))
@app.route("/student-report/<int:id>")
def student_report(id):
    if "teacher" not in session:
        return redirect(url_for("login"))
 
    student = Student.query.get_or_404(id)

    report = analyze_student(student)

    return render_template(
        "student_report.html",
        student=student,
        report=report
    )

@app.route("/student-dashboard")
def student_dashboard():

    if "student_id" not in session:
        return redirect(url_for("login"))

    student = Student.query.get(session["student_id"])

    report = analyze_student(student)

    if report["risk"] == "Low":
        message = "Excellent work! Keep maintaining your performance."

    elif report["risk"] == "Medium":
        message = "You're doing well. A little more effort can make a big difference."

    else:
        message = "Don't worry. Every improvement starts with one step. Follow the recommendations and keep going!"

    return render_template(
        "student_dashboard.html",
        student=student,
        report=report,
        message=message
    )
@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))
if __name__ == "__main__":
    app.run(debug=True)
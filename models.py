from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    roll_number = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    attendance = db.Column(db.Float, default=100)

    math_marks = db.Column(db.Integer, default=0)
    science_marks = db.Column(db.Integer, default=0)
    english_marks = db.Column(db.Integer, default=0)

    assignments_completed = db.Column(db.Integer, default=0)
    late_submissions = db.Column(db.Integer, default=0)
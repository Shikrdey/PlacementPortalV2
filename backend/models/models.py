from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)
    role = db.Column(db.String, nullable = False) # Admin, Recruiter, Student
    created_at = db.Column(db.DateTime, default = lambda: datetime.now().replace(microsecond=0))

    student = db.relationship("Student", backref = "User", lazy = True, uselist = False, cascade = "all, delete-orphan") 
    recruiter = db.relationship("Recruiter", backref = "User", lazy = True, uselist = False, cascade = "all, delete-orphan")



class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key = True)
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False )
    
    name = db.Column(db.String(50), nullable = False)
    dob = db.Column(db.String(50), nullable = False)
    sex = db.Column(db.String(10), nullable = False)
    linkedin = db.Column(db.String(500), nullable = False, unique = True)
    department = db.Column(db.String(100), nullable = False)
    degree = db.Column(db.String(100), nullable = False)
    passing_year = db.Column(db.String(10), nullable = False)
    skills = db.Column(db.String, nullable = False)
    cgpa = db.Column(db.String(10), nullable = False)
    status = db.Column(db.String(15), nullable = False, default = "Active") # Active, Blocked

    application = db.relationship("Application", backref = "Student", lazy = True, cascade = "all, delete-orphan")


class Recruiter(db.Model):
    __tablename__ = "recruiters"

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    name = db.Column(db.String(100), nullable = False, unique = True)
    contact = db.Column(db.String(50), nullable = False, unique = True)
    website = db.Column(db.String(100), nullable = False, unique = True)
    ownership_type = db.Column(db.String(50), nullable = False)
    offering_type = db.Column(db.String(50), nullable = False)
    status = db.Column(db.String(15), nullable = False, default = "Pending") # Pending, Approved, Blocked
    
    drive = db.relationship("Drive", backref = "Recruiter", lazy = True, cascade = "all, delete-orphan")


class Drive(db.Model):
    __tablename__ = "drives"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    job_type = db.Column(db.String(50), nullable = False) 
    description = db.Column(db.String, nullable = False)
    eligibility = db.Column(db.String, nullable = False)
    ctc = db.Column(db.String(50), nullable = False)
    location = db.Column(db.String(100), nullable = False)
    deadline = db.Column(db.Date, nullable = False)
    status = db.Column(db.String(15), nullable = False, default = "Pending") # Pending, Ongoing, Closed, Rejected
    
    recruiter_id = db.Column(db.Integer, db.ForeignKey("recruiters.id"), nullable = False)
    
    application = db.relationship("Application", backref = "Drive", lazy = True, cascade = "all, delete-orphan")


class Application(db.Model):
    __tablename__ = "applications"

    id = db.Column(db.Integer, primary_key = True)
    date_applied = db.Column(db.Date, default=date.today)
    resume = db.Column(db.String(500), nullable = False, unique = True)
    status =  db.Column(db.String(15), nullable = False, default = "Applied") # Applied, Shortlisted, Accepted, Rejected
    
    drive_id = db.Column(db.Integer, db.ForeignKey("drives.id"), nullable = False)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable = False)

    __table_args__ = (db.UniqueConstraint("student_id", "drive_id", name = "Unique_application"),)
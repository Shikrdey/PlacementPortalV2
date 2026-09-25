from flask import Blueprint, jsonify, request, send_file
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.models import db, Student, Drive, Application
from tasks import export_applications_csv
from datetime import datetime
import os

student_bp = Blueprint("student", __name__)

@student_bp.route("/student/create/profile", methods = ["POST"])
@jwt_required()
def student_create_profile():
    data = request.get_json()
    user_id = int(get_jwt_identity())
    student = Student.query.filter_by(user_id=user_id).first()
    if student:
        return jsonify({"message":"Profile already exist"}), 409
    student = Student(
        user_id = user_id,
        name = data["name"],
        dob = data["dob"],
        sex = data["sex"],
        linkedin = data['linkedin'],
        department = data["department"],
        degree = data["degree"],
        passing_year = data["passing_year"],
        skills = data["skills"],
        cgpa = data["cgpa"]
    )
    db.session.add(student)
    db.session.commit()
    return jsonify({"message":"Profile added successfully"}), 200



@student_bp.route("/student/profile/check")
@jwt_required()
def student_profile_check():
    user_id = int(get_jwt_identity())
    student = Student.query.filter_by(user_id=user_id).first()
    if student:
        return jsonify({"profile":True}), 200
    return jsonify({"profile":False}), 200


@student_bp.route("/student/view/profile")
@jwt_required()
def view_profile():

    user_id = int(get_jwt_identity())

    student = Student.query.filter_by(user_id=user_id).first()

    if not student:
        return jsonify({"message":"Student not found"}), 404
    return jsonify({
        "name": student.name,
        "dob": student.dob,
        "linkedin": student.linkedin,
        "sex": student.sex,
        "department": student.department,
        "degree": student.degree,
        "passing_year": student.passing_year,
        "skills": student.skills,
        "cgpa": student.cgpa,
        "email": student.User.email,
        "joined_on": student.User.created_at,
    }), 200


@student_bp.route("/student/edit/profile", methods = ["PUT"])
@jwt_required()
def student_edit_profile():

    data = request.get_json()
    user_id = int(get_jwt_identity())
    student = Student.query.filter_by(user_id=user_id).first()
    
    if not student:
        return jsonify({"message":"Student not found"}), 404

    student.name = data["name"]
    student.dob = data["dob"]
    student.linkedin = data["linkedin"]
    student.sex = data["sex"]
    student.department = data["department"]
    student.degree = data["degree"]
    student.skills = data["skills"]
    student.passing_year = data["passing_year"]
    student.cgpa = data["cgpa"]

    db.session.commit()
    return jsonify({"message": "Profile edited successfully"}), 200


@student_bp.route("/student/dashboard")
@jwt_required()
def student_dashboard():

    user_id = int(get_jwt_identity())
    drives = Drive.query.filter_by(status = "Ongoing").all()
    applications = Application.query.filter_by(student_id = (Student.query.filter_by(user_id=user_id).first()).id).all()
    drives_id = [application.drive_id for application in applications]

    data = []

    for drive in drives:
        if drive.Recruiter.status != "Blocked" :
            if drive.id not in drives_id:
                data.append({
                    "id": drive.id,
                    "title": drive.title,
                    "deadline": datetime.strftime((drive.deadline), "%d-%m-%Y"),
                    "recruiter": drive.Recruiter.name
                })

    return jsonify({
        "drives": data
    }), 200

@student_bp.route("/student/load/drive/<int:id>")
@jwt_required()
def student_load_drive(id):

    user_id = int(get_jwt_identity())
    student = Student.query.filter_by(user_id=user_id).first()
    drive = Drive.query.filter_by(id = id).first()
    application = Application.query.filter_by(student_id = student.id, drive_id = drive.id).first()
    if application:
        return jsonify({
            "drive_id": drive.id,
            "title": drive.title,
            "job_type": drive.job_type,
            "description": drive.description,
            "eligibility": drive.eligibility,
            "ctc": drive.ctc,
            "location": drive.location,
            "deadline": datetime.strftime((drive.deadline), "%d-%m-%Y"),
            "status": application.status,
            "recruiter": drive.Recruiter.name,
            "resume": application.resume,
            "applied": True,
        })
    return jsonify({
        "drive_id": drive.id,
        "title": drive.title,
        "job_type": drive.job_type,
        "description": drive.description,
        "eligibility": drive.eligibility,
        "ctc": drive.ctc,
        "location": drive.location,
        "deadline": datetime.strftime((drive.deadline), "%d-%m-%Y"),
        "recruiter" : drive.Recruiter.name,
        "applied": False,
    })
    


@student_bp.route("/student/apply/drive/<int:id>", methods = ["POST"])
@jwt_required()
def student_apply_drive(id):

    data = request.get_json()
    user_id = int(get_jwt_identity())
    student = Student.query.filter_by(user_id = user_id).first()

    if not student:
        return jsonify({"message":"Student not found"}), 404
    drive = db.session.get(Drive, data["drive_id"])

    if not drive:
        return jsonify({"message":"Drive not found"}), 404

    if drive.status != "Ongoing":
        return jsonify({"message":"Drive is not available"}), 400

    existing_application = Application.query.filter_by(student_id = student.id, drive_id = drive.id).first()

    if existing_application:
        return jsonify({"message":"Already applied to this drive"}), 409

    application = Application(resume = data["resume"], drive_id = drive.id, student_id = student.id)
    db.session.add(application)
    db.session.commit()
    return jsonify({"message":"Application Submitted Successfully"}), 200


@student_bp.route("/student/applications/history")
@jwt_required()
def student_applications_history():

    user_id = int(get_jwt_identity())
    student = Student.query.filter_by(user_id= user_id).first()
    if not student:
        return jsonify({"message":"Student not found"}), 404
    applications = Application.query.filter_by(student_id = student.id).all()
    data = []

    for application in applications:
        data.append({
            "drive_id" : application.Drive.id,
            "title": application.Drive.title,
            "recruiter": application.Drive.Recruiter.name,
            "status": application.status
        })
    return jsonify({
        "name" : student.name,
        "applications": data
    }), 200



@student_bp.route("/student/export", methods= ["GET"])
@jwt_required()
def export():

    user_id = int(get_jwt_identity())
    export_applications_csv.delay(user_id)
    return jsonify({
        "message": "Export started"
    }), 202

@student_bp.route("/student/export/download", methods=["GET"])
@jwt_required()
def download_export():

    user_id = int(get_jwt_identity())
    file_path = f"exports/student_{user_id}.csv"
    if not os.path.exists(file_path):
        return jsonify({
            "message": "File not ready"
        }), 404

    return send_file(
        file_path,
        as_attachment=True,
        download_name=f"student_{user_id}_applications.csv",
        mimetype="text/csv"
    )
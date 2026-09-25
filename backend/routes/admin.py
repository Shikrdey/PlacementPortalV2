from flask import Blueprint, jsonify, request
from models.models import db, Student, Recruiter,Drive, Application, User
from datetime import datetime
from cache import cache
from flask_jwt_extended import jwt_required, get_jwt_identity

admin_bp = Blueprint("admin", __name__)



@admin_bp.route("/admin/dashboard")
@cache.memoize(timeout=15)
@jwt_required()
def admin_dashboard():
    total_students = Student.query.count()
    total_recruiters = Recruiter.query.filter(Recruiter.status != "Pending").count()
    total_drives = Drive.query.filter(Drive.status != "Pending").count()
    total_applications = Application.query.count()
    recruiters_pending = Recruiter.query.filter_by(status = "Pending").all()
    drives_pending = Drive.query.filter_by(status = "Pending").all()

    pending_drives = []
    pending_recruiters = []

    for drive in drives_pending:
        pending_drives.append({
            "id": drive.id,
            "recruiter": drive.Recruiter.name,
            "title": drive.title,
            "status": drive.status,
            "deadline": datetime.strftime((drive.deadline), "%d-%m-%Y")
        })

    for recruiter in recruiters_pending:
        pending_recruiters.append({
           "id": recruiter.id,
            "name": recruiter.name,
            "email": recruiter.User.email,
            "status": recruiter.status,
            "joined": datetime.strftime((recruiter.User.created_at), "%d-%m-%Y")
        })

    return jsonify({
        "total_students": total_students,
        "total_recruiters": total_recruiters,
        "total_drives": total_drives,
        "total_applications": total_applications,
        "pending_recruiters": pending_recruiters,
        "pending_drives": pending_drives
    }), 200



@admin_bp.route("/admin/view/all/recruiters")
@cache.memoize(timeout=5)
@jwt_required()
def view_all_recruiters():
    recruiters = Recruiter.query.filter(Recruiter.status != "Pending").all()

    data = []

    for recruiter in recruiters:
        data.append({
            "id": recruiter.id,
            "name": recruiter.name,
            "email": recruiter.User.email,
            "status": recruiter.status,
            "joined": datetime.strftime((recruiter.User.created_at), "%d-%m-%Y")
        })

    return jsonify(data), 200


@admin_bp.route("/admin/view/recruiter/<int:id>")
@jwt_required()
def view_recruiter(id):
    recruiter = Recruiter.query.get(id)
    if not recruiter:
        return jsonify({"message":"Recruiter not found"}), 404
    return jsonify({
        "name": recruiter.name,
        "email": recruiter.User.email,
        "website": recruiter.website,
        "contact": recruiter.contact,
        "ownership_type": recruiter.ownership_type,
        "offering_type": recruiter.offering_type,
        "status": recruiter.status,
        "role": "Recruiter"
    }), 200


@admin_bp.route("/admin/approve/recruiter/<int:id>", methods = ["PUT"])
@jwt_required()
def admin_approve_recruiter(id):
    recruiter = Recruiter.query.get(id)
    if not recruiter:
        return jsonify({"message":"Recruiter not found"}), 404
    recruiter.status = "Approved"
    db.session.commit()
    return jsonify({"message":"Recruiter Approved Successfully"}), 200


@admin_bp.route("/admin/block/recruiter/<int:id>", methods = ["PUT"])
@jwt_required()
def admin_block_recruiter(id):
    recruiter = Recruiter.query.get(id)
    if not recruiter:
        return jsonify({"message":"Recruiter not found"}), 404
    recruiter.status = "Blocked"
    db.session.commit()

    return jsonify({"message":"Recruiter Blocked Successfully"}), 200



@admin_bp.route("/admin/view/all/students")
@cache.memoize(timeout=5)
@jwt_required()
def view_all_students():
    students = Student.query.all()

    data = []

    for student in students:
        data.append({
            "id": student.id,
            "name": student.name,
            "email": student.User.email,
            "status": student.status,
            "joined": datetime.strftime((student.User.created_at), "%d-%m-%Y")
        })

    return jsonify(data), 200


@admin_bp.route("/admin/view/student/<int:id>")
@jwt_required()
def view_student(id):
    student = Student.query.get(id)

    if not student:
        return jsonify({"message":"Student not found"}), 404

    return jsonify({
        "name": student.name,
        "email": student.User.email,
        "dob": student.dob,
        "sex": student.sex,
        "linkedin": student.linkedin,
        "department": student.department,
        "degree": student.degree,
        "passing_year": student.passing_year,
        "skills": student.skills,
        "cgpa": student.cgpa,
        "status": student.status,
        "role": "Student"
    }), 200


@admin_bp.route("/admin/update/student/<int:id>", methods = ["PUT"])
@jwt_required()
def admin_student_block(id):
    data = request.get_json()
    student = Student.query.get(id)
    if not student:
        return jsonify({"message":"Student not found"}), 404
    student.status = data["status"]
    db.session.commit()
    return jsonify({"message":f"Student {data["status"]} Successfully"}), 200



@admin_bp.route("/admin/view/all/drives")
@cache.memoize(timeout=5)
@jwt_required()
def view_all_drives():
    drives = Drive.query.filter(Drive.status != "Pending").all()
    data = []
    for drive in drives:
        data.append({
            "id": drive.id,
            "recruiter": drive.Recruiter.name,
            "title": drive.title,
            "status": drive.status,
            "deadline": datetime.strftime((drive.deadline), "%d-%m-%Y")
        })

    return jsonify(data), 200


@admin_bp.route("/admin/view/drive/<int:id>")
@jwt_required()
def admin_view_drive(id):

    drive= Drive.query.get(id)
    if not drive:
        return jsonify({"message":"Drive not found"}), 404

    return jsonify({
        "id": drive.id,
        "recruiter": drive.Recruiter.name,
        "title": drive.title,
        "job_type": drive.job_type,
        "description": drive.description,
        "eligibility": drive.eligibility,
        "ctc": drive.ctc,
        "location": drive.location,
        "deadline": drive.deadline,
        "status": drive.status       
    }), 200


@admin_bp.route("/admin/approve/drive/<int:id>", methods = ["PUT"])
@jwt_required()
def admin_approve_drive(id):
    drive = Drive.query.get(id)
    if not drive:
        return jsonify({"message":"Drive not found"}), 404
    drive.status = "Ongoing"

    db.session.commit()
    return jsonify({"message":"Drive Approved Successfully"}), 200


@admin_bp.route("/admin/reject/drive/<int:id>", methods = ["PUT"])
@jwt_required()
def admin_reject_drive(id):
    drive = Drive.query.get(id)
    if not drive:
        return jsonify({"message":"Drive not found"}), 404
    drive.status = "Rejected"
    db.session.commit()
    return jsonify({"message":"Drive Rejected Successfully"}), 200

@admin_bp.route("/admin/close/drive/<int:id>", methods = ["PUT"])
@jwt_required()
def admin_close_drive(id):
    drive = Drive.query.get(id)
    if not drive:
        return jsonify({"message":"Drive not found"}), 404
    drive.status = "Closed"
    db.session.commit()
    return jsonify({"message":"Drive Rejected Successfully"}), 200


@admin_bp.route("/admin/view/all/applications")
@cache.memoize(timeout=5)
@jwt_required()
def admin_view_all_applications():

    applications = Application.query.all()
    data = []
    for application in applications:
        data.append({
            "id": application.id,
            "student_name": application.Student.name,
            "title": application.Drive.title,
            "status": application.status,
            "applied_at": application.date_applied
        })

    return jsonify(data), 200


@admin_bp.route("/admin/view/application/<int:id>")
@jwt_required()
def admin_view_application(id):
    application = Application.query.get(id)
    if not application:
        return jsonify({"message":"Application not found"}), 404

    return jsonify({
        "application_id": application.id,
        "student_name": application.Student.name,
        "student_email": application.Student.User.email,
        "recruiter_name": application.Drive.Recruiter.name,
        "recruiter_email": application.Drive.Recruiter.User.email,
        "drive_id": application.Drive.id,
        "title": application.Drive.title,
        "date_applied": application.date_applied,
        "resume": application.resume,
        "status": application.status
    }), 200

@admin_bp.route("/admin/delete/student/<int:student_id>", methods = ["DELETE"])
@jwt_required()
def delete_student(student_id):

    user_id = int(get_jwt_identity())
    if user_id == 1:
        student = Student.query.filter_by(id = student_id).first()
        if student:
            user = User.query.filter_by(id = student.user_id).first()
            db.session.delete(user)
            db.session.commit()
            return jsonify({
                "message":"Student Deleted!"
            }), 200
        return jsonify({
            "message":"Student not found"
        }), 404
    return jsonify({
        "message": "Unauthorised"
    }), 401


@admin_bp.route("/admin/delete/recruiter/<int:recruiter_id>", methods = ["DELETE"])
@jwt_required()
def delete_recruiter(recruiter_id):

    user_id = int(get_jwt_identity())
    if user_id == 1:
        recruiter = Recruiter.query.filter_by(id = recruiter_id).first()
        if recruiter:
            user = User.query.filter_by(id = recruiter.user_id).first()
            db.session.delete(user)
            db.session.commit()
            return jsonify({
                "message":"Recruiter Deleted!"
            }), 200
        return jsonify({
            "message":"Recruiter not found"
        }), 404
    return jsonify({
        "message": "Unauthorised"
    }), 401

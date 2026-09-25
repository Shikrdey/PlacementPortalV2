from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from models.models import db, Recruiter, Student, Drive, Application
from datetime import datetime


recruiter_bp = Blueprint("recruiter",__name__)



@recruiter_bp.route("/recruiter/create/profile", methods = ["POST"])
@jwt_required()
def recruiter_create_profile():
    data = request.get_json()
    user_id = int(get_jwt_identity())
    recruiter = Recruiter.query.filter_by(user_id=user_id).first()
    if recruiter:
        return jsonify({"message":"Profile already exists"}), 409
    recruiter = Recruiter(
        user_id = user_id,
        name = data["name"],
        contact = data["contact"],
        website = data["website"],
        ownership_type = data["ownership_type"],
        offering_type = data["offering_type"],
    )
    db.session.add(recruiter)
    db.session.commit()

    return jsonify({"message":"Profile added successfully"}),200


@recruiter_bp.route("/recruiter/profile/check")
@jwt_required()
def recruiter_profile_check():

    user_id = int(get_jwt_identity())
    recruiter = Recruiter.query.filter_by(user_id=user_id).first()
    if recruiter:
        return jsonify({"profile":True}),200
    return jsonify({"profile":False}), 200


@recruiter_bp.route("/recruiter/dashboard")
@jwt_required()
def recruiter_dashboard():
    user_id = int(get_jwt_identity())
    recruiter = Recruiter.query.filter_by(user_id = user_id).first()
    drives = Drive.query.filter_by(recruiter_id = recruiter.id).all()
    data = []
    for drive in drives:
        data.append({
            "id": drive.id,
            "title": drive.title,
            "status": drive.status
        })
    return jsonify(data), 200


@recruiter_bp.route("/recruiter/profile")
@jwt_required()
def recruiter_profile():
    user_id = int(get_jwt_identity())
    recruiter = Recruiter.query.filter_by(user_id = user_id).first()
    if not recruiter:
        return jsonify({"message":"Recruiter not found"}), 404
    return jsonify({

        "name": recruiter.name,
        "email": recruiter.User.email,
        "contact": recruiter.contact,
        "website": recruiter.website,
        "ownership_type": recruiter.ownership_type,
        "offering_type": recruiter.offering_type,
        "status": recruiter.status,
        "joined_on": recruiter.User.created_at
        
    }), 200


@recruiter_bp.route("/recruiter/edit/profile", methods = ["PUT"])
@jwt_required()
def recruiter_edit_profile():
    user_id = int(get_jwt_identity())
    recruiter = Recruiter.query.filter_by(user_id=user_id).first()
    if not recruiter:
        return jsonify({"message":"Recruiter not found"}), 404
    data = request.get_json()
    recruiter.name = data["name"]
    recruiter.contact = data["contact"]
    recruiter.website = data["website"]
    recruiter.ownership_type = data["ownership_type"]
    recruiter.offering_type = data["offering_type"]

    db.session.commit()    

    return jsonify({"message":"Profile edited Successfully"}), 200


@recruiter_bp.route("/recruiter/create_drive", methods = ["POST"])
@jwt_required()
def create_drive():

    data = request.get_json()
    user_id = int(get_jwt_identity())
    recruiter = Recruiter.query.filter_by(user_id = user_id).first()
    if not recruiter:
        return jsonify({"message": "Recruiter not found"}), 404

    if recruiter.status != "Approved":
        return jsonify({"message": "Recruiter is not approved by admin"}), 403

    drive = Drive(title = data["title"], job_type = data["job_type"], description = data["description"], eligibility = data["eligibility"], ctc = data["ctc"], location = data["location"], deadline = datetime.strptime(data["deadline"], "%Y-%m-%d"), recruiter_id = recruiter.id)

    db.session.add(drive)
    db.session.commit()

    return jsonify({"message":"Drive Added Successfully"}), 200


@recruiter_bp.route("/recruiter/drive/<int:id>")
@jwt_required()
def recruiter_drive(id):
    user_id = int(get_jwt_identity())
    recruiter = Recruiter.query.filter_by(user_id = user_id).first()
    drive = Drive.query.filter_by(recruiter_id = recruiter.id, id = id).first()

    if not drive:
        return jsonify({
            "message": "Drive not found"
        }), 404

    applications = Application.query.filter_by(drive_id = drive.id).all()

    data = []

    for application in applications:
        data.append({
            "application_id": application.id,
            "student_name": application.Student.name,
            "student_email": application.Student.User.email,
            "status": application.status
        })
    
    return jsonify({
        "title": drive.title,
        "job_type": drive.job_type,
        "description": drive.description,
        "eligibility": drive.eligibility,
        "ctc": drive.ctc,
        "location": drive.location,
        "deadline": datetime.strftime((drive.deadline), "%d-%m-%Y"),
        "status": drive.status,
        "applications": data,
        "role": recruiter.User.role
    }), 200

@recruiter_bp.route("/recruiter/update/drive/<int:drive_id>", methods = ["PUT"])
@jwt_required()
def recruiter_update_drive(drive_id):
    data = request.get_json()
    user_id = int(get_jwt_identity())
    drive = db.session.get(Drive, drive_id)
    if drive.Recruiter.User.id != user_id:
        return jsonify({"message":"Drive not found"}), 404

    drive.status = data["status"]
    db.session.commit()

    return jsonify({
        "message":"Drive updated Successfully"
    }), 200

@recruiter_bp.route("/recruiter/edit/drive/<int:id>", methods = ["PUT"])
@jwt_required()
def recruiter_edit_drive(id):
    user_id = int(get_jwt_identity())
    data = request.get_json()
    recruiter = Recruiter.query.filter_by(user_id=user_id).first()


    if recruiter:
        drive = db.session.get(Drive, id)
        if drive.recruiter_id == recruiter.id:
            if drive.status == "Pending":
                drive.title = data["title"]
                drive.job_type = data["job_type"] 
                drive.description = data["description"]
                drive.eligibility = data["eligibility"] 
                drive.ctc = data["ctc"] 
                drive.location = data["location"] 
                drive.deadline = datetime.strptime(data["deadline"], "%Y-%m-%d")

                db.session.commit()
                return jsonify({
                    "message": "Drive Updated"
                }), 200
    return jsonify({
        "message": "Drive not found"
    }), 404        
            



@recruiter_bp.route("/recruiter/view/all/applications/<int:drive_id>")
@jwt_required()
def recruiter_view_all_drive(drive_id):
    user_id = int(get_jwt_identity())
    drive = db.session.get(Drive, drive_id)
    if user_id != drive.Recruiter.User.id or drive.status == "Pending" or drive.status == "Rejected":
        return jsonify({
            "message": "Drive not found"
        }), 404
    applications = Application.query.filter_by(drive_id = drive.id ).all()
    data = []

    for application in applications:
        data.append({
            "application_id": application.id,
            "student_name": application.Student.name,
            "student_email": application.Student.User.email,
            "status": application.status
        })
    return jsonify({
        "data" : data,
        "drive_detail": {
        "drive_id": drive.id,
        "title": drive.title,
        "job_type": drive.job_type,
        "location": drive.location
    }
    }), 200


@recruiter_bp.route("/recruiter/application/<int:app_id>")
@jwt_required()
def recruiter_drive_application(app_id):
    user_id = int(get_jwt_identity())
    recruiter = Recruiter.query.filter_by(user_id=user_id).first()
    if not recruiter:
        return jsonify({"message":"Recruiter not found"}), 404

    application = Application.query.filter_by(id = app_id).first()

    if not application:
        return jsonify({
            "message":"Application not found"
        }), 404
    
    drive_id = application.drive_id
    drive_user_id = (Drive.query.filter_by(id = drive_id).first()).Recruiter.User.id
    if user_id != drive_user_id:
        return jsonify({"message":"Not allowed to view"}), 405

    return jsonify({
        "student_name": application.Student.name,
        "email": application.Student.User.email,
        "sex": application.Student.sex,
        "dob": application.Student.dob,
        "linkedin": application.Student.linkedin,
        "department": application.Student.department,
        "degree": application.Student.degree,
        "cgpa": application.Student.cgpa,
        "skills": application.Student.skills,
        "passing_year": application.Student.passing_year,
        "applied_at": application.date_applied,
        "resume": application.resume,
        "status": application.status,
        "drive_id": drive_id
    }), 200


@recruiter_bp.route("/recruiter/update/application/<int:application_id>", methods = ["PUT"])
@jwt_required()
def recruiter_update_application(application_id):
    data = request.get_json()
    user_id = int(get_jwt_identity())
    application = db.session.get(Application, application_id)
    drive_user_id = (Drive.query.filter_by(id = application.drive_id).first()).Recruiter.User.id
    if not application or drive_user_id != user_id:
        return jsonify({"message":"Application not found"}), 404
    application.status = data["status"]
    db.session.commit()

    return jsonify({"message":"Application updated successfully"}), 200

@recruiter_bp.route("/delete/drive/<int:id>", methods = ["DELETE"])
@jwt_required()
def delete_drive(id):

    user_id = int(get_jwt_identity())

    if user_id:
        drive = db.session.get(Drive, id)
        if drive.status == "Rejected":
            if drive.Recruiter.user_id == user_id:
                db.session.delete(drive)
                db.session.commit()
                return jsonify({"message":"Drive deleted successfully"}), 200
            return jsonify({"message": "Drive not found"}), 403
        return ({"message": "You can not delete this drive"}), 403
    return ({"message": "User not found"}), 404




from celery_config import celery
from models.models import Student, Application, Drive, User, db, Recruiter
from datetime import datetime, date
import csv
from utils.email_services import send_email

@celery.task
def export_applications_csv(user_id):
    student = Student.query.filter_by(user_id=user_id).first()
    applications = Application.query.filter_by(student_id=student.id).all()
    with open(f"exports/student_{user_id}.csv", "w", newline="") as file:

        writer = csv.writer(file)
        writer.writerow(["Student ID","Drive Title","Company Name","Application Status","Applied On"])

        for application in applications:
            writer.writerow([student.id,application.Drive.Recruiter.name,application.Drive.title,application.status,application.date_applied])
    print("CSV Generated Successfully")


@celery.task
def daily_reminder():
    drives = Drive.query.filter(Drive.status == "Ongoing").all()
    for drive in drives:
        students = Student.query.filter_by(status="Active").all()
        for student in students:
            applied = Application.query.filter_by(drive_id=drive.id,student_id=student.id).first()
            if applied:
                continue
            user = User.query.get(student.user_id)
            subject = f"Reminder: Application deadline for {drive.title}"
            body = f"""
Hello {student.name},
Just a quick reminder that the application deadline for "{drive.title}" position is {datetime.strftime((drive.deadline), "%d-%m-%Y")}. Please make sure to submit your application before the deadline.
We look forward to receiving your application.

Regards,
{drive.Recruiter.name}
Placement Portal
"""
            send_email(subject=subject,recipients=[user.email],body=body)
    print("Daily Reminder Completed")


@celery.task
def close_expired_drives():
    today = date.today()
    expired_drives = Drive.query.filter(Drive.deadline < today, Drive.status == "Ongoing").all()
    for drive in expired_drives:
        drive.status = "Closed"

    db.session.commit()


@celery.task
def monthly_report():
    total_students = Student.query.count()
    total_student_selected = Application.query.filter_by(status="Selected").count()
    total_student_rejected = Application.query.filter_by(status="Rejected").count()
    total_students_blocked = Student.query.filter_by(status= "Blocked").count()
    total_recruiters = Recruiter.query.count()
    total_recruiters_blocked = Recruiter.query.filter_by(status= "Blocked").count()
    total_drives = Drive.query.count()
    total_applications = Application.query.count()

    admins = User.query.filter_by(role="Admin").all()

    subject = "Monthly Placement Portal Report"
    body = f"""
Hello Admin,
Here is the monthly Placement Portal report:

Total Students: {total_students}
Total Students Selected: {total_student_selected}
Total Students Rejected: {total_student_rejected}
Total Students Blocked: {total_students_blocked}
Total Recruiters: {total_recruiters}
Total Recruiters Blocked: {total_recruiters_blocked}
Total Drives: {total_drives}
Total Applications: {total_applications}

Regards,
Placement Portal
"""
    for admin in admins:
        send_email(
            subject=subject,
            recipients=[admin.email],
            body=body
        )
    print("Monthly Report Sent Successfully")

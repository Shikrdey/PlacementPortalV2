# Placement Portal Application - V2

## 1. Project Overview

**Placement Portal Application (PPA) V2** is a single page web-based placement management system designed to simplify and automate the campus recruitment process for an institute.

The application provides a common platform for:

* **Admin (Institute Placement Cell)**
* **Companies / Recruiters**
* **Students**

The system manages company registrations, placement drives, student applications, application status, recruitment activities, and placement history.

It replaces manual processes such as spreadsheets, emails, and offline coordination with a centralized digital platform.

---

## 2. Objectives

The main objectives of the application are:

* Provide role-based access to Admin, Companies, and Students.
* Allow companies to register and create placement drives.
* Allow Admin to approve/reject companies and placement drives.
* Allow students to search and apply for eligible placement drives.
* Track applications and recruitment status.
* Maintain complete placement history.
* Provide automated reminders and monthly reports.
* Support asynchronous CSV export using Celery.
* Improve application performance using Redis caching.

---

## 3. Technology Stack

| Technology      | Purpose                             |
| --------------- | ----------------------------------- |
| **Flask**       | Backend REST API                    |
| **Vue.js**      | Frontend user interface             |
| **SQLite**      | Database                            |
| **SQLAlchemy**  | ORM and database operations         |
| **JWT**         | Authentication and authorization    |
| **Redis**       | Caching and Celery message broker   |
| **Celery**      | Background and scheduled jobs       |
| **Flask-Mail**  | Sending emails                      |
| **Vite**        | Vue development/build tooling       |
| **Axios**       | Communication between VueJS and API |
| **Google Sans** | UI typography / font                |


The database is created programmatically using SQLAlchemy model definitions. No manual database creation is required.

---

# 4. User Roles

The application has three main roles.

## 4.1 Admin

The Admin represents the institute placement cell.

There is only **one Admin**, and Admin registration is not allowed.

Admin can:

* View dashboard statistics.
* Approve or reject company registrations.
* Approve or reject placement drives.
* View all students.
* View all companies.
* View all placement drives.
* View student applications.
* Search students and companies.
* Blacklist/deactivate students and companies.

### Admin Dashboard

The dashboard displays information such as:

* Total Students
* Total Companies
* Total Placement Drives
* Total Placement Applications
* Pending Company Registrations
* Pending Placement Drives

---

# 5. Company / Recruiter Functionalities

Companies can register themselves on the platform.

After registration, the company profile remains pending until it is approved by the Admin.

### Company Features

* Register company profile.
* Login after registration.
* View company profile.
* Create placement drives after Admin approval.
* View created placement drives.
* View student applications.
* Shortlist students.
* Update application status.
* Update final selection results.

### Company Approval Flow

```text
Company Registration
        ↓
Pending Approval
        ↓
Admin Review
     ↙       ↘
Approved    Rejected
    ↓
Create Placement Drives
```

---

# 6. Student Functionalities

Students can register themselves and create their profiles.

### Student Features

* Register and login.
* Create/update student profile.
* Add academic details.
* Add skills and other profile information.
* Upload resume(drive link).
* View approved placement drives.
* Search placement drives and companies.
* Apply for placement drives.
* View application status.
* View placement/application history.
* Export application history as CSV.

### Student Application Flow

```text
View Approved Drive
        ↓
Eligibility Check
        ↓
Apply
        ↓
Applied
        ↓
Shortlisted / Rejected
        ↓
Selected / Rejected
```

---

# 7. Placement Drive

A **Placement Drive** represents a recruitment opportunity created by a company.

A placement drive can contain information such as:

* Drive ID
* Company ID
* Job Title
* Job Type
* Job Description
* Eligibility Criteria
* Branch/Department
* Minimum CGPA
* Passing Year
* CTC
* Location
* Application Deadline
* Status

### Drive Status

```text
Pending
   ↓
Approved
   ↓
Ongoing
   ↓
Closed
```

A drive can also be rejected by the Admin.

Expired drives are automatically closed using a scheduled background job.

---

# 8. Application Management

An **Application** represents a student's application to a placement drive.

Each application contains information such as:

* Application ID
* Student ID
* Drive ID
* Resume Link
* Application Date
* Application Status

### Application Status

```text
Applied
   ↓
Shortlisted
   ↓
Selected
```

An application can also be marked as **Rejected** during the recruitment process.

### Duplicate Application Prevention

A student cannot apply multiple times to the same placement drive.

This is enforced at the database/application level using a unique combination of:

```text
Student ID + Drive ID
```

---

# 9. Authentication and Authorization

The application uses **JWT-based authentication**.

After successful login:

```text
Login
  ↓
Credentials Verification
  ↓
JWT Token Generated
  ↓
Token Stored by Frontend
  ↓
Token Sent with API Requests
  ↓
Backend Validates Token
  ↓
Role-Based Access
```

The unified `User` model identifies the user's role:

```text
Admin
Recruiter
Student
```

Role-based authorization ensures that users can access only the APIs and pages permitted for their role.

---

# 10. Backend Scheduled Jobs

The application uses **Celery + Redis** for asynchronous and scheduled background processing.

## 10.1 Daily Reminder

A scheduled job runs daily and sends reminders to students about upcoming placement application deadlines.

The reminder can be sent using:

* Email

The job identifies relevant upcoming placement drives and students who have not yet applied.

---

## 10.2 Monthly Activity Report

A monthly report is generated automatically on the first day of every month.

The report contains placement activity such as:

* Number of placement drives
* Number of students who applied
* Number of students selected
* Other relevant placement statistics

The report is generated as HTML and sent to the Admin through email.

---

## 10.3 Export Applications as CSV

Students can export their placement application history from the dashboard.

The export is handled asynchronously using Celery.

The generated CSV contains:

```text
Student ID
Company Name
Drive Title
Application Status
Applied Date
```

### Export Flow

```text
Student clicks Export
        ↓
API triggers Celery task
        ↓
Celery generates CSV
        ↓
CSV stored in exports/
        ↓
Student receives completion alert
        ↓
Student downloads CSV
```

This prevents the API request from being blocked while the CSV is being generated.

---

# 11. Redis Caching

Redis is used for caching frequently requested data and improving API performance.

Examples of data suitable for caching include:

* Dashboard statistics
* Placement drive listings
* Search results
* Frequently accessed data

Cache entries have an expiry time so that stale data is automatically removed.

Example:

```text
API Request
    ↓
Check Redis Cache
   ↙        ↘
Found      Not Found
  ↓           ↓
Return     Query Database
Data          ↓
          Store in Redis
              ↓
          Return Data
```

---

# 12. Database Design

The application uses **SQLite** as the database.

The database is created programmatically using SQLAlchemy models.

Important entities include:

```text
User
 ├── Student
 └── Recruiter

Recruiter
 └── Drive

Student
 └── Application

Drive
 └── Application
```

### Main Tables

#### User

Stores authentication and role information.

#### Student

Stores student profile and academic information.

#### Recruiter

Stores company/recruiter profile and approval status.

#### Drive

Stores placement drive information.

#### Application

Stores student applications and recruitment status.

---

# 13. Project Structure

A typical project structure is:

```text
PlacementPortalV2/
│
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── cache.py
│   ├── celery_config.py
│   ├── celery_worker.py
│   ├── mail_config.py
│   ├── tasks.py
│   │
│   ├── models/
│   │   └── models.py
│   │
│   ├── routes/
│   │   ├── auth.py
│   │   ├── admin.py
│   │   ├── recruiter.py
│   │   └── student.py
│   │   
│   │
│   ├── utils/
│   │   └── email_services.py
│   │
│   ├── instance/
│   │   └── PPA_V2.db
│   │
│   ├── exports/
│   │   └── ...
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── assets/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── stores/
│   │   ├── router/
│   │   └── index.html
│   │
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

# 14. Application Architecture

The application follows a frontend-backend architecture:

```text
                 ┌─────────────────┐
                 │    Vue.js UI    │
                 └────────┬────────┘
                          │
                     HTTP / JSON
                          │
                          ▼
                 ┌─────────────────┐
                 │   Flask API     │
                 └───────┬─────────┘
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
     ┌─────────┐    ┌─────────┐   ┌──────────┐
     │ SQLite  │    │  Redis  │   │ Celery   │
     │Database │    │ Cache   │   │  Tasks   │
     └─────────┘    └─────────┘   └──────────┘
```

---

# 15. Installation and Setup

## Prerequisites

Install the following:

* Python 3.x
* Node.js and npm
* Redis
* Git

---

## Backend Setup

Navigate to the backend directory:

```bash
cd backend
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

---

## Start Redis

Start the Redis server:

```bash
redis-server
```

Verify that Redis is running:

```bash
redis-cli ping
```

Expected output:

```text
PONG
```

---

## Run Flask Backend

From the backend directory:

```bash
python app.py
```

The Flask API will run locally.

---

## Run Celery Worker

In another terminal:

Activate virtual environment:

```bash
source .venv/bin/activate
```

```bash
celery -A celery_worker.celery worker --loglevel=info
```

---

## Run Celery Beat

In another terminal:

Activate virtual environment:

```bash
source .venv/bin/activate
```

```bash
celery -A celery_worker.celery beat --loglevel=info
```

Celery Beat is responsible for triggering scheduled jobs.

---

# 16. Frontend Setup

Navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the Vue development server:

```bash
npm run dev
```

The frontend will be available through the local Vite development server.

---

# 17. Admin Account

Admin registration is not available through the application.

The Admin account is created programmatically after database creation.

This ensures that:

* There is only one Admin.
* Users cannot register themselves as Admin.
* Admin privileges are protected from normal user registration.

---

# 18. Security and Validation

The application implements:

* JWT authentication.
* Role-based authorization.
* Password hashing.
* Protected API routes.
* Duplicate application prevention.
* Company approval before drive creation.
* Admin-only management operations.
* Student/company activation and blocking controls.

---

# 19. Key Features Summary

### Admin

* Dashboard
* Company approval/rejection
* Placement drive approval/rejection
* Student management
* Company management
* Application management
* Search
* Blacklist/deactivation
* Reports and statistics

### Company

* Registration
* Company profile
* Placement drive creation
* Applicant management
* Student shortlisting
* Application status updates
* Selection management

### Student

* Registration/login
* Profile management
* Resume upload (drive link)
* Placement drive search
* Drive application
* Application tracking
* Placement history
* CSV export

### System

* JWT authentication
* Role-based access control
* SQLite database
* Redis caching
* Celery background jobs
* Daily reminders
* Monthly reports
* Async CSV export
* Automatic closing of expired drives

---

# 20. Conclusion

The **Placement Portal Application V2** provides a centralized platform for managing the complete campus placement lifecycle.

It connects the institute, recruiters, and students through role-based workflows while reducing manual coordination and improving application tracking.

The use of **Flask, Vue.js, SQLite, Redis, and Celery** provides a lightweight architecture suitable for local deployment while supporting authentication, caching, scheduled tasks, asynchronous processing, and placement management.

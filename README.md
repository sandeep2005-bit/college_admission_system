# 🎓 College Admission System

A web-based **College Admission Management System** developed using **Python Flask, MySQL, HTML, CSS, and JavaScript**. The system simplifies the student admission process by allowing students to register and administrators to manage and view admission information through a centralized application.

---

## 📌 Project Overview

The College Admission System is designed to digitally manage the college admission process.

The application provides:

- 👨‍🎓 Student registration
- 🔐 Student login
- 👨‍💼 Admin login
- 📋 Student details management
- 📄 Merit/allotment document management
- 🗓️ Academic year information
- 🗃️ MySQL database integration
- 📊 Admin dashboard
- 🔎 Student information viewing
- 🔒 Database-based authentication

---

## ✨ Features

### 👨‍🎓 Student Module

- Student registration
- Personal information submission
- Academic information submission
- Upload admission-related documents
- Academic year selection
- Secure login
- View admission information

### 👨‍💼 Admin Module

- Admin authentication
- Admin dashboard
- View registered students
- View student academic details
- View admission information
- Manage student records

### 🗄️ Database Module

- MySQL database
- Student records storage
- Admission information
- Academic details
- Document information
- Database relationships
- SQL queries
- Triggers
- Stored procedures

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend programming |
| Flask | Web framework |
| MySQL | Database |
| HTML5 | Web page structure |
| CSS3 | User interface design |
| JavaScript | Client-side functionality |
| XAMPP | MySQL/Apache environment |
| VS Code | Development environment |
| GitHub | Version control and repository |

---

## 🏗️ System Architecture

```text
                ┌─────────────────────┐
                │       Student       │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │    HTML / CSS / JS  │
                │    Frontend UI      │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │      Flask App      │
                │      app.py         │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │       MySQL         │
                │      Database       │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Admission Records   │
                │ Student Records     │
                └─────────────────────┘

# 📄 Form Automation with Python + PostgreSQL
# 📄 Automação de Formulários com Python + PostgreSQL

---

## 🇺🇸 English

### 📌 Project Overview
This project demonstrates an automated workflow using **Python**, **PostgreSQL**, and **PyAutoGUI** to process and fill forms automatically.

The system reads pending form data from a PostgreSQL database and automatically fills a form interface using desktop automation.

This project was built for portfolio purposes, showcasing database integration, automation, and clean project structure.

---

### Technologies Used

- Python 3
- PostgreSQL
- psycopg2
- PyAutoGUI
- SQL
- Git & GitHub

---

### How It Works

1. Form data is stored in a PostgreSQL database.
2. Python reads pending records.
3. Automation script fills forms automatically.
4. Processed records are updated in the database.

---

### Project Structure

src/
│
├── main.py # Main execution file
├── db.py # Database connection
├── read_forms.py # Reads pending forms
├── automation.py # Form automation logic
├── dbsetup.py # Reset database for testing
└── browser.py # Open forms for testing


---

### Installation

```bash
git clone https://github.com/YOUR_USERNAME/form-automation-python-postgresql.git
cd form-automation-python-postgresql

Create virtual environment:

python -m venv venv

Activate:

Windows:

venv\Scripts\activate
---
Install dependencies:

pip install -r requirements.txt
---
Database Setup

Create a PostgreSQL database and update credentials inside:

src/db.py
---

Run database setup:

python src/dbsetup.py

Run Project
python src/main.py

🎯 Purpose

This project demonstrates:

Database integration

Automation workflows

Python scripting

Real-world data processing




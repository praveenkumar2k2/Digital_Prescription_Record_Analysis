# Digital_Prescription_Record_Analysis

## 📌 Category
Data Engineering – Healthcare Informatics

---

## 📖 Project Description

The Digital Prescription Record Analysis system is a Python-based CLI tool designed to manage, clean, store, and analyze electronic medical prescriptions.

The system digitizes prescription management, enforces business validation rules, and provides analytical insights to improve healthcare decision-making and patient safety.

---

## 🎯 Objectives

- Digitize prescription management to reduce errors
- Enforce business rules and validation checks
- Maintain secure and normalized MySQL records
- Provide real-time analytical insights via CLI
- Detect abnormal prescribing patterns

---

## 🛠️ Tech Stack

- Python (Pandas, Matplotlib)
- MySQL
- SQL (Joins, Aggregations, Indexing)
- CLI (Menu-driven Interface)

---

## 🗂️ Project Architecture

CSV Files (Raw Data)
↓
Python ETL Pipeline

Data Cleaning

Null Handling

Deduplication

Business Rule Validation
↓
MySQL Database (Clean Tables)
↓
SQL Analytics Queries
↓
Matplotlib Dashboards (CLI)

---

## 🧱 Database Schema

### Tables:

- patients
- doctors
- medicines
- prescriptions

Includes:
- Primary Keys
- Foreign Keys
- Check Constraints
- Default Values
- Indexes for performance

---

## ✅ Business Rules Implemented

- Age must be between 0–100
- Duplicate prescriptions are rejected
- Invalid patient/doctor IDs are rejected
- Missing dosage/frequency → "Not Provided"
- Unknown gender → "U"
- Referential integrity via Foreign Keys

---

## 🔄 ETL Pipeline Features

- CSV ingestion
- Column standardization
- NaN to NULL conversion
- Duplicate removal
- Data validation
- Logging support
- Bulk insertion using executemany()

---

## 📊 Business Insights Implemented

1. Most Frequently Prescribed Medicines
2. Doctor-wise Prescription Volume Comparison
3. Gender-wise Prescription Distribution
4. Age Group vs Prescription Count
5. Anomaly Detection (Doctors with unusually high prescriptions)
6. Daily Prescription Trend Analysis
7. Data Quality Comparison (Raw vs Clean Data)

---

## 🖥️ CLI Menu Features

Users can interact via terminal:

1. Most Prescribed Medicines

2. Doctor-wise Volume

3. Gender Distribution

4. Age Group Analysis

5. Detect Unusual Doctors

6. Daily Trend

7. Data Quality Comparison

8. Exit

---

## 🚀 How to Run the Project

### Step 1: Create MySQL Database

Run the provided DDL script to create tables.

### Step 2: Install Dependencies

pip install pandas matplotlib mysql-connector-python

### Step 3: Run ETL

python etl_pipeline.py


### Step 4: Run CLI Analytics

python cli.py

---

## 📈 Sample Output

- Interactive bar charts
- Line trend analysis
- Statistical anomaly detection
- Data quality visualization

---

## 🔮 Future Enhancements

- Streamlit dashboard
- REST API integration
- Role-based authentication
- PDF report generation
- Cloud deployment (AWS/GCP)

---

## 👨‍💻 Developed By

Praveen Kumar  
Data Engineer Trainee  










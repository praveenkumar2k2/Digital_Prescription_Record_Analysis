import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="digital_prescription_db"
    )


def most_prescribed_medicines():
    conn = get_connection()
    query = """
    SELECT m.medicine_name, COUNT(*) as total
    FROM prescriptions p
    JOIN medicines m ON p.medicine_id = m.medicine_id
    GROUP BY m.medicine_name
    ORDER BY total DESC
    LIMIT 10;
    """
    df = pd.read_sql(query, conn)
    plt.figure()
    plt.bar(df['medicine_name'], df['total'])
    plt.xticks(rotation=45)
    plt.title("Most Frequently Prescribed Medicines")
    plt.show()
    conn.close()


def doctor_volume():
    conn = get_connection()
    query = """
    SELECT d.doctor_name, COUNT(*) as total
    FROM prescriptions p
    JOIN doctors d ON p.doctor_id = d.doctor_id
    GROUP BY d.doctor_name
    ORDER BY total DESC
    LIMIT 10;
    """
    df = pd.read_sql(query, conn)
    plt.figure()
    plt.bar(df['doctor_name'], df['total'])
    plt.xticks(rotation=45)
    plt.title("Doctor-wise Prescription Volume")
    plt.show()
    conn.close()


def gender_distribution():
    conn = get_connection()
    query = """
    SELECT p.gender, COUNT(*) as total
    FROM prescriptions pr
    JOIN patients p ON pr.patient_id = p.patient_id
    GROUP BY p.gender;
    """
    df = pd.read_sql(query, conn)
    plt.figure()
    plt.bar(df['gender'], df['total'])
    plt.title("Gender-wise Prescription Distribution")
    plt.show()
    conn.close()


def age_group_analysis():
    conn = get_connection()
    query = """
    SELECT CASE
            WHEN age < 18 THEN '0-17'
            WHEN age BETWEEN 18 AND 35 THEN '18-35'
            WHEN age BETWEEN 36 AND 50 THEN '36-50'
            WHEN age BETWEEN 51 AND 65 THEN '51-65'
            ELSE '65+'
        END AS age_group,
        COUNT(*) AS total_prescriptions
    FROM prescriptions pr
    JOIN patients p ON pr.patient_id = p.patient_id
    GROUP BY age_group;
    """
    df = pd.read_sql(query, conn)
    plt.figure()
    plt.bar(df['age_group'], df['total_prescriptions'])
    plt.title("Age Group vs Number of Prescriptions")
    plt.show()
    conn.close()


def anomaly_detection():
    conn = get_connection()
    query = """
    SELECT d.doctor_name, COUNT(*) as total_prescriptions
    FROM prescriptions p
    JOIN doctors d ON p.doctor_id = d.doctor_id
    GROUP BY d.doctor_name;
    """
    df = pd.read_sql(query, conn)
    threshold = df['total_prescriptions'].mean() + 2 * df['total_prescriptions'].std()
    unusual = df[df['total_prescriptions'] > threshold]
    print("Doctors issuing unusually high prescriptions:")
    print(unusual)
    conn.close()


def daily_trend():
    conn = get_connection()
    query = """
    SELECT DATE(prescribed_date) as date, COUNT(*) as total_prescriptions
    FROM prescriptions
    GROUP BY DATE(prescribed_date)
    ORDER BY date;
    """
    df = pd.read_sql(query, conn)
    plt.figure()
    plt.plot(df['date'], df['total_prescriptions'])
    plt.xticks(rotation=45)
    plt.title("Daily Prescription Trend")
    plt.show()
    conn.close()


def data_quality():
    raw_count = len(pd.read_csv("D:/databricks_projects/P1_digital_prescription_project/data/prescriptions_1000.csv"))

    conn = get_connection()
    clean_count = pd.read_sql("SELECT COUNT(*) as total FROM prescriptions;", conn)['total'][0]

    plt.figure()
    plt.bar(["Raw", "Clean"], [raw_count, clean_count])
    plt.title("Data Quality Improvement")
    plt.show()
    conn.close()

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

# Most Prescribed Medicines → Horizontal Bar Chart

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

    plt.figure(figsize=(8,6))
    plt.barh(df['medicine_name'], df['total'])
    plt.gca().invert_yaxis()
    plt.title("Top 10 Most Prescribed Medicines")
    plt.xlabel("Number of Prescriptions")
    plt.show()
    conn.close()

# Doctor Volume → Pie Chart (Top 5 Only)
def doctor_volume():
    conn = get_connection()
    query = """
    SELECT d.doctor_name, COUNT(*) as total
    FROM prescriptions p
    JOIN doctors d ON p.doctor_id = d.doctor_id
    GROUP BY d.doctor_name
    ORDER BY total DESC
    LIMIT 5;
    """
    df = pd.read_sql(query, conn)

    plt.figure(figsize=(6,6))
    plt.pie(df['total'], labels=df['doctor_name'], autopct='%1.1f%%')
    plt.title("Top 5 Doctors by Prescription Volume")
    plt.show()
    conn.close()
    
    
#Gender Distribution → Pie Chart
def gender_distribution():
    conn = get_connection()
    query = """
    SELECT p.gender, COUNT(*) as total
    FROM prescriptions pr
    JOIN patients p ON pr.patient_id = p.patient_id
    GROUP BY p.gender;
    """
    df = pd.read_sql(query, conn)

    plt.figure(figsize=(5,5))
    plt.pie(df['total'], labels=df['gender'], autopct='%1.1f%%')
    plt.title("Gender-wise Prescription Distribution")
    plt.show()
    conn.close()


# Age Group → Donut Chart
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

    plt.figure(figsize=(6,6))
    plt.pie(df['total_prescriptions'], labels=df['age_group'], autopct='%1.1f%%')
    
    # Donut effect
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    plt.title("Age Group Distribution")
    plt.show()
    conn.close()


#Anomaly Detection → Box Plot 
def anomaly_detection():
    conn = get_connection()
    query = """
    SELECT d.doctor_name, COUNT(*) as total_prescriptions
    FROM prescriptions p
    JOIN doctors d ON p.doctor_id = d.doctor_id
    GROUP BY d.doctor_name;
    """
    df = pd.read_sql(query, conn)

    plt.figure(figsize=(6,5))
    plt.boxplot(df['total_prescriptions'])
    plt.title("Prescription Distribution (Outlier Detection)")
    plt.ylabel("Number of Prescriptions")
    plt.show()

    threshold = df['total_prescriptions'].mean() + 2 * df['total_prescriptions'].std()
    unusual = df[df['total_prescriptions'] > threshold]

    print("Doctors issuing unusually high prescriptions:")
    print(unusual)

    conn.close()


# Daily Trends → Line Chart
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

# Data Quality → Side-by-Side Bar Chart (Raw vs Clean)
def data_quality():
    raw_count = len(pd.read_csv("D:/databricks_projects/P1_digital_prescription_project/data/prescriptions_1000.csv"))

    conn = get_connection()
    clean_count = pd.read_sql("SELECT COUNT(*) as total FROM prescriptions;", conn)['total'][0]

    plt.figure(figsize=(5,5))
    plt.bar(["Raw Data", "Clean Data"], [raw_count, clean_count])
    plt.title("Data Quality Improvement")
    plt.ylabel("Number of Records")
    plt.show()

    conn.close()

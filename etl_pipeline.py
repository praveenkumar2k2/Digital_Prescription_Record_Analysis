import pandas as pd
import mysql.connector
import logging

logging.basicConfig(
    filename="etl_log.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# =========================================================

def clean_patients(df):
    
    # Age validation

    df = df.copy()   # IMPORTANT

    df = df[(df['age'] >= 0) & (df['age'] <= 100)]

    df.loc[:, 'gender'] = df['gender'].fillna('U')
    df.loc[:, 'gender'] = df['gender'].apply(lambda x: x if x in ['M','F'] else 'U')

    df = df.drop_duplicates(subset=['patient_id'])
    
    logging.info("Patients cleaned successfully")

    return df

# =========================================================

def clean_prescriptions(df, patients_df, doctors_df, medicines_df):

    # Remove duplicate prescriptions
    df = df.drop_duplicates(subset=['prescription_id'])

    # Remove invalid patient IDs
    df = df[df['patient_id'].isin(patients_df['patient_id'])]

    # Remove invalid doctor IDs
    df = df[df['doctor_id'].isin(doctors_df['doctor_id'])]

    # Remove invalid medicine IDs
    df = df[df['medicine_id'].isin(medicines_df['medicine_id'])]

    # Handle missing dosage/frequency
    df['dosage'] = df['dosage'].fillna("Not Provided")
    df['frequency'] = df['frequency'].fillna("Not Provided")

    logging.info("Prescriptions cleaned successfully")
    return df
# =========================================================

def insert_data(table_name, df):

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="digital_prescription_db"
    )

    cursor = conn.cursor()

    # ✅ Remove extra spaces in column names
    df.columns = df.columns.str.strip()

    # ✅ Convert NaN to None (VERY IMPORTANT)
    df = df.astype(object).where(pd.notnull(df), None)

    columns = ", ".join(df.columns)
    placeholders = ", ".join(["%s"] * len(df.columns))

    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

    data = df.values.tolist()

    cursor.executemany(query, data)

    conn.commit()
    conn.close()

    print(f"{table_name} inserted successfully.")
    
    logging.info(f"Data inserted into {table_name} successfully")

# =========================================================

def run_etl():

    patients = pd.read_csv("D:/databricks_projects/P1_digital_prescription_project/data/patients_1000.csv")
    doctors = pd.read_csv("D:/databricks_projects/P1_digital_prescription_project/data/doctors_1000.csv")
    medicines = pd.read_csv("D:/databricks_projects/P1_digital_prescription_project/data/medicines_1000.csv")
    prescriptions = pd.read_csv("D:/databricks_projects/P1_digital_prescription_project/data/prescriptions_1000.csv")
    
    '''Debugging: Print column names to verify they match expected names'''
    '''  
    print("Columns:", medicines.columns.tolist())
    print("Columns:", doctors.columns.tolist())
    print("Columns:", patients.columns.tolist())
    print("Columns:", prescriptions.columns.tolist())
    '''
    
    # Clean data
    patients_clean = clean_patients(patients)
    prescriptions_clean = clean_prescriptions(
        prescriptions,
        patients_clean,
        doctors,
        medicines
    )
    
    # print(patients_clean.isnull().sum())
    # print(prescriptions_clean.isnull().sum())


    # Load to MySQL
    insert_data("patients", patients_clean)
    insert_data("doctors", doctors)
    insert_data("medicines", medicines)
    insert_data("prescriptions", prescriptions_clean)

    print("ETL Completed Successfully")
    
if __name__ == "__main__":
    run_etl()


-- ============================================
-- Business Insights Queries
-- ============================================

-- 1. Most Frequently Prescribed Medicines
SELECT m.medicine_name, COUNT(*) as total
FROM prescriptions p
JOIN medicines m ON p.medicine_id = m.medicine_id
GROUP BY m.medicine_name
ORDER BY total DESC
LIMIT 10;


-- 2. Doctor-wise Prescription Volume
SELECT d.doctor_name, COUNT(*) as total
FROM prescriptions p
JOIN doctors d ON p.doctor_id = d.doctor_id
GROUP BY d.doctor_name
ORDER BY total DESC;


-- 3. Gender-wise Prescription Distribution
SELECT p.gender, COUNT(*) as total
FROM prescriptions pr
JOIN patients p ON pr.patient_id = p.patient_id
GROUP BY p.gender;


-- 4. Age Group Analysis
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


-- 5. Detect Doctors with Unusually High Prescriptions
SELECT doctor_id, COUNT(*) as total
FROM prescriptions
GROUP BY doctor_id;


-- 6. Daily Prescription Trend
SELECT DATE(prescribed_date) as date,
       COUNT(*) as total_prescriptions
FROM prescriptions
GROUP BY DATE(prescribed_date)
ORDER BY date;


-- 7. Data Quality Check
SELECT COUNT(*) FROM prescriptions;

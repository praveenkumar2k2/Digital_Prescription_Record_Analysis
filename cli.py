import analytics


def menu():
    while True:
        print("\n===== Digital Prescription CLI =====")
        print("1. Most Prescribed Medicines")
        print("2. Doctor-wise Volume")
        print("3. Gender Distribution")
        print("4. Age Group Analysis")
        print("5. Detect Unusual Doctors")
        print("6. Daily Trend")
        print("7. Data Quality Comparison")
        print("8. Exit")


        choice = input("Enter your choice: ")

        if choice == "1":
            analytics.most_prescribed_medicines()
        elif choice == "2":
            analytics.doctor_volume()
        elif choice == "3":
            analytics.gender_distribution()
        elif choice == "4":
            analytics.age_group_analysis()
        elif choice == "5":
            analytics.anomaly_detection()
        elif choice == "6":
            analytics.daily_trend()
        elif choice == "7":
            analytics.data_quality()
        elif choice == "8":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()
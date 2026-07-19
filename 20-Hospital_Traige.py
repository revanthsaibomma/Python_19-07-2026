# 11. Hospital Triage Priority System
# Input:
# •	patient age
# •	oxygen level
# •	heart rate
# •	symptom severity
# Rules:
# •	Oxygen below threshold → Emergency
# •	Elderly patient with severe symptoms → High priority
# •	Mild symptoms → General queue
# •	Else medium priority

age = int(input("Enter Patient Age: "))
oxygen = float(input("Enter Oxygen Level (%): "))
heart_rate = int(input("Enter Heart Rate (bpm): "))
severity = input("Enter Symptom Severity (mild/moderate/severe): ").lower()

if oxygen < 90:
    print("Priority : Emergency")
    print("Reason : Oxygen level is below the safe threshold.")

elif age >= 60 and severity == "severe":
    print("Priority : High Priority")
    print("Reason : Elderly patient with severe symptoms.")

elif severity == "mild":
    print("Priority : General Queue")
    print("Reason : Symptoms are mild.")

else:
    print("Priority : Medium Priority")
    print("Reason : Patient requires further medical evaluation.")
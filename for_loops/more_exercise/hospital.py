period_of_days = int(input())

doctors = 7
treated_patients = 0
untreated_patients = 0

for day in range(1, period_of_days + 1):
    patients = int(input())

    if day % 3 == 0 and untreated_patients > treated_patients:
        doctors += 1

    if patients <= doctors:
        treated_patients += patients
    else:
        treated_patients += doctors
        untreated_patients += patients - doctors

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
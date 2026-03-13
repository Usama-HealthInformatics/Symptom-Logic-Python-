score = 0

print("Symptom Scoring System")

fever = input("Fever? (yes/no): ")
cough = input("Cough? (yes/no): ")
fatigue = input("Fatigue? (yes/no): ")
headache = input("Headache? (yes/no): ")

if fever == "yes":
    score += 2

if cough == "yes":
    score += 2

if fatigue == "yes":
    score += 1

if headache == "yes":
    score += 1

print("Your symptom score:", score)

if score >= 4:
    print("Possible condition: Flu or COVID-like illness")

elif score >= 2:
    print("Possible mild infection")

else:
    print("Low risk symptoms")

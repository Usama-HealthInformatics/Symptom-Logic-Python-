# Simple Symptom Diagnostic Logic

print("Welcome to the Symptom Checker")

fever = input("Do you have fever? (yes/no): ")
cough = input("Do you have cough? (yes/no): ")
headache = input("Do you have headache? (yes/no): ")

if fever == "yes" and cough == "yes":
    print("Possible condition: Flu or Viral Infection")

elif fever == "yes" and headache == "yes":
    print("Possible condition: Fever with Migraine or Infection")

elif cough == "yes":
    print("Possible condition: Cold or Respiratory Infection")

else:
    print("Condition unclear. Please consult a healthcare professional.")

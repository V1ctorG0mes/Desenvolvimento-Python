print("HEART RATE VERIFIER")

age = int(input("Please enter your age: "))
bpm = int(input("Please enter your heart rate: "))

if age <= 2:
    if bpm >= 120 and bpm <= 140:
        print("Adequate heart rate")
    else:
        print("Inadequate heart rate")
elif age >= 8 and age <= 17:
    if bpm >= 80 and bpm <= 100:
        print("Adequate heart rate")
elif age >= 18 and age <= 60:
    if bpm >= 70 and bpm <= 80:
        print("Adequate heart rate")
elif age >= 60:
    if bpm >= 50 and bpm <= 60:
        print("Adequate heart rate")
else:
    print("There is no data for the indicated age")
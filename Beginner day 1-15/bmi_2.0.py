height = float(input("Enter your height: "))
wight = float(input("Enter your wheight: "))

bmi = round(wight / (height / 100) **2)

if bmi < 18.5:
    print(f"Yor BMI is {bmi}, underweight")
elif bmi < 25:
    print(f"Yor BMI is {bmi}, normal")
elif bmi < 30:
    print(f"Yor BMI is {bmi}, over")
elif bmi < 35:
    print(f"Yor BMI is {bmi}, obese")
else:
    print(f"Yor BMI is {bmi}, clinical obese")

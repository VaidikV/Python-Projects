print("BMI calculator")
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))


calculating_bmi = weight / height ** 2 
bmi = round(calculating_bmi)


if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")




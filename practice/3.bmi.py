height=float(input("Enter your height in meters: "))
weight=float(input("Enter your weight in kg: "))
bmi=weight/(height**2)
if bmi<18.5:
    print(f"Your BMI is {bmi:.2f}, you are underweight.")
elif 18.5<=bmi<24.9:
    print(f"Your BMI is {bmi:.2f}, you have a normal weight.")
elif 25<=bmi<29.9:
    print(f"Your BMI is {bmi:.2f}, you are overweight.")
elif bmi>=30:
    print(f"Your BMI is {bmi:.2f}, you are obese.")
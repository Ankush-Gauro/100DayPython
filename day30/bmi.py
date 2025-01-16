height = float(input("Enter your height in m: "))
weight = int(input("Enter your weight in kg: "))

if height > 3:
    raise ValueError("Height is too high")

bmi = weight / (height * height)
print("Your BMI is: ", bmi)


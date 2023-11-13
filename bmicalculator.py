#KELVIN MWENDA
#SCT211-0062/2022

print("This is calculator calculates your bmi...")
weight = float(input("Enter your weight:"))
height = float(input("Enter your height: "))

#weight(kg)/height(m)
#underweight<18.5
#normal weight18.5-24.9
#overweight>25

bmi = float(weight/(height**2))
if bmi < 18.5:
    print("You are underweight!!")
elif bmi > 25:
    print("You are overweight!!")
else:
    print("You have a normal weight")
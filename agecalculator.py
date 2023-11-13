#KELVIN MWENDA
#SCT211-0062/2022

import datetime

print("This calculator calculates the age of a person...")
name = input("What is your name: ")
print("Wow, " + name + " is a great name.")


birth_year = int(input("Which year were you born: "))
if birth_year < 0 or birth_year > datetime.date.today().year:
            print("Invalid birth year")

current_date = datetime.date.today()
print(current_date)
birth_date = datetime.date (birth_year, 1, 1)# Assuming January 1st of the birth year
age = current_date - birth_date

years = age.days // 365
remaining_days = age.days % 365
months = remaining_days // 30  # Assuming an average of 30 days per month
days = remaining_days % 30


print(f"Your age is " ,years, " years, ", months, " months, and ", days, " days.")
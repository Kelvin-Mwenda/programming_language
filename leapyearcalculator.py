#KELVIN MWENDA
#SCT211-0062/2022
print("This calculator calculates whether the year entered is a leap year or not...")
year = int(input("Enter a year:"))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("A leap year")
else:
    print("Not a leap year")
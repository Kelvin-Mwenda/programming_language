#KELVIN MWENDA
#SCT211-0062/2022

print("This calculator calculates the total bill and divides the bill equally by a number of people...")
total_bill = float(input("Enter the total bill: "))
tip_rate = int(input("What is the percentage rate for the tip?(10,12 or 15)"))

if tip_rate is 10:
   tip_amount = float(10/100) * (total_bill)
elif tip_rate is 12:
    tip_amount = float(12/100) * (total_bill)
else:
    tip_amount = float(15/100) * (total_bill)
    
people_num = float(input("How many people are splitting the bill: "))

gross_bill = float(total_bill) + float(tip_amount)
each_person = float(gross_bill/people_num)
round_each = round(each_person, 2)

print("Each person should pay Ksh.",round_each)
#KELVIN MWENDA
#SCT211-0062/2022
import math
class calculate():
    def __init__(self,num1,num2):
        self.n1 = num1
        self.n2 = num2
        
    def sum(self):
        sum = int(self.n1) + int(self.n2)
        print(self.n1," + ",self.n2," = ",sum)
        
print("Hello,I am your simple calculator...")
number1 = input("Enter the first number:")
number2 = input("Enter the second number:")
result = calculate(number1,number2)
result.sum()

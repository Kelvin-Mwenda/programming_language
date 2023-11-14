#KELVIN MWENDA
#SCT211-0062/2022

class Calculator:
    def __init__(self, num1, num2):
        self.n1 = num1
        self.n2 = num2

    def calculate_sum(self):
        try:
            sum_result = int(self.n1) + int(self.n2)
            print(f"{self.n1} + {self.n2} = {sum_result}")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    print("Hello, I am your simple calculator...")
    
    while True:
        number1 = input("Enter the first number: ")
        number2 = input("Enter the second number: ")
        try:
            calculator = Calculator(number1, number2)
            calculator.calculate_sum()
        except Exception as e:
            print(f"An error occurred: {e}")

        choice = input("Do you wish to exit?[y/n]: ")
        if choice.lower() == 'n':
            break
        else:
            continue
        
        
        
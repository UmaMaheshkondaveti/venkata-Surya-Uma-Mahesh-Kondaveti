class Calculator:
    def calculate(self, a, b, operation):
        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '*':
            return a * b
        elif operation == '/':
            if b == 0:
                return "Can't divide by zero!"
            return a / b
        else:
            return "Unknown operation"


my_calc = Calculator()

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

answer = my_calc.calculate(a, b, op)
print(f"Result: {answer}")

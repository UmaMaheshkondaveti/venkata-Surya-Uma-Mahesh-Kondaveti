class Calculator:
    def __init__(self, num1: float, num2: float, operation: str):
        self.num1 = num1
        self.num2 = num2
        self.operation = operation.lower()

    def perform_operation(self):
        if self.operation == "add":
            return self.num1 + self.num2
        elif self.operation == "sub":
            return self.num1 - self.num2
        elif self.operation == "mul":
            return self.num1 * self.num2
        elif self.operation == "div":
            if self.num2 == 0:
                return "Cannot divide by zero"
            return self.num1 / self.num2
        else:
            return "Unsupported operation"

# Take inputs from the user
if __name__ == "__main__":
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Choose operation (add / sub / mul / div): ")

        calc = Calculator(a, b, op)
        output = calc.perform_operation()
        print("Result:", output)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

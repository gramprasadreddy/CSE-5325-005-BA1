def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero is not allowed."

def calculator():
    # Prompt user to enter two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Prompt user to enter an operator
    operator = input("Enter an operator (+, -, *, /): ")

    # Call the appropriate function based on the operator
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    else:
        return "Invalid operator."

    # Display the result
    return f"The result is: {result}"

# Run the calculator
print(calculator())

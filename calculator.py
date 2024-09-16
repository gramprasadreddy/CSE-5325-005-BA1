import math

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

def square_root(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Error! Cannot take the square root of a negative number."

def calculator():
    operation_type = input("Enter '1' for basic operations (+, -, *, /) or '2' for square root: ")

    if operation_type == '1':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter an operator (+, -, *, /): ")

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
    
    elif operation_type == '2':
        num = float(input("Enter a number to find the square root: "))
        result = square_root(num)
    
    else:
        return "Invalid operation type."

    return f"The result is: {result}"

print(calculator())

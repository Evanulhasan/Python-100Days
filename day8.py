# Making a Simple calculator 
num1 = float(input("Enter the number: "))

operation = input("Enter Operator: ")
num2 = float(input("Enter the number: "))

if operation == "+": 
    result = num1 + num2
elif operation == "-": 
    result = num1 - num2
elif operation == "*": 
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else: 
        result = "Error: Division"
elif operation == "**": 
    result = num1 + num2
else:
    result = "Error: Invalid operator"
    
print(f"Result: {result}")





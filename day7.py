num1 = float(input("Enter Number: "))
operation = input("Enter operation:" )
num2 = float(input("Enter Number: "))



match operation:
    case '+':
        result = num1 + num2 
    
    case '-':
        result = num1 - num2 
        
    case '*':
        result = num1 * num2 
        
    case '/':
        if num2 == 0:
            result = "Error: Cannot divide by zero"
        else: 
            result = num1 / num2
    
    case '**':
        result = num1 ** num2 
    
    case _:
        result = "Invalid Operator"

print("Result:", result)
    
    
    
        


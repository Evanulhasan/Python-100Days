# The code snippet you provided is a Python program that takes user input for their age, compares it
# to 18 using a conditional statement, and then outputs a message based on the comparison result.
# a = int(input("Enter your age: "))
# print("Your age is:", a)

# #Conditional operators 
# # >, <, >=, <=, ==, !=

# if(a>18): 
#     print("You can drive")
# else: 
#     print("You cannot drive")



# num = int(input("Enter the value of num: "))
# if(num<0):
#     print("Number is negative")
# elif(num==0):
#     print("Number is Zero")
# else:
#     print("Number is Positive.")
    
# print("I am happy now")

num = int(input("Enter the number: "))
if(num<0):
    print("Number is negative")
elif(num > 0):
    print("Number is Positive")
    if(num<=10):
        print("Number is between 1-10")
    elif(num > 10 and num <=20):
        print("Number is between 11 - 20") 
    else: 
        print("Number is greater than 20")
else:
    print("Number is zero")





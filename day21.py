# def average(a=9, b=1):
#     print("The average is ", (a+b)/2)
    
# # average(4, 6)
# average(b=9)

# def name(fname, mname="Hasan", lname="Oualid"):
#     print(f"Hello {fname} {mname} {lname}")
    
# name("Evanul")


# def average(*numbers):
    
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print(f"Average is: {sum/ len(numbers)}")
    

# # Taking tuple input using eval input 
# nums = eval(input("Enter a tuple: "))
# average(*nums)

# def name(**name):
#     print("Hello,", name["fname"],name["mname"], name["lname"]) 
    
# name(mname="Evanul",lname="Hasan", fname="Oualid")



def average(*numbers):
    
    sum = 0
    for i in numbers:
        sum = sum + i
    # print(f"Average is: {sum/ len(numbers)}")
    #In One function we can use only one return if we use two return first one work only.
    return sum/len(numbers)
    

# Taking tuple input using eval input 
nums = eval(input("Enter a tuple: "))
c=average(*nums)
print(c)



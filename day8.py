
# Get user's name
name = input("Enter your name: ")
print("Hello, " + name + "!")

# Get user's age and convert it to an integer
age = input("Enter your age: ")
age = int(age)
print("You are", age, "years old.")

# Get multiple inputs separated by spaces and convert them to integers
numbers = input("Enter numbers separated by spaces: ")
numbers_list = list(map(int, numbers.split()))
print("The numbers are:", numbers_list)
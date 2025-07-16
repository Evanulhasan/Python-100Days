# Modules and Pip

# print("Evanul Hasan Oualid")

def find_second_largest_simple(numbers):
  # Sort the list in descending order
  numbers.sort(reverse=True)
  # Return the second element
  print(numbers)
  return numbers[1]

# Example
my_list = [10, 20, 4, 45, 99]
second_largest = find_second_largest_simple(my_list)
print(f"The second largest number is: {second_largest}")
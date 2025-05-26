# Create a python program capable of greeting you with Good Morning. 
# Good Afternoon and Good Evening. Your program should use timemodule to get th current hour.

import datetime

def time_based_greeting():
  """
  This function greets the user with "Good Morning", "Good Afternoon", or
  "Good Evening" based on the current hour.
  """
  # Get the current hour (in 24-hour format, 0-23)
  current_hour = datetime.datetime.now().hour

  if 5 <= current_hour < 12:
    print("Good Morning! ☀️")
  elif 12 <= current_hour < 18:
    print("Good Afternoon! 🌤️")
  else:
    print("Good Evening! 🌙")

# Run the greeting function
if __name__ == "__main__":
  time_based_greeting()
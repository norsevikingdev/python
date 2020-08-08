# Error Handling

while True:
  try:
    age = int(input("What is your age? "))
    10/age
  except ValueError:
    print("Please enter a number")
  except ZeroDivisionError:
    print("Please enter a number greater than 0")
  else:
    break
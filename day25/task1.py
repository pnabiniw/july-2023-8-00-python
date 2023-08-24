try:
    num1 = int(input("Enter a number "))
    num2 = int(input("Enter another number "))
except ValueError:
    print("Please enter a valid number")
else:
    result = num1 + num2
    print(result)

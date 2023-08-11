# Conditions in python or in any programming language is used to make decisions
# We can make conditions in python in three different ways
# 1. Simple if
# 2. if....else block
# 3. if...elif ladder

# Note: Nested if conditions are also possible


# 1. Simple if
age = 18
if age > 19:
    print("The person is not a teenager")

# 'if conditions' always takes truthy or falsy statement. If the statement is truthy the block inside
# if condition is executed. If falsy the block inside if is not executed

if age:
    print(f"The person's age is {age}")

vowels = []
if vowels:
    print(vowels)

a = 2
if a:
    print(f"The number is {a}")  # The number is 2


# 2. if...else
age = 18
if age > 19:
    print("The person is not a teenager")
else:
    print("The person is a teenager")


if age:
    print(f"The person's age is {age}")
else:
    print("The age is not provided")

vowels = []
if vowels:
    print(vowels)
else:
    print("The list is empty")

data = [1, 2, 3, 4, 5]
if 2 in data:
    print("2 is present in the list")
else:
    print("2 is not in the list")

num = 5
if not num:
    print("The number is not given")
else:
    print(f"The given number is {num}")


# 3. if...elif ladder
exam_percent = int(input("Enter exam percent "))
if exam_percent >= 80:
    print("The student got distinction")
elif exam_percent >= 65:
    print("The student got first division")
elif exam_percent >= 55:
    print("The student got second division")
elif exam_percent >= 40:
    print("The student got third division")
else:
    print("The student failed !!")



# ternary if
a = 5
if a > 10:
    print("The number is greater than 10")
else:
    print("The number is less than 10")

# This is ternary if condition
print("The number is greater than 10") if a > 10 else print("The number is less than 10")



# Nested if => nested if is simply if condition inside a if condition
a = 12
if a > 10:
    if a > 15:
        print("The number is greater than 15")
    else:
        print("The number is just greater than 10")
else:
    print("The number is less than 10")

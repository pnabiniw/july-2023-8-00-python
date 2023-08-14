# break, continue and pass are the control statements in python. They can alter the normal flow
# of the program

# break
for i in range(10):
    if i == 4:
        break
    print(i)  # 0, 1, 2, 3


n = 0
while n <= 10:
    if n == 7:
        break
    print(n)
    n += 1


# continue
for i in range(10):
    if i == 4:
        continue
    print(i)  # 0, 1, 2, 3, 5, 6, 7, 8, 9

n = 0
while n <= 10:
    n += 1
    if n in [4, 7, 9]:
        continue
    print(n)  # 0, 1, 2, 3, 5, 6, 8, 10, 11


# pass
# pass is used to pass the block of code. It literally does nothing. It is also used in the place
# where code may occur in future
def addition(a, b):
    pass

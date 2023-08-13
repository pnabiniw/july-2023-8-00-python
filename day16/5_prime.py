n = int(input("Enter a number "))
counter = 0
for i in range(1, n+1):
    if n % i == 0:
        counter += 1
if counter == 2:
    print(f"{n} is prime")
else:
    print(f"{n} is composite")

# first 50 even numbers

n = 0
even_number_count = 0
while even_number_count != 50:
    if n % 2 == 0:
        print(n)
        even_number_count += 1
    n += 1


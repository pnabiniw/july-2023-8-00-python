# The order of arguments in a function must be in following way:
# 1. Positional Arguments
# 2. Default Arguments
# 3. *args
# 4. **kwargs


def addition(a, b, c, d=1, e=2, f=3, *args, **kwargs):
    print(a)  # 1
    print(b)  # 2
    print(c)  # 3
    print(d)  # 4
    print(e)  # 5
    print(f)  # 6
    print(args)  # (7, 8, 9, 10)
    print(kwargs)  # {"p": 11, "q": 12, "r": 14}


addition(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, p=11, q=12, r=14)

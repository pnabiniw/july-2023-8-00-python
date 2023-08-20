class Math:
    chapters = ["Linear Algebra", "Calculus"]


class Chemistry:
    chapters = ["Acid, Salt, Base", ]


class Physics(Math, Chemistry):
    pass


p = Physics()
print(p.chapters)  # ["Linear Algebra", "Calculus"]

# Operators are the special symbols in any programming language to carry out
# Arithmetic and Logical Operations

a = 1
b = 2
c = a + b
# Here '=' is an assignment operator and '+' is an arithmetic operator

# Arithemetic Operators
# Addition (+)
# Subtraction (-)
# Multiplication (*)
# Division (/)
# Floor Division (//) => Floor division removes the decimal value and only
# provides the integer towards floor.

print(3 // 2)  # It gives 1
print(-3 // 2)  # It gives -2

# Exponential (**)
print(3 ** 2)  # It gives 9

# Modulus (%) => Gives remainder of a division
print(3 % 2)  # Gives 1
print(4 % 2)  # Gives 0




###### Comparision / Relational Operators #######
# ==, <, >, !=, >=, <= are the relational operators

print(4 == 5)  # False
print(6 != 3)  # True


# Logical Operators
# and, or, not are the logical operations and their operators are "and", "or"
# and "not" respectively. The results in logical operations are either True or False



# Identity Operators
# Identity operators check whether the two objects are same or not. 'is' and
# 'is not' are used for the identity check.
a = 1
b = 1
print(a is b)  # True
print(id(a))
print(id(b))  # For the same object, id() gives equal value


# Membership Operators
# It is used to check membership of an object in a sequence. 'in' and 'not in' are
# used for membership check
print(2 in [1, 2, 3])  # True
print(3 not in [1, 2, 3])  # False


# Assignment Operator
# The result of any operation can be assigned to a variable using an assignment
# operator. "=" is a basic assignment operator.
name = "Jon"  # here = is an assignment operator

# +=, -=, *=, /= are also some of the assignment operators
a = 1
a = a + 1  # This line can also be written as a += 1
print(a)  # 2
a += 1  # 3
print(a)


# Precedence and Associativity
# Precedence of the operators is the rule that determines which operator should be
# executed first
# If multiple operators in an operation have the same precedence then the associativity
# determines the operation sequence

# Normally associativity is from left-right except for the case of '**'.
# For exponent (**), it is from right-left

print(2**3**2)  # 512

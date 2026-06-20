# Logical Operators in Python are used to combine conditional statements. The three main logical operators are:
# 1. and: Returns True if both statements are true
# 2. or: Returns True if at least one statement is true
# 3. not: Reverse the result, returns False if the result is true


a = 8
b = 9
print(a > 5 and b > 5)  # Output: True
print(a > 5 or b < 5)   # Output: True
print(not(a > 5 and b > 5))  # Output: False

print(not(a > 10))  # Output: True
print(not(b < 5))   # Output: True


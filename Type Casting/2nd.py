# type() function is used to get the data type of a variable. It returns the data type of the variable as a string.

# str() function is used to convert a value to a string data type. It takes a value as an argument and returns the string representation of that value.
# float() function is used to convert a value to a float data type. It takes a value as an argument and returns the float representation of that value.
# int() function is used to convert a value to an integer data type. It takes a




a = 5
b = float(a)  # Type casting from integer to float
t = type(b)  # This will return the data type of variable b, which is float.

print(t)  # This will print <class 'float'>.
print(b)  # This will print 5.0, which is the float representation of the integer 5.

t = type(a)  # This will return the data type of variable a, which is int (integer).
print(t)  # This will print <class 'int'>.
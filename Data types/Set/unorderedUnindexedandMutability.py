s = {3, 1, 4, 1, 5, 9, 2}

print(s) 
try:
    print(s[0])
except TypeError as e:
    print(e)
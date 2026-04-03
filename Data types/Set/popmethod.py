s = {1, 2, 3, 4, 5}
val = s.pop()
print(val)
print(s)

s.clear()  
try:
    s.pop()
except KeyError as e:
    print("Error:", e)
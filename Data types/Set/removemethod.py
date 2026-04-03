s = {1, 2, 3, 4, 5}
s.remove(3)
print(s)  

try:
    s.remove(10)
except KeyError as e:
    print("Error:", e)  

s.discard(4)
print(s)  

s.discard(10)  
print(s)
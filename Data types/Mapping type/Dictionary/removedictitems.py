d = {1: 'pankaj', 2: 'rahul', 3: 'vansham', 'age':22}

# Using del 
del d["age"]
print(d)

# Using pop() 
val = d.pop(1)
print(val)

# Using popitem()
key, val = d.popitem()
print(f"Key: {key}, Value: {val}")

# Using clear()
d.clear()
print(d)
x = ["Tom", "Jerry"]
y = ["Tom", "Jerry"]
z = x

print(x is z) # True 
print(x is y) # False because x is not the same object as y, even if they have the same content
print(x == y) # True 

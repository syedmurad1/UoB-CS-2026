# and  logical operator
a = 66
b = 33
c = 99
if a > b and c > a:
  print("Both conditions are True")


# or  logical operator
a = 66
b = 33
c = 99
if a > b or a > c:
  print("At least one of the conditions is True")


# not  logical operator
a = 33
b = 66
if not a > b:
  print("a is NOT greater than b")


# Nested If
k = 11

if k > 10:
  print("Above ten,")
  if k > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# pass 
# g = 3
# h = 4

# if g > h:
#   pass

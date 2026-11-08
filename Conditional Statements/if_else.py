a = "Charles"
if a=="Charles":
  print("I am the King")




  # Alternative execution
x = input("Input a number: ")
if x.isdigit():
    print ("You input a number")
else:
    print ("Please input a number next time")

# Avoiding division by zero

x = int(input("x? "))
y = int(input("y? "))
if y != 0:
    print (x / y)
else:
    print ("Attempted division by zero")


# Elif
a = 5
b = 5
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


# if elif else
a = 99
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

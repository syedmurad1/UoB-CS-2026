# Write a program that takes an integer n and prints:
# "Positive" if n > 0
# "Negative" if n < 0
# "Zero" if n == 0
# Answer:


n = int(input("Enter an integer: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")












# Login Check (Username & Password)
# Ask the user for a username and password.
# If username is "admin" and password is "1234", print "Login successful".
# Answer:


username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")

















# Day of Week from Number
# Exercise:
# Read a number from 1–7 and print the day of the week:
# 1 = Monday, 2 = Tuesday, …, 7 = Sunday.
# If the number is not 1–7, print "Invalid day".
# Answer:


n = int(input("Enter a number (1-7): "))

if n == 1:
    print("Monday")
elif n == 2:
    print("Tuesday")
elif n == 3:
    print("Wednesday")
elif n == 4:
    print("Thursday")
elif n == 5:
    print("Friday")
elif n == 6:
    print("Saturday")
elif n == 7:
    print("Sunday")
else:
    print("Invalid day")




















# Write a program that asks for a person’s age and prints the ticket price:

# Age < 5: "Free"
# Age 5–17: "Child ticket: £5"
# Age 18–64: "Adult ticket: £10"
# Age 65+: "Senior ticket: £7"
# Answer:


age = int(input("Enter age: "))

if age < 5:
    print("Free")
elif 5 <= age <= 17:
    print("Child ticket: £5")
elif 18 <= age <= 64:
    print("Adult ticket: £10")
else:
    print("Senior ticket: £7")
























# Write a program to check if a year is a leap year.
# A year is leap if:
# it is divisible by 400, OR
# it is divisible by 4 but not by 100.
# Answer:

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")























# Age Group & Ticket Type
# Exercise:
# Write a program that:
# Asks for age.
# If age < 18:
# If age < 5 → print "Free entry"
# Else → print "Child ticket"
# Else (age ≥ 18):
# If age ≥ 60 → print "Senior ticket"
# Else → print "Adult ticket"
# Answer:

age = int(input("Enter age: "))

if age < 18:
    if age < 5:
        print("Free entry")
    else:
        print("Child ticket")
else:
    if age >= 60:
        print("Senior ticket")
    else:
        print("Adult ticket")

























# Website Login with Role
# Exercise:
# Write a program that:
# Asks for username and password.
# If username == "admin" and password == "1234":
# Ask for role ("viewer" or "editor").
# If role is "viewer", print "Admin logged in as viewer".
# If role is "editor", print "Admin logged in as editor".
# Otherwise print "Unknown role".
# Else print "Invalid login".
# Answer:

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    role = input("Enter role (viewer/editor): ")
    if role == "viewer":
        print("Admin logged in as viewer")
    elif role == "editor":
        print("Admin logged in as editor")
    else:
        print("Unknown role")
else:
    print("Invalid login")

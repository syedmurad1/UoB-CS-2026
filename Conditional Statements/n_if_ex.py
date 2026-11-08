# Password and Username Checking
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin":
    if password == "i-am-admin":
        print("Login successful! Welcome, admin.")
    elif password == "123":
        print("Weak password. Please reset your password.")
    else:
        print("Incorrect password. Please try again.")
else:
    if username == "guest":
        if password == "123":
            print("Login successful! Welcome, guest.")
        else:
            print("Incorrect password. Please try again.")
    else:
        print("Unknown user. Please try again.")
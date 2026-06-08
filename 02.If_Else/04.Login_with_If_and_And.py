username = str(input("Enter your username: "))
password = str(input("Enter this user's password: "))

if username.lower() == "darth_vader" and password == "1138":
    print("Login successful!")
else:
    print("Login unauthorized")
password = input("enter a password: ")
if password.isalnum():
    if len(password) < 8:
        print("your password has leters, numbers and it is < 8")
    else:
        print("your password has leters, numbers and it is NOT < 8")
else:
    print("your password has NO leters OR NO numbers ")

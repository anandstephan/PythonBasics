password_count = len(input("Enter the Password"))

if password_count<6:
    print("Weak")
elif password_count>=6 and password_count<=10:
    print("Medium")
else:
    print("Strong")
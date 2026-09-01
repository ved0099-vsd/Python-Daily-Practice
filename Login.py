print("-" * 40)
print("Login System")
print("-" * 40)

Username = input("Please enter your Username : ")
Password = int(input("Please enter your Password : "))

if(Username == "Admin"):
    if(Password == 1234):
        print("Login Successfull ! ")
    else:
        print("Password Incorrect")

else:
    print("Invalid Username")
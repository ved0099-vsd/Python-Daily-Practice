#Login System 🔐

#Take:

#Username
#Password

#Correct username = "admin"
#Correct password = "1234"

#If username is correct, check the password.

#Print:

#Login successful
#Wrong password
#Wrong username

def main():
    Username = input("Enter your username  : ")
    Password = int(input("Enter your Password : "))

    if Username == "admin123":
        if Password == 1234:
            print("Login Successfull")
        else:
            print("Incorrect Password")
    else:
        print("Wrong Username")

if __name__ == "__main__":
    main()
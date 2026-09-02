#Login System 🔐

#Take:
#Username
#Password
#OTP

#Rules:

#Username must be correct.
#If username is correct → check password.
#If password is correct → check OTP.
#Only then → Login successful.

def main():
    Username = input("Enter Username : ")
    Password = int(input("Enter Password : "))
    OTP = int(input("Enter OTP : "))

    if Username == "Ved":
        if Password == 1234:
            if OTP == 1001:
                print("Login Successfull........!")
            else:
                print("Incorrect OTP")
        else:
            print("incorrect Password")
    else:
        print("Incorrect Username")

if __name__ == "__main__":
    main()
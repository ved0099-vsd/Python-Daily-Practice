#Password Strength 🔐

#Take a password.

#Check:

#Length ≥ 8
#Contains a number
#Contains an uppercase letter

#If all three → "Strong password".

#If only some → "Medium password".

#Otherwise → "Weak password".

def main():
    Password = input("Enter a password : ")

    length = len(Password)

    if length < 6:
        print("Weak password")

    elif length <= 9:
        print("Strong password")

    else:
        print("Strong password")

if __name__ == "__main__":
    main()
def main():

    Ticket = input("Do you have a Boarding Pass? (yes/no) : ")
    ID = input("Do you have a valid ID ? : ")
    Security = input("Have you passed all security checks ? (yes/no) : ")

    if Ticket == "yes":
        if ID in ["Passport","Aadhaar card","Pan card"]:
            if Security == "yes":
                print("Yes you can board the flight")
            else:
                print("You have no tpassed the security checks ")
        else:
            print("You must have a ID")
    else:
        print("You dont have a boarding pass bindok")

if __name__ == "__main__":
    main()
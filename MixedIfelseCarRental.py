#Car Rental 🚗
#Take:

#Age
#Licence (yes/no)
#Car availability (yes/no)
#Security deposit

#Rules:
#Age must be 21+.
#Licence must be valid.
#Car must be available.
#Deposit must be at least ₹5,000.

#Only then approve rental.

def main():
    Age = int(input("Enter your Age : "))
    License = input("Do you have license? (yes/no) : ")
    Car_availaility = input("is car available ? (yes/no) : ")
    Security_deposit = int(input("ENter deposit amount : "))

    if Age >= 21:
        if License == "yes":
            if Car_availaility == "yes":
                if Security_deposit >= 5000:
                    print("here are your car keys!!!!!!!!")
                else:
                    print("Deposit must be 5000 atleast")
            else:
                print("Sorry no car available right now ")
        else:
            print("you dont have a license !")
    else:
        print("Your age is below 21")
        
if __name__ == "__main__":
    main()
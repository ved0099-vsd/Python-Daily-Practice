#Restaurant Order 🍔

#Take:
#Food item (pizza, burger, pasta)
#Quantity
#Membership (yes/no)

#Prices:
#Pizza = ₹250
#Burger = ₹150
#Pasta = ₹200

#Calculate the total bill.
#If the customer is a member:
#Bill ≥ ₹500 → 20% discount

#Otherwise → 10% discount
#If not a member → No discount
#Print the final bill.

def main():
    Food = input("Enter food item (pizza,pasta,burger) :")
    Quantity = int(input("Enter Quantity : "))
    Member = input("Are you a member of our restaurant ? (yes/no) ")


    if Food in {"pizza","burger","pasta"}:   #Dict  #in
        if Quantity > 0:

            if Food == "pizza":
                Price = 250
            elif Food == "burger":
                Price = 150
            else:
                Price = 200

            Amount = Price * Quantity
            if Member == "yes":
                if Amount >= 500:
                    Discount = Amount * 0.20
                    Amount = Amount - Discount
                    print("Your bill will be ",Amount)
                else:
                    Discount = Amount * 0.10
                    Amount = Amount - Discount
                    print("Your bill will be : ",Amount)
            else:
                print("No discount pay the following amount ", Amount)
        else:
            print("Invalid Quantity")
    else:
        print("Sorry thats not available")
            






if __name__ == "__main__":
    main()
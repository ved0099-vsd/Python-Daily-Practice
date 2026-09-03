#Mini E-Commerce System 🛒

#Take:

#Product price
#Quantity
#Membership (yes/no)
#Delivery type (standard/express)

#Calculate the total.

#Rules:

#Discount:

#Member + total ≥ ₹5000 → 20% discount
#Member + total < ₹5000 → 10% discount
#Non-member → No discount

#Delivery:

#Standard → ₹50
#Express → ₹150

def main():
    price = int(input("Enter product price: "))
    Quantity = int(input("Enter product quantity: "))
    Membership = input("Do you have membership? (yes/no): ")
    Delivery = input("Enter delivery type (standard/express): ")

    Total = price * Quantity
    print("Product total:", Total)

    if Membership == "yes" and Total >= 5000:
        Discount = Total * 0.20
        Total = Total - Discount

        if Delivery == "standard":
            Total = Total + 50
            print("You got 20 percent discount")
            print("Your bill will be:", Total)

        else:
            Total = Total + 150
            print("You got 20 percent discount")
            print("Your bill will be:", Total)

    elif Membership == "yes" and Total < 5000:
        Discount = Total * 0.10
        Total = Total - Discount

        if Delivery == "standard":
            Total = Total + 50
            print("You got 10 percent discount")
            print("Your bill will be:", Total)

        else:
            Total = Total + 150
            print("You got 10 percent discount")
            print("Your bill will be:", Total)

    else:
        if Delivery == "standard":
            Total = Total + 50
            print("You are not a member, so no discount")
            print("Your bill will be:", Total)

        else:
            Total = Total + 150
            print("You are not a member, so no discount")
            print("Your bill will be:", Total)


if __name__ == "__main__":
    main()
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

    # Discount
    if Membership == "yes":
        if Total >= 5000:
            Discount = Total * 0.20
            Total = Total - Discount
            print("20% discount applied")
        else:
            Discount = Total * 0.10
            Total = Total - Discount
            print("10% discount applied")
    else:
        print("No discount")

    # Delivery
    if Delivery == "standard":
        Total = Total + 50
        print("Standard delivery: ₹50")
    elif Delivery == "express":
        Total = Total + 150
        print("Express delivery: ₹150")
    else:
        print("Invalid delivery type")

    print("Final bill:", Total)


if __name__ == "__main__":
    main()
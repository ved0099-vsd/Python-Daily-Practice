#Shopping Discount 🛍️

#Take the shopping amount.

#₹5000 or more → 20% discount
#₹2000–₹4999 → 10% discount
#Below ₹2000 → No discount

#Print the final amount.


def main():
    Amount = int(input("Enter Shopping Amount  : "))

    if Amount >= 5000:
        Discount = Amount * 0.20
        Amount = Amount - Discount
        print("You amount after 20% discount will be ",Amount)

    elif Amount >= 2000:
        Discount = Amount * 0.10
        Amount = Amount - Discount
        print("You amount after 10% discount will be ",Amount)

    else:
        print("No discount")


if __name__ == "__main__":
    main()
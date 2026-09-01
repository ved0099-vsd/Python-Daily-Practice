def main():
    Amount = int(input("Enter Shopping Amount : "))
    Membership = input("Are you a member of our Shop (Yes/No) :")

    if Amount >= 5000:
        if Membership == "Yes":
            print("You will get discount of 15%, Your Discounted price will be", Amount * 15/100)
        else:
            print("You are not a member so only 5% Discount yopur Discounted amount will be", Amount * 5/100)
    else:
        print("Amount under 5000 so no discount at all")


if __name__ == "__main__":
    main()
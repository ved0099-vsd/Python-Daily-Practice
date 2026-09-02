def main():
    Amount = int(input("Enter Shopping Amount : "))
    Membership = input("Are you a member of our Shop? (yes/no)  : ")

    if Amount >= 10000:
        if Membership == "yes":
            Discount = Amount * 15 / 100
        else:
            Discount = Amount * 5 / 100

    elif Amount >= 5000:
        if Membership == "yes":
            Discount = Amount * 10 / 100
        else:
            Discount = Amount * 3 / 100

    else:
        Discount = 0

    Final_amount = Amount - Discount

    print("Discount : ",Discount)
    print("Final amount will be : ",Final_amount)

if __name__ == "__main__":
    main()
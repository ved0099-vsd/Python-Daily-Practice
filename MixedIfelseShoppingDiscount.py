def main():
    amount = float(input("Enter shopping amount: "))
    member = input("Are you a member? (yes/no): ")

    if amount >= 10000:
        if member == "yes":
            discount = amount * 20 / 100
        else:
            discount = amount * 10 / 100

    elif amount >= 5000:
        if member == "yes":
            discount = amount * 10 / 100
        else:
            discount = amount * 5 / 100

    else:
        discount = 0

    final_amount = amount - discount

    print("Discount:", discount)
    print("Final amount:", final_amount)


if __name__ == "__main__":
    main()
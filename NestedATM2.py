def main():
    Balance = int(input("Enter balance....: "))
    Amount = int(input("Enter Withdrawl Amount : "))

    if Amount > 0:
        if(Balance > Amount):
            Balance = Balance - Amount
            print("Withdrawl Successfull ")
            print("Your Available balance is ",Balance)
        else:
            print("Insufficient Balance.......")

    else:
        print("Invalid Amount Entered ")

if __name__ == "__main__":
    main()
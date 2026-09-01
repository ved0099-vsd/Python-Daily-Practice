def main():
    Balance = int(input("Enter Balance......:"))
    Withdraw = int(input("Enter Withdraw Amount  :"))

    if(Withdraw > 0):
        if(Balance >= Withdraw):
            Balance = Balance - Withdraw
            print("Withdrawl Successfull........")
            print("Remaining Balance",Balance)
        else:
            print("Invalid balance ")

    else:
        print("Invalid Amount Entered")

if __name__ == "__main__":
    main()
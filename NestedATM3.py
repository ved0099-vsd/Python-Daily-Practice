def main():
    Balance = 5000
    ATMPin = 1234
    ATMPin = int(input("Enter your ATM Pin : "))

    if ATMPin == 1234:
        Withdrawl = (int(input("Enter Withdrawl Amount : ")))
        if(Withdrawl <= Balance):
            Balance = Balance - Withdrawl
            print("Your available balance is : ", Balance)
        else:
            print("Insufficient Balance")

    else:
        print("Invalid ATM pin")
        


if __name__ == "__main__":
    main()
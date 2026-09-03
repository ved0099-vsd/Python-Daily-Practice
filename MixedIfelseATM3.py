#ATM Withdrawal 💳

#Take:

#PIN
#Balance
#Withdrawal amount

#Correct PIN = 1234

#If PIN is correct:

#Check whether withdrawal amount is positive.
#Check whether there is enough balance.

def main():
    Pin = int(input("Enter PIN :"))
    Balance = 5000
    Amount = int(input("Enter withdrawal amount : "))

    if Pin == 6969:
        if Balance >= Amount:
            Balance = Balance - Amount
            print("Transaction Successfull")
            print("Available balance is ",Balance)
        else:
            print("insufficient Balance")
    else:
        print("Incorrect PIN")


if __name__ == "__main__":
    main()
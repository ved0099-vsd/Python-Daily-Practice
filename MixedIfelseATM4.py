#ATM Withdrawal 💳

#Take:

#PIN
#Balance
#Withdrawal amount

#Correct PIN = 1234.

#If PIN is correct:

#Amount must be greater than 0.
#Amount must not exceed balance.
#Minimum ₹500 must remain after withdrawal.

#Print the appropriate message.

def main():
    Pin = int(input("Enter PIN : "))
    Balance = 5000
    Amount = int(input("Enter your Withdrawal Amount : "))

    if Pin == 1234:
        if Amount <= Balance:
            if Amount > 0:
                if Balance - Amount >= 500:
                    Balance = Balance - Amount
                    print("Transaction Successfull balance is :",Balance )
                else:
                    print("500 must remain in account")
            else:
                print("Invalid amount")
        else:
            print("insufficient balance")
    else:
        print("invalid password")
    

if __name__ == "__main__":
    main()
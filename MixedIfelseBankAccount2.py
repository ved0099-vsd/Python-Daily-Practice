#Bank Account 🏦
#Take:
#Account status
#PIN
#Balance
#Transaction type (withdraw/deposit)
#If account is active and PIN is correct:

#Withdraw:
#Check amount.
#Check sufficient balance.
#Keep minimum ₹500.

#Deposit:
#Amount must be greater than 0.

def main():
    Account_status = input("ENTER ACCOUNT STATUS (active/inactive ): ")
    Pin = int(input("Enter PIN : "))
    Balance = float(input("Enter Balance : "))
    Transaction = input("Enter transaction type (withdrawl/deposit) : ")

    if Account_status == "active":
        if Pin == 1234:
            if Transaction == "withdrawl":
                withdraw = float(input("Enter your withdrawl amount : "))

                if withdraw > 0:
                    if withdraw <= Balance:
                        if Balance - withdraw >= 500:
                            Balance = Balance - withdraw
                            print("Withdrawal Successful")
                            print("Remaining balance",Balance)
                        else:
                            print("Remaining balance of 500 must remain")
                    else:
                        print("Insufficient balance ")
                else:
                    print("invalid amount")

            elif Transaction == "deposit":

                amount = float(input("Enter deposit amount : "))
                if amount > 0:                    
                    Balance = Balance + amount

                    print("Deposit Successfull")
                    print("Available balance ",Balance)
                else:
                    print("Amount invalid")
            else:
                print("Transaction type invalid")
        else:
            print("invalid password")
    else:
        print("Account inactive")

if __name__ == "__main__":
    main()
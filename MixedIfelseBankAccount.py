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
    status = input("Enter account status (active/inactive): ")
    pin = int(input("Enter PIN: "))
    balance = float(input("Enter balance: "))
    transaction = input("Enter transaction (withdraw/deposit): ")

    if status == "active":
        if pin == 1234:

            if transaction == "withdraw":
                amount = float(input("Enter withdrawal amount: "))

                if amount > 0:
                    if amount <= balance:
                        if balance - amount >= 500:
                            balance = balance - amount
                            print("Withdrawal successful")
                            print("Remaining balance:", balance)
                        else:
                            print("Minimum balance of ₹500 must remain")
                    else:
                        print("Insufficient balance")
                else:
                    print("Invalid amount")

            elif transaction == "deposit":
                amount = float(input("Enter deposit amount: "))

                if amount > 0:
                    balance = balance + amount
                    print("Deposit successful")
                    print("Updated balance:", balance)
                else:
                    print("Invalid amount")

            else:
                print("Invalid transaction type")

        else:
            print("Incorrect PIN")

    else:
        print("Account is inactive")


if __name__ == "__main__":
    main()




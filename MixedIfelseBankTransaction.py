#Mini Bank Transaction 🏦

#Take:

#Account status (active/inactive)
#PIN
#Transaction (withdraw/deposit)
#Balance

#Correct PIN = 1234.

#If account is active and PIN is correct:

#Withdraw:

#Amount > 0
#Amount ≤ balance
#₹500 must remain

#Deposit:

#Amount must be > 0

#Print the updated balance.

def main():
    Status = input("Enter your Account Status :(active/inactive) ")
    PIN = int(input("Enter your PIN : "))
    Transaction = input("Enter transaction type (withdraw/deposit) :")
    Balance = 69000

    if Status == "active":
        if PIN == 1234:
            if Transaction == "withdraw":
                Amount = int(input("Enter withdraw amount : "))
                if Amount > 0:
                    if Amount <= Balance:
                        Balance = Balance - Amount
                        if Balance - Amount >= 500:
                            print("Transaction successfull")
                            print("your remaining balance is",Balance)
                        else:
                            print("minimum 500 must remian in the account so transaction failed")
                    else:
                        print("insufficient balance")
                else:
                    print("invalid amount")
            else:
                if Transaction == "deposit":
                    Deposit = int(input("Enter deposit amount : "))                   
                    if Deposit > 0:

                        Balance = Balance + Deposit
                        print("Deposit successfull available balance is :",Balance)
                    else:
                        print("invalid input")
                else:
                    print("please select between deposit/withdraw")
        else:
            print("invalid PIN")
    else:
        print("Your Account is not active")
                


                

if __name__ == "__main__":
    main()
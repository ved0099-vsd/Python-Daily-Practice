# 1. ATM Withdrawal 💰
#Take:
#PIN
#Account status
#Balance
#Withdrawal amount

#Rules:

#PIN must be correct.
#Account must be active.
#Withdrawal amount must be greater than 0.
#Withdrawl Amount must not exceed balance.
#After withdrawal, at least ₹500 must remain.

def main():
    PIN = int(input("Enter PIN : "))
    Status = input("Is your Account Active ? (Yes/No)")
    Balance = 5000
    Withdrawl = int(input("Enter Withdrawl Amount---- : "))

    if PIN == 1234:
        if Status == "Yes":
            if Withdrawl > 0:
                if Withdrawl <= Balance:
                    if Balance - Withdrawl >= 500:
                        Balance = Balance - Withdrawl
                        print("Withdrawl Transaction Successful")
                        print("Remaining balance ",Balance)
                    else:
                        print("Reamining Balance of 500 must remain")
                else:
                    print("Insufficient balance")
            else: 
                print("Invalid withdrawl amount")
        else:
            print("Account is inactive")
    else:
        print("Incorrect PIN")



if __name__ == "__main__":
    main()
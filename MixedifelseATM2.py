#PIN must be correct.
#Account must be active.
#Withdrawal amount must be greater than 0.
#Amount must not exceed balance.
#After withdrawal, at least ₹500 must remain.


def main():
    Pin = int(input("Enter PIN : "))
    Status = input("IS your account active (yes/no): ")
    Balance = 5000
    Withdrawl = int(input("Enter your Withdrawl amount---: "))

    if Pin == 1234:
        if Status == "yes":
            if Withdrawl > 0:
                if Withdrawl <= Balance:
                    if Balance - Withdrawl >= 500:
                        Balance = Balance - Withdrawl
                        print("Withdrawl transaction successful")
                        print("Available balance is ",Balance)
                    else:
                        print("Remaining balance of 500 must remain")
                else:
                    print("insufficient balance")
            else:
                print("invalid withdrawl amount")
        else:
            print("Your account is not active")
    else:
        print("Wrong PIN")    

if __name__ == "__main__":
    main()
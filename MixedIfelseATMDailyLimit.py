#ATM + Daily Limit 💰🔥

#Take:
#Balance
#Withdrawal amount
#Daily withdrawal amount already used.

#Rules:
#Withdrawal must be > 0.
#Balance must be sufficient.
#Daily total withdrawal cannot exceed ₹20,000.
#Minimum ₹500 must remain.

def main():
    pin = int(input("Enter PIN: "))
    balance = int(input("Enter account balance: "))
    amount = int(input("Enter withdrawal amount: "))
    withdrawn_today = int(input("Enter amount already withdrawn today: "))

    if pin == 1234:
        if amount > 0:
            if amount <= balance:
                if withdrawn_today + amount <= 20000:
                    balance = balance - amount
                    print("Withdrawal successful")
                    print("Remaining balance:", balance)
                else:
                    print("Daily withdrawal limit exceeded")
            else:
                print("Insufficient balance")
        else:
            print("Invalid withdrawal amount")
    else:
        print("Incorrect PIN")


if __name__ == "__main__":
    main()
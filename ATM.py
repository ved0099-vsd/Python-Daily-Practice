print("-" * 40)
print("ATM WITHDRAWL")
print("-" * 40)

Balance = 1000

Amount = int(input("Enter your Amount..."))

if(Amount <= Balance ):
    if(Amount % 100 == 0):
        Balance = Balance - Amount
        print("Transaction Successsfull")
    else:
        print("Amount should be Multiple of 50")


else:
    print("Balance Insufficient..!")
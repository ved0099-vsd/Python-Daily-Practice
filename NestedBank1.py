def main():
    Pin = int(input("Enter your PIN : "))
    Status = input("Account Active or nor ? ")
    Balance = 10000
    Withdraw = float(input("Enter withdrawl amount : "))

    if Pin == 1122:
        if Status == "Active":
            if Withdraw <= Balance:
                Balance = Balance - Withdraw
                print("Transaction Successfull... balance amount is ",Balance)
            else:
                print("Insufficient Balance ")
        else:
            print("its inactive")
    else:
        print("Wrong PIN")

if __name__ =="__main__":
    main()
    
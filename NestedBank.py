def main():
    AccountNo = int(input("Enter your Account No. : "))
    Pin = int(input("Enter your PIN : "))
    Balance = 5000

    if(AccountNo == 123456789):
        if (Pin == 1234):
            print("Your Balance is ",Balance)
        else:
            print("Incorrect PIN")
    else:
        print("Incorrect Account No.")

if __name__ == "__main__":
    main()
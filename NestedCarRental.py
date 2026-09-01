def main():
    Age = int(input("Enter your Age : "))
    Liscence = (input("Do you have a Liscence ? (Yes/No)"))
    Deposit = 5000

    if(Age >= 18):
        if(Liscence == "Yes"):
            Amount = int(input("Yes you can Rent our Car And Deposit is 5000 pay now :"))

            if(Deposit == 5000):
                print("Transaction Successfull........")

            else:
                print("Pay 5000 not less")

    else:
        print("You are not eligible")


        
if __name__ == "__main__":
    main()
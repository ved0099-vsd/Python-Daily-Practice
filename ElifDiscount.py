def main():
    Amount = int(input("Enter Amount : "))

    if(Amount >= 5000):
        print("18% Discount....... Your Discounted amount will be ", Amount * 18/100 )

    elif(Amount >= 4000):
        print("15% Discount....... Your Discounted amount will be ", Amount * 15/100 )

    elif(Amount >= 2500):
        print("12% Discount....... Your Discounted amount will be ", Amount * 12/100 )

    elif(Amount >= 1500):
        print("8% Discount....... Your Discounted amount will be ", Amount * 8/100 )


    else:
        print("Sorry No Discount")

if __name__ == "__main__":
    main()
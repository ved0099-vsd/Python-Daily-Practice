def main():
    units = int(input("Enter your Electricity Units : "))

    if units < 100:
        Bill = units * 5        
        if Bill > 2000:
            Bill = Bill * 5 /100
            print("Your bill is above 2000 so subcharges of 5 percent so the amount will be : ",Bill)
        else:
            print(Bill)

    elif units < 200:
        Bill = units * 7

        if Bill > 2000:                
            Bill = Bill * 7 /100
            print("Your bill is above 2000 so subcharges of 7 percent so the amount will be : ",Bill)
        else:
                print(Bill)
    elif units < 300:
        Bill = units * 10

        if Bill > 2000:                
            Bill = Bill * 10 / 100
            print("Your bill is above 2000 so subcharges of 7 percent so the amount will be : ",Bill)
        else:
            print("Bill")

    else:
        Bill = units * 12

        if Bill > 2000:                
            Bill = Bill * 12 /100
            print("Your bill is above 2000 so subcharges of 7 percent so the amount will be : ",Bill)

if __name__ == "__main__":
    main()
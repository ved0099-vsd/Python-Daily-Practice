def main():
    units = int(input("Enter your consumed units : "))

    if units < 100:
        Bill = units * 7
        if Bill > 2000:
            Subcharges = Bill * 5 / 100 
            Bill = Subcharges + Bill
            print("Your bill is above 2000 so including subcharges the Amount will be", Bill)
        else:
            print("Your bill will be ", Bill)

    elif units < 200:
        Bill = units * 10
        if Bill > 2000:
            Subcharges = Bill * 5 / 100
            Bill = Subcharges + Bill
            print("Your bill is above 2000 so including subcharges the Amount will be", Bill)
        else:
            print("Your bill will be ", Bill)

    elif units < 300:
        Bill = units * 12
        if Bill > 2000:
            Subcharges = Bill * 5 / 100
            Bill = Subcharges + Bill
            print("Your bill is above 2000 so including subcharges the Amount will be", Bill)
        else:
            print("Your Bill will be", Bill)

    else:
        units > 300
        Bill = units * 15
        if Bill > 2000:
            Subcharges = Bill * 5 /100
            Bill = Subcharges + Bill
            print("Your bill is above 2000 so including subcharges the Amount will be", Bill)
        else:
            print("Your bill will be ",Bill)

if __name__ == "__main__":
    main()
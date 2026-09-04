#Electricity Bill ⚡

#Take units consumed.

#0–100 → ₹5/unit
#101–200 → ₹7/unit
#201–300 → ₹10/unit
#Above 300 → ₹12/unit

#After calculating the bill:

#If bill is above ₹3000, add a 5% surcharge.

#Print the final bill.

def main():
    units = int(input("Enter your units : " ))

    if units > 300:
        Bill = units * 12
        if Bill >= 3000:
            Charge = Bill + 5/100
            print("Your bill is ab0ve 3000 so subcharge of 5 % so bill is ",Charge)
        else:
            print("Your bill is ",Bill)

    elif units >= 200:
        Bill = units * 10
        if Bill >= 3000:
            Charge = Bill + 5/100
            print("Your bill is ab0ve 3000 so subcharge of 5 % so bill is ",Charge)
        else:
            print("Your bill is ",Bill)

    elif units >= 100:            
        Bill = units * 7
        if Bill >= 3000:
            Charge = Bill + 5/100
            print("Your bill is ab0ve 3000 so subcharge of 5 % so bill is ",Charge)
        else:
            print("Your bill is ",Bill)

    else:
        units <= 100
        Bill = units * 5
        print("Your bill will be : ",Bill)



if __name__ == "__main__":
    main()
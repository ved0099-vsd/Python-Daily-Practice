#Electricity Bill ⚡

#Take the number of units.

#0–100 units → ₹5/unit
#101–200 units → ₹7/unit
#Above 200 → ₹10/unit

#Calculate and print the bill.

def main():
    units = int(input("Enter your units : "))

    if units >= 200:
        Bill = units * 10
        print("Bill is :",Bill)

    elif units >= 101:
        Bill = units * 7
        print("Bill is ",Bill)

    else:
        Bill = units * 5
        print("Bill is ",Bill)
        

if __name__ == "__main__":
    main()
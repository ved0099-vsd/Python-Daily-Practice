#shopping Discount 🛍️

#take:

#Shopping amount
#Membership (yes/no)

#Rules:

#Amount	Member	Discount
#₹10,000+	Yes	20%
#₹10,000+	No	10%
#₹5,000–₹9,999	Yes	10%
#₹5,000–₹9,999	No	5%
#Below ₹5,000	Anyone	0%

#Print the final amount.

def main():
    Amount = int(input("Enter shopping amount : "))
    Member = input("Are you a member (yes/no) : ")

    if Amount >= 10000:
        if Member == "yes":
            Discount = Amount * 20 / 100
            Total = Amount - Discount
            print("Your total bill with discount will be ",Total)
        else:
            Discount = Amount * 10 / 100
            Total = Amount - Discount
            print("No membership so only 10% discount total bill is : ",Total)

    elif Amount >= 5000:
        if Member == "yes":
            Discount = Amount * 10 / 100
            Total = Amount - Discount
            print("Your total bill with discount will be ",Total)
        else:
            Discount = Amount * 5 / 100
            Total = Amount - Discount
            print("No membership so only 5% discount total bill is : ",Total)

    else : 
        if Amount < 5000:
            print("No discount total bill is ",Amount)

if __name__ =="__main__":
    main()
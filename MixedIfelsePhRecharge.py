#Mobile Recharge 📱

#Take recharge amount.

#₹0–199 → "Basic Plan"
#₹200–499 → "Standard Plan"
#₹500–999 → "Premium Plan"
#₹1000 or above → "Unlimited Plan"

def main():
    amount = int(input("Enter recharge amount : "))
    if amount >= 1000:
        print("Unlimited plan")
        Coupon = input("do you have a extra data coupon? (yes/no) : ")
        if Coupon == "yes":
            print("extra 2 gb added")
        else:
            print("No extra data")

    elif amount >= 500:
        print("premium plan")
        Coupon = input("do you have a extra data coupon? (yes/no) : ")
        if Coupon == "yes":
            print("extra 2 gb added")
        else:
            print("No extra data")

    elif amount >= 200:
            print("standard  plan")
            Coupon = input("do you have a extra data coupon? (yes/no) : ")
            if Coupon == "yes":
                print("extra 2 gb added")
            else:
                print("No extra data")
    else:
        print("Basic plan")
        
        Coupon = input("do you have a extra data coupon? (yes/no) : ")
        if Coupon == "yes":
                print("extra 2 gb added")
        else:
                print("No extra data")

if __name__ == "__main__":
    main()
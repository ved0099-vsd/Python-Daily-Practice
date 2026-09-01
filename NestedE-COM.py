def main():
    Product = input("What do you want ? We have Groceries,Vegetables,Fast food : ")
    Payment = (input("payment completed or not (yes/no) :"))
    Address = input("Please enter your Address : ")

    if Product in ["Groceries","Vegetables","Fast food"]:
        if Payment == "yes":
            if Address == Address:
                print("Your Items will be delivered in 30 mins")
        else:
            print("Paymet no done")
    else:
        print("That product is not avaialable")

if __name__ == "__main__":
    main()
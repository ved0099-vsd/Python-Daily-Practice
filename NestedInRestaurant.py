def main():
    Restaurant = input("is Restaurant Open? (Yes/No) : ")
    Food = input("Whats available ? (PavBhaji,Dosa,Idli) :")
    Payment = input("Payment Done or not ? (Yes/No) :")

    if Restaurant == "Yes":
        if Food in ["PavBhaji","Dosa","Idli"]:
            if Payment == "Yes":
                print("Here is your Food")
            else:
                print("DO paymet sir")
        else:
            print("Sorry its not available")
    else:
        print("Sorry Restaurant is closed")


if __name__ == "__main__":
    main()
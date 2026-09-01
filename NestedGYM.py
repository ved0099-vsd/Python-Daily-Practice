def main():
    Age = int(input("Enter your Age : "))
    Medical = input("Does you have Medical Clearance ? (yes/no) ")
    Payment = input("Payment Done ? (yes/no) : ")

    if Age >= 16:
        if Medical == "yes":
            if Payment == "yes":
                print("Welcome to Ved Fitness club")
            else:
                print("Payment not done")
        else:
            print("Medical Clearance not done")
    else:
        print("you are below 16 bruh")

if __name__ == "__main__":
    main()
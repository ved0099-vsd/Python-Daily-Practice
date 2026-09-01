def main():
    Age = int(input("Enter your Age : "))
    Liscense = input("Do you have a liscense? (Yes/No) : ")
    Budget = int(input("Enter your Budget : "))

    if Age >= 18:
        if Liscense == "Yes":
            if Budget >= 150000:
                print("Yes you can buy a car!!!!!!!!")
            else:
                print("that low budget increase it")
        else:
            print("Go get a liscense first")
    else:
        print("You are a minor you cannot get a liscense and a car too")

if __name__ == "__main__":
    main()
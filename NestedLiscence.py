def main():
    Age = int(input("Enter your Age  :"))
    Status = input("Enter your License Status (yes,no) :")

    if Age >= 18:
        if(Status == "yes"):
            print("You can get a valid driving liscense")
        else:
            print("Go get a driving liscense")

    else:
        print("You are a minor")

if __name__ == "__main__":
    main()
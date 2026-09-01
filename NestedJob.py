def main():
    Age = int(input("Enter Your age : "))
    Qualification = input("Enter your Qaulification is it MSC CS/ BE / BTECH ? :")
    Experiance = int(input("Enter your years of Experiance : "))

    if Age >= 24:
        if Qualification == "MSC CS" or "BE/BTECH":
            if Experiance >= 2:
                print("Yes you are eligible for this INterview")
            else:
                print("You have low experiance")
        else:
            print("DO dont have required qualifiaction")
    else:
        print("Your age is low")

if __name__ == "__main__":
    main()
def main():
    Percentage = float(input("Enter your Percenatge : "))
    Income = int(input("Enter your Family INcome : "))
    Entrance = float(input("Enter your Entrance exam marks : "))

    if Percentage >= 87:
        if Income <= 400000:
            if Entrance >= 93:
                print("You are eligible for Scholarship")
            else:
                print("You have low entrance marks")
        else:
            print("You have high income")
    else:
        print("You have low percentage")

if __name__ == "__main__":
    main()
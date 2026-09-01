def main():
    Marks = int(input("Enter Marks : "))
    Age = int(input("Enter your Age : "))

    if Marks >= 70:
        if(Age >= 19):
            print("Yes you can take admission")
        else:
            print("You are below 19 yo cant take admission here")
    else:
        print("Not eligible")


if __name__ == "__main__":
    main()
def main():
    num1 = int(input("enter first number : "))
    num2 = int(input("enter Second number : "))


    Data = (1,2,355,234,655,86,97,1,9,6,9,69)

    if num1 and num2 in Data:
        print("both numbers are present :" )
    elif num1 in Data:
        print("Only first number is present")
    elif num2 in Data:
        print("Only second number is present")
    else:
        print("Both numbers are absent")

if __name__ == "__main__":
    main()
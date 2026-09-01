def main():
    num1 = int(input("Enter first no. : "))
    num2 = int(input("Enter second no. : "))
    num3 = int(input("Enter third no. : "))

    if(num1 > num2 and num1 > num3):
        print(num1,"is greater")

    elif(num2 > num1 and num2 > num3):
        print(num2,"is greater")
    else:
        print(num3," is greater")

if __name__ == "__main__":
    main()
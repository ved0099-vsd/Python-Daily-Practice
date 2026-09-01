def main():
    Num1 = int(input("Enter first number : "))
    Num2= int(input("Enter second number : "))

    Operator = (input("Enter operator : "))

    if(Operator == "+" ):
        print("Addition will be ",Num1 + Num2)

    elif(Operator == "-"):
        print("Subtraction will be ", Num1 - Num2)

    elif(Operator == "*"):
        print("Multiplication will be ", Num1 * Num2)

    elif(Operator == "/"):
        print("Division will be ",Num1/Num2)



    else:
        print("Invalid Input")

if __name__ == "__main__":
    main()
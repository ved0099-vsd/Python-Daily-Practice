def main():
    Ans = 0
    try:
        No1 = int(input("Enter first number : "))
        No2 = int(input("Enter second number : "))

        Ans = No1 / No2
        print("Division successfull",Ans)

    except ZeroDivisionError as Zobj:
        print("Zero division Error due to second operand is Zero :",Zobj)

    except ValueError as Vobj:
        print("Data type error due to invalid data type : ",Vobj)

    except Exception as Eobj:
        print("other exception occured",Eobj)

    print("Ans is :",Ans)

if __name__ == "__main__":
    main()
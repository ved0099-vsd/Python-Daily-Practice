def main():
    Ans = 0
    try:
        No1 = int(input("Enter first number : "))
        No2 = int(input("Enter second number : "))

        Ans = No1 / No2       
        print("Division successfull : ",Ans)

    except ZeroDivisionError as zobj:   #second operand 0
        print("Zero division error occured because second operand is Zero :",zobj)

    except ValueError as vobj:   # Data type error
        print("Data type error occured due to invalid datatype :",vobj)

    print("Ans is :",Ans)

   

if __name__ == "__main__":
    main()
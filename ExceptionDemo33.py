def main():
    Ans = 0
    try:
        No1 = int(input("Enter first number : "))
        No2 = int(input("Enter second number : "))

        Ans = No1 / No2

        print("Division successfull",Ans)

    except ZeroDivisionError as Zobj:
        print("Zero division error due to Zero : ",Zobj)
    except ValueError as Vobj:
        print("Value error due to invalid Data type :",Vobj)

    print("Ans is ",Ans)

if __name__ == "__main__":
    main() 
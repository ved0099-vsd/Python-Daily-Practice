def main():
    Ans = 0

    try:
        No1 = int(input("Enter first number : "))
        No2 = int(input("enter second number : "))

        Ans = No1 / No2
        print("Ans is :",Ans)

    except ZeroDivisionError as zobj:
        print("Zero division error occured due to second operand is Zero :",zobj)

        print("Ans is :",Ans) 

if __name__ == "__main__":
    main()

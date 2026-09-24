def main():
    Ans = 0
    try:
        No1 = int(input("Enter first number : "))
        No2 = int(input("Enter second number : "))

        Ans = No1 / No2
        print("Division successfull ",Ans)

    except ZeroDivisionError as Zobj:
        print("Error due to second operand zero : ",Zobj)

    except ValueError as Vobj:
        print("data type error because of Invalid data type :",ValueError)

#Exception is a general/base exception. It can catch exceptions that weren't specifically handled by the previous except blocks.
    
    except Exception as Eobj:   #handles other unexpected exceptions.
        print("Exception Occured : ",Eobj)

    print("Ans is :",Ans)       

if __name__ == "__main__":
    main()
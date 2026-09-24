#try → code that may cause an exception
#except → handles the exception
#finally → runs whether exception occurs or not

def main():
    Ans = 0
    try:
        No1 = int(input("Enter first number  :"))
        No2 = int(input("Enter second number : "))

        Ans = No1 / No2
        print("Division is :",Ans)

    except ZeroDivisionError as Zobj:
        print("Zero division occured due to Zero :",Zobj)

    except ValueError as Vobj:
        print("Error due to Data type error : ",Vobj)

    except Exception as Eobj:
        print("Exception occured and handled")

    finally:   #The finally block always executes, whether an exception occurs or not.
        print("Finally inside block")

    print("Ans is :",Ans)

if __name__ == "__main__":
    main()
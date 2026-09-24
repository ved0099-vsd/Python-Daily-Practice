#def

def Addition(No1,No2):
    Ans = No1 + No2
    return Ans

def Sub(No1,No2):
    Ans = No1 - No2
    return Ans

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Ret = Addition(Value1,Value2)
    print("Addition is :",Ret)

    Ret = Sub(Value1,Value2)
    print("Subtraction is :",Ret)

if __name__ == "__main__":
    main()
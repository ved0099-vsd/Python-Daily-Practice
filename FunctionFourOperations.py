def Calculation(Value1, Value2):
    Add = Value1 + Value2
    Sub = Value1 - Value2
    Multi = Value1 * Value2
    Div = Value1 / Value2

    return Add, Sub, Multi , Div

def Display(Ret1,Ret2,Ret3,Ret4):
    print("Addition is",Ret1)
    print("Subtraction is",Ret2)
    print("Multiplication is",Ret3)
    print("Division is",Ret4)

def main():
    Value1 = int(input("Enter a number : "))
    Value2 = int(input("Enter second number : "))

    Ret1, Ret2, Ret3, Ret4 = Calculation(Value1,Value2)

    Display(Ret1,Ret2,Ret3,Ret4)


if __name__ == "__main__":
    main()
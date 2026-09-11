def Subtraction(Value1, Value2):
    Sub = Value1 - Value2
    return Sub

def main():
    Value1 = int(input("Enter a number :"))
    Value2 = int(input("Enter second Number : "))

    Ret = Subtraction(Value1,Value2)
    print("Subtraction is",Ret)

if __name__ == "__main__":
    main()
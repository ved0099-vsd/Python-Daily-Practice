def Addition(Value1,Value2,Value3):
    Add = Value1 + Value2 + Value3
    return Add

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))
    Value3 = int(input("Enter third number : "))

    Ret = Addition(Value1,Value2,Value3)
    print("Addition of 3 numbers is ",Ret)

if __name__ == "__main__":
    main()
def Maximum(Value1,Value2):
    if Value1 > Value2:
        print("Value1 is Maximum",Value1)
    else:
        print("Value2 is greater",Value2)
        return Maximum

def Display(Ret):
    print("Maximum number is : ",Ret)

def main():
    Value1 = int(input("Enter a number : "))
    Value2 = int(input("Enter second number : "))

    Ret = Maximum(Value1,Value2)

    Display(Ret)

if __name__ == "__main__":
    main()
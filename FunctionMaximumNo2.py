def Maximum(Value1, Value2):
    if Value1 > Value2:
        return Value1
    else:
        return Value2

def Display(Ret):
    print("Greater No. is ",Ret)

def main():
    Value1 = int(input("Enter a number : "))
    Value2 = int(input("Enter seconnd Number : "))

    Ret  = Maximum(Value1,Value2)

    Display(Ret)

if __name__ == "__main__":
    main()
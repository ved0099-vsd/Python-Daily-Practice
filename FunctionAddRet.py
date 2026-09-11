def Addition(Value1,Value2):
    Add = Value1 + Value2
    return Add

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second Number  :"))

    Ret = Addition(Value1,Value2)

    print("Addition is ",Ret)



if __name__ == "__main__":
    main()
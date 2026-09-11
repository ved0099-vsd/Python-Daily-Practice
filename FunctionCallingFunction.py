def Addition(Value1,Value2):
    Add = Value1 + Value2
    return Add

def Display(Ret):
    print("Addition is", Ret)

def main():
    Value1  = int(input("Enter a number : "))
    Value2 = int(input("Enter second number  :"))

    Ret = Addition(Value1,Value2)
    Display(Ret)



if __name__ == "__main__":
    main()
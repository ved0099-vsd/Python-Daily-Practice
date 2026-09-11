def Square(Value):
    Sq = Value * Value
    return Sq

def Display(Ret):
    print("Square is ",Ret)

def main():
    Value  = int(input("enter a number  : "))
    Ret  = Square(Value)

    Display(Ret)

if __name__ == "__main__":
    main()
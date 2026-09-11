def Cube(Value):
    Cb = Value * Value * Value
    return Cb

def Display(Ret):
    print("Cube is", Ret)

def main():
    Value  = int(input("Enter your Number : "))

    Ret = Cube(Value)

    Display(Ret)
    

if __name__ == "__main__":
    main()
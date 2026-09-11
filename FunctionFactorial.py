def Factorial(Value):
    Fact = 1

    for i in range(1, Value + 1):
        Fact = Fact * i

    return Fact

def Display(Ret):
    print("Factorial is =", Ret)

def main():
    Value = int(input("Enter a number : "))

    Ret = Factorial(Value)

    Display(Ret)

if __name__ == "__main__":
    main()
def CheckEvenOdd(Value):
    if Value % 2 == 0:
        print("Even",Value)
    else:
        print("Odd",Value)
    return CheckEvenOdd

def main():
    Value  = int(input("Enter a value :"))

    Ret  = CheckEvenOdd(Value)

if __name__ == "__main__":
    main()

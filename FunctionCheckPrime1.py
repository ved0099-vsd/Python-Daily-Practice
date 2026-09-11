def CheckPrime(Value):
    Count = 0

    for  i in range(1, Value + 1):
        if Value % i == 0:
            Count = Count + 1

    if Count == 2:
        return True
    else:
        return False

def Display(Ret):
    if Ret == True:
        print("Number is Prime")
    else:
        print("Number is not Prime")

def main():
    Value = int(input("Enter a number : "))

    Ret  = CheckPrime(Value)

    Display(Ret)

if __name__ == "__main__":
    main()
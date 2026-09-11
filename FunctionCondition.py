def CheckNo(Value):
    if Value > 0 :
        print("Positive")
    elif Value < 0 :
        print("Negative")
    else:
        print("Zero")

    return CheckNo

def main():
    Value = int(input("enter a number : "))

    Ret = CheckNo(Value)

if __name__ == "__main__":
    main()
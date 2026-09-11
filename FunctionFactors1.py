def Factors(Value):
    for i in range(1, Value + 1):
        if Value % i == 0:
            print(i)

def main():
    Value = int(input("Enter a number : "))

    Factors(Value)

if __name__ == "__main__":
    main()
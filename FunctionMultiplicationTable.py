def Table(Value):
    for i in range(1,11):
        Ans = Value * i
        print(Ans)


def main():
    Value  = int(input("Enter a number : "))

    Table(Value)

if __name__ == "__main__":
    main()
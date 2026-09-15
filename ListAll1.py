def main():
    Data = [10, 25, 30, 45, 50, 65, 70]

    Sum = 0
    Maximum = Data[0]
    Minimum = Data[0]
    Even = 0
    Odd = 0

    print("Even numbers :")

    for i in Data:
        Sum = Sum + i

        if i > Maximum:
            Maximum = i

        if i < Minimum:
            Minimum = i

        if i % 2 == 0:
            print(i)
            Even = Even + 1

    print("Odd numbers :")

    for i in Data:
        if i % 2 != 0:
            print(i)
            Odd = Odd + 1

    print("Sum is :", Sum)
    print("Maximum is :", Maximum)
    print("Minimum is :", Minimum)
    print("Even numbers are :", Even)
    print("Odd numbers are :", Odd)

if __name__ == "__main__":
    main()
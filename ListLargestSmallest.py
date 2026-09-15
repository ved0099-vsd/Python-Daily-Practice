def main():
    Data = [45, 12, 78, 23, 56, 9]

    Maximum = Data[0]
    Minimum = Data[0]

    for i in Data:
        if i > Maximum:
            Maximum = i

        if i < Minimum:
            Minimum = i

    print("Maximum is :", Maximum)
    print("Minimum is :", Minimum)

if __name__ == "__main__":
    main()
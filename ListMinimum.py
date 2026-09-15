def main():
    Data = [25, 10, 45, 30, 15]

    Minimum = Data[0]

    for i in Data:
        if i < Minimum:
            Minimum = i

    print("Minimum is :", Minimum)

if __name__ == "__main__":
    main()
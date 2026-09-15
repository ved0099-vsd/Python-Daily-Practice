def main():
    Data = [10, -5, 20, -15, 30, -25]

    Positive = 0
    Negative = 0

    for i in Data:
        if i > 0:
            Positive = Positive + 1
        elif i < 0:
            Negative = Negative + 1

    print("Positive numbers are :", Positive)
    print("Negative numbers are :", Negative)

if __name__ == "__main__":
    main()
def main():
    n = int(input("Enter a number: "))

    total = 0

    for i in range(1, n + 1):
        total = total + (i * i * i)
    print("Sum of cubes =", total)


if __name__ == "__main__":
    main()
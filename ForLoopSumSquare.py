#Find the sum of squares from 1 to n.
#Example: 1² + 2² + 3² + ... + n²

def main():
    n = int(input("Enter a number: "))

    total = 0

    for i in range(1, n + 1):
        total = total + (i * i)

    print("Sum of squares =", total)


if __name__ == "__main__":
    main()
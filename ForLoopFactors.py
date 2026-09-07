#Take a number and print its factors.
#Example: 12 → 1, 2, 3, 4, 6, 12

def main():
    n = int(input("Enter a number: "))

    for i in range(1, n + 1):
        if n % i == 0:
            print(i)


if __name__ == "__main__":
    main()
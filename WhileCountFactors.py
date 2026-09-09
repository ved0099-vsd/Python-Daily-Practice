#Take a number n and count how many factors it has.

def main():
    n = int(input("Enter a number: "))

    i = 1
    count = 0

    while i <= n:
        if n % i == 0:
            count = count + 1

        i = i + 1

    print("Number of factors =", count)


if __name__ == "__main__":
    main()
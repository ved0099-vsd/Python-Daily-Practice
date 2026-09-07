#Take a number and check whether it is a prime number.

def main():
    n = int(input("Enter a number: "))

    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count = count + 1

    if count == 2:
        print("Prime number")
    else:
        print("Not a prime number")


if __name__ == "__main__":
    main()
    
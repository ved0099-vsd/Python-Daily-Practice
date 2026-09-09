#Take a number n and count how many numbers from 1 to n are divisible by 5.

def main():
    n = int(input("Enter a number: "))

    i = 1
    count = 0

    while i <= n:
        if i % 5 == 0:
            count = count + 1

        i = i + 1

    print("Count =", count)


if __name__ == "__main__":
    main()
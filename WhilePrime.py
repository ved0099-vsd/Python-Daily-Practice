#Q8 — Check whether a number is prime using while loop

def main():
    n = int(input("enter a number : "))

    i = 1
    count = 0

    while i <= n:
        if i % 2 == 0:
            count = count + 1

        i = i + 1

    if count == 2:
        print("Prime no.")
    else:
        print("Not a prime no")

if __name__ == "__main__":
    main()
def main():
    n = int(input("Enter a number : "))

    count = 0
    i = 1

    while i <= n:
        if i % 2 == 0:
            count = count + 1
        i = i + 1
    print("Sum of even nos is :",count)

if __name__ == "__main__":
    main()
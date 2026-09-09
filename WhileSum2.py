def main():
    n = int(input("Enter a number : "))

    i = 1
    total = 0

    while i <= n:
        total = total + i
        i = i + 1
    print(total)

if __name__ == "__main__":
    main()
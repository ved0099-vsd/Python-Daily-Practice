#Take a number n and print numbers from n to 1.
def main():
    n = int(input("Enter a number : "))
    i = n

    while i >= 1:
        print(i)
        i = i - 1


if __name__ == "__main__":
    main()
#Take a number n and find how many even numbers are between 1 and n.

def main():
    n = int(input("Enter a number : "))
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)


if __name__ == "__main__":
    main()


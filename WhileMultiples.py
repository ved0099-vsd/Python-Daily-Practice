#Take a number n and print multiples of 5 up to n.

def main():
    n = int(input("Enter a number : "))
    i = 5

    while i <= n:
        print(i)
        i = 5 + i

if __name__ == "__main__":
    main()
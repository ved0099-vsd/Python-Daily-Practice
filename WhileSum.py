#Take a number n and find the sum from 1 to n.

def main():
    n = int(input("Enter a number : "))

    sum = 0
    i = 1

    while i <= n:
        sum = sum + i   #This adds the current i to total.
        i = i + 1       #This increases i by 1.

    print("Sum =", sum)

if __name__ == "__main__":
    main()
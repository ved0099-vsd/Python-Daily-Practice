#Take a number n and find the sum of even numbers from 1 to n.

def main():
    n = int(input("Enter a number : "))
    i = 1
    count = 0

    while i <= n:
        i = i + 2
        count = count + i
    print(count)

if __name__ == "__main__":
    main()
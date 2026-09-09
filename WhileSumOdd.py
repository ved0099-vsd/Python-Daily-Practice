#Take a number n and find the sum of odd numbers from 1 to n.

def main():
    n = int(input("enter a number : "))
    i = 1

    while i <= n:
        print(i)
        i = i + 2

if __name__ == "__main__":
    main()
#Take a number n and print the square of only even numbers from 1 to n.

def main():
    n = int(input("Enter your number : "))
    for i in range(1,n+1):
        if i % 2== 0:
            print(i*i)


if __name__ == "__main__":
    main()
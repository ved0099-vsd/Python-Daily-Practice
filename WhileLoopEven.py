#Take a number n and print only the even numbers from 1 to n.

def main():
    n = int(input("enter a number : "))
    i = 2

    while i <= n:
        print(i)
        i = i + 2

if __name__ == "__main__":
    main()
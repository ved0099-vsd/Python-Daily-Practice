#Take a number n and print all its factors using a while loop.

def main():
    n = int(input("enter a number : "))
    i = 1

    while i <= n:
        if n % i == 0:
            print(i)
        i = i + 1
        

if __name__ == "__main__":
    main()
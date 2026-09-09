#Take a number n and find the sum of its factors.

def main():
    n = int(input("enter a number : "))
    i = 1
    count = 0

    while i <= n:
        if n % i == 0:
            count = count + i
        i = i + 1
    print(count)
        

if __name__ == "__main__":
    main()
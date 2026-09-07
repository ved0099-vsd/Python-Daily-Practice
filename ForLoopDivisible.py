#Take a number n and find how many numbers are divisible by 3 between 1 and n.

def main():
    n = int(input("enter a number : "))
    count = 0
    for i in range(1,n+1):
        if i % 3 == 0:
            count = count + 1
    print(count)
            


if __name__ == "__main__":
    main()
#Take a number n and print multiples of 2 and 3 from 1 to n.

def main():
    n = int(input("Enter a number : "))
    for i in range(1,n+1):
        if i % 2 == 0 and i % 3 == 0:
            print(i)

if __name__ == "__main__":
    main()
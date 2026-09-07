#Take a number n and print only numbers less than 10 from 1 to n.

def main():
    n = int(input("Enter a number : "))
    for i in range(1,n+1):
        if i < 10:
            print(i)

if __name__ == "__main__":
    main()
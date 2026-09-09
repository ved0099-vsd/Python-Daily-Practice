#Take a number n and print the square of every number from 1 to n.

def main():
    n = int(input("Enter a number : "))
    i = 1
    while i <= n:
        print(i,"=",i*i)
        i = i + 1



if __name__ == "__main__":
    main()
#Print the square of all even numbers from 1 to n.

def main():
    n = int(input("Enter a numebr : "))
    for i in range(1,n+1):
        if i % 2 == 0:

            print("Square of",i,"is",i*i)


if __name__ == "__main__":
    main()
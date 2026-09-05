#Print the cube of all odd numbers from 1 to n.

def main():
    n = int(input("enter a number : "))
    for i in range(1,n+1,2):
        if i % 2 != 0:
            print("Cube of",i,"is",i*i*i)

if __name__ == "__main__":
    main()
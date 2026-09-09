#Take a number and print its multiplication table from 1 to 10.

def main():
    n = int(input("enter a number : "))
    i = 1

    while i <= 10:
        print(n,"X",i,"=",n*i)
        i = i + 1


if __name__ == "__main__":
    main()
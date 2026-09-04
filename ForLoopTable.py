#Take a number from the user and print its table from 1 to 10.

def main():
    num = int(input("ENter a number :"))

    for i in range(1,11):
        print(num, "x", i, "=", num * i)


if __name__ == "__main__":
    main()
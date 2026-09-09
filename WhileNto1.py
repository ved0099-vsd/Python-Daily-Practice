#Take a number n and print numbers from n to 1.

def main():
    n = int(input("Enter a number : "))

    i = n     #we want to start counting from the number the user enters.

    while i >= 1:
        print(i)
        i = i - 1


if __name__ == "__main__":
    main()
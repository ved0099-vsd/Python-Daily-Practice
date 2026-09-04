def main():
    n = int(input("Enter a number : "))

    factorial = 1

    for i in range (1, n +1 ):
        factorial = factorial * i

    print("Factorial = ",factorial)

if __name__ == "__main__":
    main()
#Q10 — Find factorial using while loop

def main():
    n = int(input("Enter a number : "))

    i = 1
    factorial = 1

    while i <= n:
        factorial = factorial * i
        i = i + 1
    print(factorial)

if __name__ == "__main__":
    main()
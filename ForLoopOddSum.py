def main():
    n = int(input("Enter a number : "))
    total = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            total = total + i
    print("sum of Odd nos is", total)
            

if __name__ == "__main__":
    main()
def main():
    n = int(input("Enter a number : "))
    total = 0
    if n % 2 == 0:
        for i in range(1,n+1):
            total = total + i
        print("Sum =",total)
    else:
        print("its a odd so no sum")

if __name__ == "__main__":
    main()
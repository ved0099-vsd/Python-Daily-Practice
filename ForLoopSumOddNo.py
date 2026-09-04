def main():
    n = int(input("Enter a number"))
    count = 0

    for i in range (1,n + 1):
        if i % 2!= 0:
            count = count + 1
    print("Count of odd nos is = ", count)
        


if __name__ == "__main__":
    main()
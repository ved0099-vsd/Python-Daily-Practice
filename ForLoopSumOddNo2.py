def main():
    n = int(input("Enter number : "))
    Count = 0

    for i in range(1,n + 1):
        if i % 2 != 0:
            Count = Count + 1
    print("Count of all nos is : ",Count)
    


if __name__ == "__main__":
    main()
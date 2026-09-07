def main():
    n = int(input("Enter a number : "))
    count = 0

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            count = count +1 

    print("COunt =", count)



if __name__ == "__main__":
    main()
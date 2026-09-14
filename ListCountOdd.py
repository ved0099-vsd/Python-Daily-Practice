def main():
    Data = [10,21,32,43,54,65]
    Count = 0

    for i in Data:
        if i % 2 != 0:
            Count = Count + 1
    print("Odd numbers are : ", Count)

if __name__ == "__main__":
    main()
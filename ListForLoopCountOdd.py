# Count odd numbers

def main():
    Data = [10,21,30,41,50,63]
    Count = 0

    for i in Data:
        if i % 2 != 0:
            Count = Count + 1

    print("Odd numbers are : ", Count)

if __name__ == "__main__":
    main()
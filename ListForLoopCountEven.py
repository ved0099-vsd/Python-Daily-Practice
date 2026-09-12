# Count even numbers

def main():
    Data = [10,21,30,41,50]
    Count = 0

    for i in Data:
        if i % 2 == 0:
            Count = Count + 1

    print("Even numbers are :",Count)

if __name__ == "__main__":
    main()
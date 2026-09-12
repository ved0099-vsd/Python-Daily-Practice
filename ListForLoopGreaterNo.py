# Count numbers greater than 25

def main():
    Data = [10,30,15,40,20,50]
    Count = 0

    for i in Data:
        if i > 25:
            Count = Count + 1

    print("Numbers greater than 25 :", Count)

if __name__ == "__main__":
    main()
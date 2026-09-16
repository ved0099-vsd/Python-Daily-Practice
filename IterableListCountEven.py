def CountEven(Data):
    Count = 0

    for no in Data:
        if no % 2 == 0:
            Count = Count + 1

    return Count

def main():
    Data = [10,12,13,54,32,65,79,69,98]

    Ret = CountEven(Data)

    print("Count of Even numbers is : ", Ret)
if __name__ == "__main__":
    main()
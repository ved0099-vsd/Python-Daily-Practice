def Count(Data):
    Count = 0

    for no in Data:
        Count = Count + 1

    return Count

def main():
    Data = [10,20,30,40,50]

    Ret = Count(Data)

    print("Number of elements : ", Ret)


if __name__ == "__main__":
    main()
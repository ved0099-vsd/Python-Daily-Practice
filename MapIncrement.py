def Increment(No):
    return No + 1

def main():
    Data = [23,54,23,56,68,89,46,24]
    print("Data is : ",Data)

    MData = list(map(Increment,Data))
    print("Data after mapping is : ", MData)


if __name__ == "__main__":
    main()
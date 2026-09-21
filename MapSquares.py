def Square(No):
    return No * No

def main():
    Data = [12,56,78,90,88,77,66,55]
    print("Data is ",Data)

    MData = list(map(Square,Data))
    print("Data after Mapping is : ",MData)

if __name__ == "__main__":
    main()
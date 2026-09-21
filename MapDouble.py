def Double(No):
    return No * 2

def main():
    Data = [4,14,23,45,67,89,9,87,65,43,21]
    print("Data is : ",Data)

    MData = list(map(Double,Data))
    print("Data after Mapping is : ",MData)



if __name__ == "__main__":
    main()
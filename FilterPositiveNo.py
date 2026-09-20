def PositiveNo(No):
    return No > 0

def main():
    Data = [23,43,56,-23,0,-54,-4,8765,234567,-987654]

    print("Input Data is : ", Data)

    FData = list(filter(PositiveNo,Data))

    print("Data after Filter is : ", FData)

if __name__ == "__main__":
    main()
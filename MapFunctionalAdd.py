Add10 = lambda No : No + 10

def main():
    Data = [23,45,67,89,87,65,43]
    print("Data is :",Data)

    MData = list(map(Add10,Data))
    print("Data after mapping is : ",MData)

if __name__ == "__main__":
    main()
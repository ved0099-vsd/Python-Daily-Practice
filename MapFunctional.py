# Functional Lambda

CheckEven = lambda No : No % 2 == 0

Increment = lambda No : No + 1

def main():
    Data = [12,45,87,55,44,24,65,90]

    print("Data is :",Data)

    FData = list(filter(CheckEven,Data))

    print("Data after filter is : ",FData)

    MData = list(map(Increment,FData))

    print("Data after Map is : ",MData)

if __name__ == "__main__":
    main()
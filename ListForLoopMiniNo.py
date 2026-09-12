# Find Minimum number

def main():
    Data = [10,50,20,40,30]

    Minimum = Data[0]

    for i in Data:
        if i < Minimum :
            Minimum = i

    print("Maximum is : ", Minimum)

if __name__ == "__main__":
    main()
Square = lambda No : No * No

def main():
    Data = [5,13,24,65,56,3]
    print("Data is : ",Data)

    MData = list(map(Square,Data))  #map() → changes/transforms elements
    print("Data after Map is :",MData)

if __name__ == "__main__":
    main()
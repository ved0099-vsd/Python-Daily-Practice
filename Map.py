#Filter = select, Map = transform.

def CheckEven(No):
    return No % 2 == 0

def Increment(No):   #Increment() adds 1 to every element:
    return No + 1

def main():
    Data = [12,45,65,77,66,24,86]

    print("Data is : ",Data)

    FData = list(filter(CheckEven,Data))   #filter() → selects elements

    print("Data after Filter is :",FData)

    MData = list(map(Increment,FData))      #map() → modifies every selected element

    print("Data after Map is : ",MData)

if __name__ == "__main__":
    main()
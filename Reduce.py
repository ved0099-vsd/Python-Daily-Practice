# filter() → SELECT
# map()    → TRANSFORM
# reduce() → COMBINE

#reduce() is especially useful for things like sum, multiplication, maximum, minimum, etc.

from functools import reduce

def CheckEven(No):
    return No % 2 == 0

def Increment(No):
    return No + 1

def Addition(No1,No2):
    return No1 + No2

def main():
    Data = [2,4,6,8,23,53,65,78]
    print("Data is :",Data)

    FData = list(filter(CheckEven,Data))   #Only even numbers remain.
    print("Data after filter is :",FData)      

    MData = list(map(Increment,FData))     #Increment() adds 1 to every number:
    print("Data after mapping is : ",MData)

    RData = reduce(Addition,MData)        #This combines all elements into one final value.
    print("Data after Reduce is : ",RData)

if __name__ == "__main__":
    main()

#                  Data
#                    ↓
#                 filter()
#                    ↓
#                  FData
#                    ↓
#                  map()
#                    ↓
#                  MData
#                    ↓
#                 reduce()
#                    ↓
#             One final value
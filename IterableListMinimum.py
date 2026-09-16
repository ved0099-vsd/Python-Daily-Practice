def Minimum(Data):
    Min = Data[0]

    for no in Data:
        if no < Min:
            Min = no

    return Min

def main():
    Data = [78,90,56,98,77]

    Ret = Minimum(Data)

    print("Minimum number is : ",Ret)

if __name__ == "__main__":
    main()
def Maximum(Data):
    Max = Data[0]

    for no in Data:
        if no > Max:
            Max = no

    return Max

def main():
    Data = [78,43,45,67,99]

    Ret = Maximum(Data)

    print("Maximum number is : ", Ret)


if __name__ == "__main__":
    main()
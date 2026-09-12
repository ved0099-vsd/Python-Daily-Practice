# Find Maximum number

def main():
    Data = [10,50,20,40,30]

    Maximum = Data[0]

    for i in Data:
        if i > Maximum:
            Maximum = i

    print("Maximum is : ", Maximum)

if __name__ == "__main__":
    main()
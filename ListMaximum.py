def main():
    Data = [25, 10, 45, 30, 15]

    Maximum = Data[0]

    for i in Data:
        if i > Maximum:
            Maximum = i

    print("Maximum is :", Maximum)

if __name__ == "__main__":
    main()
    
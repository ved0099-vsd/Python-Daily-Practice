def main():
    Data = [1,2,3,4,5,6,7,8,9]

    for no in Data:
        print(no)

    Data[3] = 69
    print("-" * 20)

    for no in Data:
        print(no)


if __name__ == "__main__":
    main()
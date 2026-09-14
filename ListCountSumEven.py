def main():
    Data = [10,21,32,43,54,65]
    Sum = 0

    for i in Data:
        if i % 2 == 0:
            Sum = Sum + i

    print("Sum of even numbers is : ", Sum)

if __name__ == "__main__":
    main()
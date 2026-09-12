# Sum of Even Numbers

def main():
    Data = [10,21,30,41,50,63]
    Sum = 0

    for i in Data:
        if i % 2 == 0:
            Sum = Sum + i

    print("Sum of even numbers : ", Sum)

if __name__ == "__main__":
    main()
def main():
    name = str(input("enter a name : "))

    Data = ("Ved","Dhamal","Vedant")

    if name in Data:
        print("that name is present ")
    else:
        print("name is absent")

if __name__ == "__main__":
    main()
def main():
    Battery = int(input("enter battery percentage : "))

    if(Battery > 25):
        print("Sufficient Battery....")
    else:
        print("Low Battery  :")

if __name__ == "__main__":
    main()
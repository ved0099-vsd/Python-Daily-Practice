def main():
    print("Enter first no. : ")
    no1 = int(input())

    print("Enter second no. : ")
    no2 = int(input())

    if(no1 < no2):
        print(no1,"is smaller")
    else:
        print(no2,"is smaller")

if __name__ == "__main__":
    main()
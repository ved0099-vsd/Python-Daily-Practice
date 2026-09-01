def main():
    print("enter a number :")
    no = int(input())

    if(no % 5 == 0):
        print("it belongs to 5's table ")
    else:
        print("it does not belong to 5's table")

if __name__ == "__main__":
    main()
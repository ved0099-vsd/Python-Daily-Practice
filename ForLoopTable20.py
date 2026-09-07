def main():
    num = int(input("Enter a number : "))
    for i in range (1, num + 1 ):
        print(num, "X" , i , "=", num * i)

if __name__ == "__main__":
    main()
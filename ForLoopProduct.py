def main():
    n = int(input("Enter a  number : "))
    product = 1
    for i in range(1,n+1):
        product = product * i
    print(product)
        

if __name__ == "__main__":
    main()
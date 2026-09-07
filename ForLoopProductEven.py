#Find the product of all even numbers from 1 to n.

def main():
    n = int(input("Enter a number : "))
    product = 1                         #Because 1 is the starting value for multiplication.

    for i in range(1,n+1,1):
        if i % 2== 0:
            product = product * i
    print("Product of even nos is", product) 




if __name__ == "__main__":
    main()
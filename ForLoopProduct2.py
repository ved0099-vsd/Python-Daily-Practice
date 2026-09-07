#Take a number n and find the product of only odd numbers from 1 to n.

def main():
    n = int(input("Enter a number : "))
    product = 1

    for i in range(1,n+1):
        if i % 2!= 0:
            product = product * i

    print(product)

        


if __name__ == "__main__":
    main()
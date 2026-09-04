#Sum of 1 to N ➕
#Take a number n and calculate the sum from 1 to n.

def main():
    n = int(input("Enter a number : "))

    total = 0                      #Variable to store our answer

    for i in range(1,n + 1):
        total = total + i

    print("Sum =", total)
    

if __name__ == "__main__":
    main()
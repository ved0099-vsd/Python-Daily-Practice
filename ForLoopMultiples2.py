#Print the first 10 multiples of a number.

def main():
    n = int(input("enter a number : "))
    count = 0

    for i in range(1,51,3):
        if n <= 50:
            count = count + n
        print(count)        
            

if __name__ == "__main__":
    main()
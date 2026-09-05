#Count how many numbers between 1 and n are divisible by 3.

def main():
    n = int(input("enter a number : "))
    for i in range(1,n + 1):
        if i % 3 == 0:
            print(i)

if __name__ == "__main__":
    main()
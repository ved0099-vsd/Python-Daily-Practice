#Take a number n and print only numbers greater than 5 from 1 to n.

def main():
    n = int(input("Enter a number : "))
    for i in range (1,n+1):
        if i > 5:
            print(i)
    
    

if __name__ == "__main__":
    main()
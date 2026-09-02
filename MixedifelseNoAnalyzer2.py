#Number Analyzer 🔢

#Take a number and determine:

#Positive or negative
#Even or odd
#Divisible by 5 or not

def main():

    num = float(input("Enter a number : "))

    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

    if num % 10 == 0:
        print("Divisible by 10")
    else:
        print("Not divisible by 10")

if __name__ == "__main__":
    main()
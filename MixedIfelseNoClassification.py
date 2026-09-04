#Set 5 — 10 Questions
#1. Number Classification 🔢

#Take a number and print whether it is:

#Positive even
#Positive odd
#Negative even
#Negative odd
#Zero

def main():
    Num = int(input("Enter a number : "))

    if Num == 0:
        print("Zero")

    elif Num > 0:
        if Num % 2 == 0:
            print("Positive Even")
        else:
            print("Positive Odd")

    else:
        
        if Num % 2 == 0:
            print("negative even")
        else:
            print("negative odd")
        





if __name__ == "__main__":
    main()
#Leap Year 📅

#Take a year.

#A year is a leap year if:
#It is divisible by 400 OR
#It is divisible by 4 but not divisible by 100.

def main():
    Year = int(input("Enter a year :"))

    if Year % 400 == 0:
        print("its a leap year",Year)
    elif Year % 4 == 0 and Year % 100 != 0:
        print("its a leap year")
    else:
        print("its not A LEAP YEAR")

if __name__ == "__main__":
    main()
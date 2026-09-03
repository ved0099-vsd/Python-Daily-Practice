#Temperature 🌡️

#Take temperature in Celsius.

#Below 10 → Cold
#10–25 → Pleasant
#26–35 → Hot
#Above 35 → Very hot

#Print the appropriate message.

def main():
    Temp = int(input("Enter Temperature "))

    if Temp >= 35:
        print("its too hot")
    elif Temp >= 26:
        print("its hot")
    elif Temp >= 10:
        print("its pleasant")
    else:
        print("COLD")

if __name__ == "__main__":
    main()
def main():

    Fuel = int(input("Enter Fuel Percentage :"))

    if(Fuel <= 15):
        print("Critical Low")

    elif(Fuel <= 25):
        print("Low Fuel")

    elif(Fuel <= 50):
        print("Medium Fuel")  

    elif(Fuel <= 75):
        print("Good Fuel")  

    elif(Fuel >= 76):
            print("Full Tank")  

if __name__ == "__main__":
    main()
def main():
    Signal = input("enter Signal Colour : ")

    if(Signal == "Red"):
        print("STOP")

    elif(Signal == "Orange"):
        print("WAIT")

    elif(Signal == "Green"):
        print("GO")

    else:
        print("Invalid Colour")

if __name__ == "__main__":
    main()
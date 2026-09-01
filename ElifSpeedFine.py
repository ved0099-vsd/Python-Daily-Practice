def main():
    Speed = int(input("Enter speed : "))

    if(Speed >= 120):
        print("2000 Fine")

    elif(Speed >= 90):
        print("1000 fine")

    else:
        print("No Fine")
if __name__ == "__main__":
    main()
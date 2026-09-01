def main():
    print("Enter your amount : ")
    amount = int(input())

    if(amount >= 1000):
        print("Free delivery")
    else:
        print("Delivery charges applicable")

if __name__ == "__main__":
    main()
def main():
    Room = input("Room available? (YES/NO):  ")
    Payment = input("Payment Done or NOT (Done/No) : ")

    if Room == "YES":
        if Payment == "Done":
            print("Here are your Keys....!")
        else:
            print("Please DO Payment")
    else:
        print("Sorry NO Room avaialble right now")

if __name__ == "__main__":
    main()
import threading

def Display():
    print("Inside display :",threading.get_ident()) #threading.get_ident() gives the ID of the thread that is currently executing the code.

def main():
    print("Inside display : ", threading.get_ident()) #threading.get_ident() gives the ID of the thread that is currently executing the code.
    Display()

if __name__ == "__main__":
    main()
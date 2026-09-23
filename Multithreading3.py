import threading

def Display():
    print("inside display : ",threading.get_ident())

def main():
    print("Inside display : ",threading.get_ident())

    tobj = threading.Thread(target=Display) # new thread--target=Display means the function that the thread should execute.

    tobj.start() #starts the new thread.

if __name__ == "__main__":
    main()
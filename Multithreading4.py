import threading

def Display():
    print("inside display : ",threading.get_ident())

def main():
    print("inside : ",threading.get_ident())

    tobj = threading.Thread(target=Display)

    tobj.start()

if __name__ == "__main__":
    main()
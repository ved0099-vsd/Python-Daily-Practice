import threading

def Display(No):
    print(f"inside Display {No} : ",threading.get_ident())

def main():
    print("Inside Main : ",threading.get_ident())

    tobj = threading.Thread(target=Display, args = (11,))

    tobj.start()

if __name__ == "__main__":
    main()
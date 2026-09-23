import threading

def Display(No1,No2,No3):
    print(f"inside Display {No1},{No2},{No3} :", threading.get_ident())

def main():
    print("inside main :",threading.get_ident())

    tobj = threading.Thread(target=Display, args = (43,45,56))

    tobj.start()


if __name__ == "__main__":
    main()
import threading

def Display(No):    # def Display(*No)
    print(f"inside display {No} : ", threading.get_ident())

def main():
    print("inside main :",threading.get_ident())

    tobj = threading.Thread(target=Display, args = (11,)) #Run Display() and pass 11 as its argument.

    tobj.start()

#Why (11,)?
#args expects a tuple of arguments.

(11,) # tuple containing 11
(11)  # simply the number 11


if __name__ == "__main__":
    main()
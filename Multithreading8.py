import threading

def Display(No, No1 , No2):
    print(f"inside Display {No},{No1},{No2} :",threading.get_ident())

def main():
    print("inside main : ",threading.get_ident())

    tobj = threading.Thread(target=Display, args = (11,62,34))

    tobj.start()

if __name__ == "__main__":
    main()

#Why args=(11,21,51,)?
#args expects the arguments as a tuple.

#The final comma is optional when there are multiple values:
(11,21,51)

#But for one argument, the comma is important:
(11,)   # tuple
(11)    # integer
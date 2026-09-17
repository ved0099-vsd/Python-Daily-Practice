no = 12            #Global

def Display():
    a = 32          #Local

    print("From display : ", no)

    print("From Display value of a is : ", a)

def Demo():

    print("From demo value of a is : ", a)

    print("From demo : ", no)

Display()
Demo()
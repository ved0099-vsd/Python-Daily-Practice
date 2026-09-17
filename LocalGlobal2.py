no = 12  #Global

def Display():

    no = 23    #Local

    print("From Display : ", no)

print("Before : ", no)

Display()

print("After : ", no)
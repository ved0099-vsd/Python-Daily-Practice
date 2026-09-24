class Demo:  #Creates a class named Demo.
    def __init__(self):     #__init__() is a special method called a constructor.
        print("Inside constructor")

obj1 = Demo()  #This creates the first object.
obj2 = Demo()  #This creates the second object.

#Demo class
#    ↓
#obj1 = Demo()
#    ↓
#__init__()
#    ↓
#Inside constructor

#obj2 = Demo()
#    ↓
#__init__()
#    ↓
#Inside constructor
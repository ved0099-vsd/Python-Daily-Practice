#__init__() → constructor → called when object is created
#__del__() → destructor → called when object is being destroyed

class Demo:
    def __init__(self):
        print("inside Constructor")

#__del__() is called when an object is being destroyed/garbage-collected.

    def __del__(self):
        print("inside destructor")

obj1 = Demo()
obj2 = Demo()

print("End of application")
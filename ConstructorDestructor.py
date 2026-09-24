class Demo:
    def __init__(self):
        print("inside constructor")

    def __del__(self):
        print("inside destructor")

obj1 = Demo()
obj2 = Demo()

print("End of application")
class Ved:
    #Class Variable
    No1 = 11
    No2 = 12

    def __init__(self):
        #Instance Variable
        self.value1 = 21
        self.value2 = 51
        self.value3 = 91

print(Ved.No1)
print(Ved.No2)

#Object or Instance Creation

mobj1 = Ved()
mobj2 = Ved()
mobj3 = Ved()

print(mobj1.value1)
print(mobj2.value2)
print(mobj3.value3)


#Main difference
#Class Variable	     |     Instance Variable
#No1, No2	         |      value1, value2
#Belongs to class	 |     Belongs to object
#Marvellous.No1	     |       mobj1.value1
#Shared by objects	 |     Each object has its own copy
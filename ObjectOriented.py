class Arithmetic:                   #Creates a class named Arithmetic.
    def Addition(self,No1,No2):     #Addition() is a method inside the class | self represents the current object.
        Ans = No1 + No2
        return Ans

    def Subtraction(Self,No1,No2):
        Ans = No1 - No2
        return Ans

Aobj = Arithmetic()              #This creates an object of the Arithmetic class.

Value1 = int(input("Enter a number : "))
Value2 = int(input("Enter second number  :"))

Ret = Aobj.Addition(Value1,Value2)    #This calls the Addition() method using the object Aobj.

print("Addition is : ",Ret)

Ret = Aobj.Subtraction(Value1,Value2)
print("Subtraction is :",Ret)
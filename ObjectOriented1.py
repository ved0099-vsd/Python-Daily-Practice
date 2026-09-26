class Arithmetic:
    def Multiplication(Self,No1,No2):
        Ans = No1 * No2
        return Ans

    def Division(Self,No1,No2):
        Ans = No1 / No2
        return Ans

Aobj = Arithmetic()

Value1 = float(input("Enter first number : "))
Value2 = float(input("Enter second Number : "))

Ret = Aobj.Multiplication(Value1,Value2)
print("Multiplication is : ",Ret)

Ret = Aobj.Division(Value1,Value2)
print("Division is :",Ret)
class Arithmetic:
    def Addition(Self,No1,No2):
        Ans = No1 + No2
        return Ans
    
    def Sub(Self,No1,No2):
        Ans = No1 - No2
        return Ans

    def Multi(Self,No1,No2):
        Ans = No1 * No2
        return Ans

    def Division(Self,No1,No2):
        Ans = No1 / No2
        return Ans

Aobj = Arithmetic()

Value1 = float(input("Enter first number : "))
Value2 = float(input("Enter second number : "))

Ret = Aobj.Addition(Value1,Value2)
print("Add is :",Ret)

Ret = Aobj.Sub(Value1,Value2)
print("Sub is :",Ret)

Ret = Aobj.Multi(Value1,Value2)
print("multi is :",Ret)

Ret = Aobj.Division(Value1,Value2)
print("Div is :",Ret)